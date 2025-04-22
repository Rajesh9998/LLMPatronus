import logging
from fpdf import FPDF
import google.generativeai as genai
from typing import List
import itertools
import random
import concurrent.futures
from together import Together
from duckduckgo_search import DDGS
import time
from pinecone import ServerlessSpec
from pinecone import Pinecone
import getpass
import os
from files_crawler import files_crawler
from vulns_detector import vulns_detector
from moa_analysis import moa_analysis
from google.api_core.exceptions import ResourceExhausted, InternalServerError
import sys
import PyPDF2

from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


# Custom logging formatter
class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

# Configure logging
logger = logging.getLogger("LLMPatronous")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

# Initialize PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

# Initialize text file for logging
log_file_path = os.path.join('Temp', 'temp_output.txt')
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

def log_to_txt(text):
    with open(log_file_path, 'a', encoding='utf-8') as f:
        f.write(text + '\n')

def print_banner():
    banner = """
    ██╗     ██╗     ███╗   ███╗██████╗  █████╗ ████████╗██████╗  ██████╗ ███╗   ██╗ ██████╗ ██╗   ██╗███████╗
    ██║     ██║     ████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║██╔═══██╗██║   ██║██╔════╝
    ██║     ██║     ██╔████╔██║██████╔╝███████║   ██║   ██████╔╝██║   ██║██╔██╗ ██║██║   ██║██║   ██║███████╗
    ██║     ██║     ██║╚██╔╝██║██╔═══╝ ██╔══██║   ██║   ██╔══██╗██║   ██║██║╚██╗██║██║   ██║██║   ██║╚════██║
    ███████╗███████╗██║ ╚═╝ ██║██║     ██║  ██║   ██║   ██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝╚██████╔╝███████║
    ╚══════╝╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚══════╝
                                                                                                    
    """
    print("\033[95m" + banner + "\033[0m")
    print("\033[94m" + "Welcome to LLMPatronous - Your AI-Powered Security Guardian" + "\033[0m")
    print("\033[94m" + "Version: 1.0.0" + "\033[0m")
    print("\033[94m" + "Developed by: Rajesh Yarra" + "\033[0m")
    print("\033[94m" + "=" * 80 + "\033[0m")

def query_gemini(user_query: str, top_k: int = 100) -> str:
    safe = [
        {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]

    def get_docs(query: str) -> List[str]:
        query_embedding = generate_embeddings([query])[0]
        results = index.query(vector=query_embedding, top_k=top_k, include_metadata=True)
        return [x["metadata"]["content"] for x in results["matches"]]

    def generate_embeddings(texts: List[str]):
        embeddings = []
        for text in texts:
            result = genai.embed_content(
                model="models/text-embedding-004",
                content=text,
                task_type="retrieval_document",
                title="PDF Chunk Embedding"
            )
            embeddings.append(result['embedding'])
        return embeddings

    def generate_response(query: str, docs: List[str]) -> str:
        context = "\n---\n".join(docs)
        prompt = (
            "You are a helpful AI assistant. "
            "Answer the question using the provided context only.\n\n"
            "If you Do not Find any relavent answer just respond with the question i am asking is out of the Context provided\n\n"
            f"CONTEXT:\n{context}\n\n"
            f"Question: {query}"
        )
        response = model.generate_content(prompt, safety_settings=safe)
        return response.text

    retrieved_docs = get_docs(user_query)
    answer = generate_response(user_query, retrieved_docs)
    return answer

gemini_apis = [
    #GEMINI_API_KEY_1,
    #GEMINI_API_KEY_2,
    #GEMINI_API_KEY_3,
    #GEMINI_API_KEY_4,
    #..............
]
random.shuffle(gemini_apis)
together_apis = [
    #TOGETHER_API_KEY_1,
    #TOGETHER_API_KEY_2,
    #TOGETHER_API_KEY_3,
    #TOGETHER_API_KEY_4,
    #..............
]
random.shuffle(together_apis)

moa_report = {}
generation_config = {
    "temperature": 0.5,
    "top_p": 0.95,
    "top_k": 72,
    "max_output_tokens": 10000,
    "response_mime_type": "text/plain",
}

safe = [
    {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

def get_next_api_key(api_list):
    return api_list.pop(0)

def process_file(file, gemini_api, together_api, vulns_dict, whole_code):
    global gemini_apis, together_apis
    logger.info(f"Processing file: {file}")
    
    max_retries = 1
    for attempt in range(max_retries):
        try:
            genai.configure(api_key=gemini_api)
            model = genai.GenerativeModel('gemini-1.5-pro-exp-0827', tools=[query_gemini], generation_config=generation_config, safety_settings=safe)

            chat = model.start_chat(enable_automatic_function_calling=True)
            response = chat.send_message(
                f"what is {vulns_dict[file]} and give give me a detailed information about it and how to mitigate it, "
                f"the example code of it and the updated code how to mitigate it, make sure to give your explanation and "
                f"codes based on android apps mostly java and also the Information that is Directly relevent to the "
                f"Vulnerability mentioned only",
                safety_settings=safe
            )
            logger.info(f"Response received from Gemini for file {file}")
            log_to_txt(f"Response for {file}:\n{response.text}\n\n{'='*50}\n")
            
            code = whole_code[file]

            moa_result = moa_analysis(vulns_dict[file], response.text, code, together_api, gemini_api)
            logger.info(f"MOA Analysis completed for file {file}")
            log_to_txt(f"\nMOA Analysis Result for file {file}:\n{moa_result}\n\n{'='*50}\n")

            return file, moa_result

        except ResourceExhausted:
            logger.warning(f"API quota exhausted for key {gemini_api}. Rotating to next key.")
            if gemini_apis:
                gemini_api = get_next_api_key(gemini_apis)
                gemini_apis.append(gemini_api)  # Add the used key back to the end of the list
            else:
                logger.error("All Gemini API keys exhausted. Waiting for 60 seconds before retrying.")
                time.sleep(60)
                gemini_apis = gemini_apis_original.copy()  # Reset the API keys list
            
            if together_apis:
                together_api = get_next_api_key(together_apis)
                together_apis.append(together_api)  # Add the used key back to the end of the list
            else:
                logger.error("All Together API keys exhausted. Waiting for 60 seconds before retrying.")
                time.sleep(60)
                together_apis = together_apis_original.copy()  # Reset the API keys list

        except Exception as e:
            logger.error(f"Error processing file {file}: {str(e)}")
            if attempt == max_retries - 1:
                return file, f"Error: {str(e)}"

    return file, "Failed to process after multiple attempts"

def final_report_gemini():
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))  # Replace with your actual API key

    safe = [
        {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]

    generation_config = {
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 40,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-exp-0827",
        generation_config=generation_config,
        system_instruction="You are an expert cybersecurity analyst specializing in creating detailed, professional vulnerability assessment reports in Markdown format.",
        safety_settings=safe
    )

    moa_report_file = genai.upload_file(path=r"C:/Users/pandu/projects/LLMPatronous/Temp/temp_output.txt", display_name="MoA Report")
    whole_code_file = genai.upload_file(path=r"C:/Users/pandu/projects/LLMPatronous/Temp/combined_text_files.txt", display_name="Whole Code")
    template = genai.upload_file(path=r"C:/Users/pandu/projects/LLMPatronous/Final_Report.pdf", display_name="Template")
    \
    logger.info(f"Uploaded file '{moa_report_file.display_name}' as: {moa_report_file.uri}")
    logger.info(f"Uploaded file '{whole_code_file.display_name}' as: {whole_code_file.uri}")
    logger.info(f"Uploaded file '{template.display_name}' as: {template.uri}")
    report_request = {
        "role": "System",
        "content": """You are an expert cybersecurity consultant specializing in vulnerability assessment reports. 
        Your task is to professionally rewrite and enhance the provided report, ensuring it meets industry standards 
        and best practices and in-detail .

        I have a Vulnerability Assessment Report that needs to be rewritten and enhanced. Please follow these guidelines:
        
        1. Maintain the original structure but improve the formatting for better readability.
        2. Use professional, technical language appropriate for a cybersecurity audience.
        3. Expand on technical details where necessary, providing more in-depth explanations.
        4. Ensure all vulnerabilities are clearly described, including their potential impact and severity.
        5. Add or enhance recommendations for addressing each vulnerability.
        6. Include a brief executive summary at the beginning of the report.
        7. Add a section on methodology used for the assessment, if not already present.
        8. Incorporate any relevant industry standards or compliance requirements.
        9. Ensure proper use of cybersecurity terminology and acronyms.
        10. Add a conclusion section summarizing the overall security posture and key action items.
        11. Make sure to add the Code that is responsible for the vulnerability and code how to fix it also accordingly.
        12. Format the report using Markdown syntax for better readability when saved as a .md file.
        13. Remember that the text you return should be in MarkDown format only, because I am gonna save it in a .md file
        Here's the original report that needs to be enhanced:

        {moa_report_file}

        Here is the whole code that is responsible for the vulnerabilities and the code how to fix it:
        {whole_code_file}

        the template and exact format of the report is given below for your reference:
        {template}

        """,
    }

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = model.generate_content(report_request, safety_settings=safe)
            logger.info("Vulnerability assessment report generated successfully.")
            return response.text
        except InternalServerError:
            if attempt < max_retries - 1:
                logger.warning(f"Internal server error occurred. Retrying... (Attempt {attempt + 1}/{max_retries})")
                time.sleep(1)  # Wait for 5 seconds before retrying
            else:
                logger.error("Failed to generate vulnerability assessment report after multiple attempts.")
                return "Error: Failed to generate vulnerability assessment report."

def main():
    print_banner()
    
    logger.info("Initializing LLMPatronous...")
    
    global gemini_apis, together_apis
    gemini_apis_original = gemini_apis.copy()
    together_apis_original = together_apis.copy()

    logger.info("Setting up Pinecone...")
    pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
    index_name = "rag"   # pinecone index name

    existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

    if index_name not in existing_indexes:
        logger.info(f"Creating new Pinecone index: {index_name}")
        pc.create_index(
            index_name,
            dimension=768,
            metric='cosine',
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
        while not pc.describe_index(index_name).status['ready']:
            time.sleep(1)
    else:
        logger.info(f"Using existing Pinecone index: {index_name}")

    index = pc.Index(index_name)
    index.describe_index_stats()
    
    logger.info("Crawling files...")
    files_crawler()

    logger.info("Detecting vulnerabilities...")
    vulns_dict = vulns_detector()
    logger.info(f"Vulnerabilities detected: {len(vulns_dict)}")

    files = list(vulns_dict.keys())
    
    from Temp.files_content import whole_code

    logger.info("Starting file processing...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        while files:
            batch = files[:5]
            files = files[5:]

            futures = []
            for file in batch:
                gemini_api = get_next_api_key(gemini_apis)
                together_api = get_next_api_key(together_apis)
                futures.append(executor.submit(process_file, file, gemini_api, together_api, vulns_dict, whole_code))
                time.sleep(1)

            for future in concurrent.futures.as_completed(futures):
                file, result = future.result()
                moa_report[file] = result
                
                # Add the used keys back to the end of their respective lists
                gemini_apis.append(gemini_api)
                together_apis.append(together_api)

    logger.info("File processing completed.")
    
    for file, report in moa_report.items():
        logger.info(f"{file}: {report}")

    
    

    temp_dir = os.path.join('Temp')
    os.makedirs(temp_dir, exist_ok=True)

    logger.info("Saving Temp_output_report...")
    

    logger.info("Generating final vulnerability assessment report...")
    '''final_report_content = final_report()

    
    if not final_report_content.startswith("Error:"):
        with open('vulnerability_assessment_report.pdf', 'w') as f:
            f.write(final_report_content)
        logger.info("Vulnerability assessment report saved as: vulnerability_assessment_report.pdf")
    else:
        logger.error(final_report_content)

    logger.info("LLMPatronous execution completed successfully.")
    '''
    
    
    # also create a log file for the time taken to rewrite the report
    start_time = time.time()
    md_format_content= final_report_gemini()
    end_time = time.time()
    print(f"Time taken to rewrite the report: {end_time - start_time} seconds")
     # Ensure the Temp directory exists
    temp_dir = os.path.join('Temp')
    os.makedirs(temp_dir, exist_ok=True)
    
    # Save the content to Final_Report.md in the Temp directory
    final_report_path = os.path.join(temp_dir, "Final_Report.md")
    with open(final_report_path, "w", encoding="utf-8") as file:
        file.write(md_format_content)


if __name__ == "__main__":
    main()