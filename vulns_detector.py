import concurrent.futures
import google.generativeai as genai
from typing import List
import markdown
import time
import random
import json
from duckduckgo_search import DDGS
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


# Define multiple API keys for concurrent requests (replace these with actual keys)
api_keys = [
    #GEMINI_API_KEY_1,
    #GEMINI_API_KEY_2,
    #GEMINI_API_KEY_3,
    #GEMINI_API_KEY_4,
    #GEMINI_API_KEY_5,
    #.................
]
random.shuffle(api_keys)

# Safety settings for Google Gemini
safe = [
    {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

# List of vulnerabilities
list_of_vulns = [
    "Webview XSS via DeepLink",
    "Injection",
    "Steal Password ResetTokens/MagicLoginLinks",
    "Security Logging and Monitoring Failures",
    "Cryptographic Failures",
    "Steal Files using Fileprovider via Intents",
    "Identification and Authentication Failures",
    "Insecure Design",
    "Reading User Email via Broadcasts",
    "HardCoded Credentials",
    "Insecure Activity Handling",
    "Server-Side Request Forgery (SSRF)",
    "Webview XSS via Exported Activity",
    "Broken Authentication",
    "Man-In-the-Middle Attack",
    "Vulnerable and Outdated Components",
    "Intent Sniffing Between Two Applications",
    "Software and Data Integrity Failures",
    "Code Execution via Malicious App",
    "Logic Flaws",
    "Broken Access Control",
    "Security Misconfiguration",
    "Insecure Input Validation",
    "Steal Files via Webview using XHR request"
]

# Split vulnerabilities into chunks of 8
def chunk_vulns(vulns, chunk_size):
    for i in range(0, len(vulns), chunk_size):
        yield vulns[i:i + chunk_size]

# Function to call Gemini API with a subset of vulnerabilities
def process_vulns(api_key: str, vulns: List[str], code: str):
    genai.configure(api_key=api_key)

    # Prompt setup
    generation_config = {
        "temperature": 0.5,
        "top_p": 1,
        "top_k": 74,
        "max_output_tokens": 10000,
        "response_mime_type": "text/plain",
    }

    gemini_model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-exp-0827",
        generation_config=generation_config,
        safety_settings=safe
    )

    prompt = (
        "You are a Cyber Security analyst with expertise in code analysis and vulnerability assessment. "
        "Your task is to thoroughly examine the following code for specific vulnerabilities. "
        "Please ensure that your analysis is accurate and comprehensive, taking special care to identify any "
        "vulnerabilities that might be easily overlooked.\n\n"

        "### Vulnerabilities to Check:\n"
        f"- {', '.join(vulns)}\n\n"

        "### Code to Analyze:\n"
        f"```\n{code}\n```\n\n"

        "### Instructions:\n"
        "1. **Identify Vulnerabilities:** Check the code for the listed vulnerabilities, providing specific examples and line references where applicable.\n"
        "I Want every vulnerability you can find In the code. "
        "Please ensure your analysis is clear, well-structured, and easy to understand, making it straightforward to follow your findings. "
        "Do not provide recommendations, only identify the vulnerabilities."
    )

    response = gemini_model.generate_content(prompt, safety_settings=safe)

    # Return the text response from the model
    return response.text

# Main function to handle concurrent processing
def concurrent_vulnerability_scan(code: str):
    vulns_chunks = list(chunk_vulns(list_of_vulns, 8))
    report = ""  # Initialize report string to store all results
    start_time = time.time()  # Start the timer

    # Use ThreadPoolExecutor for concurrency
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(api_keys)) as executor:
        futures = []
        for i, vulns_chunk in enumerate(vulns_chunks):
            api_key = api_keys[i % len(api_keys)]  # Rotate API keys if more chunks than keys
            print(f"Starting future {i+1} for vulnerabilities: {vulns_chunk}")
            futures.append(executor.submit(process_vulns, api_key, vulns_chunk, code))

        # Collect results and log when they are done
        for future in concurrent.futures.as_completed(futures):
            print(f"Future {futures.index(future) + 1} Processing Completed Sucessfully.")
            result = future.result()
            report += f"### Vulnerability Scan Result for Future {futures.index(future) + 1}:\n{result}\n\n"

    # End the timer
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total time to complete the task: {elapsed_time:.2f} seconds")

    # Save the report to a file
    with open('Temp/vulns_detected.txt', 'w', encoding='utf-8') as file:
        file.write(report)
    print("Vulnerability scan report saved to vulns_detected.txt.")

    # Display final report
    markdown.markdown(report)

    return report

# Process and convert the report into JSON
import os
from openai import OpenAI

def generate_vulns_json(report: str):
    client = OpenAI(
        api_key= os.getenv("GITHUB_TOKEN"),

        base_url="https://models.inference.ai.azure.com",
    )
    # extract the file names from the file codee_files_list.txt
    with open('Temp/code_files_list.txt', 'r', encoding='utf-8') as f:
        files_list = f.read()



    query = (
        "convert the data into a single JSON output of file name and vulnerabilities in it "
        "and I don't include other character (not even ''' or JSON) than the dictionary "
        "ex { 'File_name'(no file extension is needed) : [vuln1,vuln2...],} "
        "(where file_name is the name of the file where the vulnerabilities are identified and "
        "vuln1,vuln2...... are names of the vulnerabilities that are identified in that particular file "
        "(make sure to get the filenames and vulnerabilities names correctly for example if filename is build.gradle just use build as the filename and .gradle is the file extension and another example is not to include the folder path to the file name as example app/buils where app is folder name and build is file name and I just need the filename and not the folder path i.e, return build not app/build or build.gradle)Note : for app/build file just  only return 'build'  as the File name only)"
        "Note : You should only return me a JSON output that includes files that has vulnerabilitites in it and not the files that does not have any vulnerabilities in it (Just don't include them in the JSON) "
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant .",
            },
            {
                "role": "user",
                "content": f"{query} {files_list} {report}",
            },
        ],
    )

    results = response.choices[0].message.content
    
    vulns_dict = json.loads(results)
    print(type(vulns_dict))
    print(vulns_dict)
    return vulns_dict

# Getting the whole code
def vulns_detector():
    temp_dir = os.path.join('Temp')
    combined_file = os.path.join(temp_dir, "combined_text_files.txt")
    
    with open(combined_file, 'r', encoding='utf-8') as file:
        code = file.read()

    # Run the vulnerability scan
    rep = concurrent_vulnerability_scan(code)
    
    # Generate JSON from the report
    vulns_dict=generate_vulns_json(rep)
    return vulns_dict
