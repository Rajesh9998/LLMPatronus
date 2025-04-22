from openai import OpenAI
import PyPDF2
import time
from dotenv import load_dotenv
import os
load_dotenv()

token = os.getenv("GITHUB_TOKEN")
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)


def final_report(final_report_content):
    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": """You are an expert cybersecurity consultant specializing in vulnerability assessment reports. Your task is to professionally rewrite and enhance the provided report, ensuring it meets industry standards and best practices.

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
11. Make sure to add the Code that is responsible for the vulnerability and code how to fix it also accordingly
12. Format the report using Markdown syntax for better readability when saved as a .md file.

Here's the original report that needs to be enhanced:

"""
            },
            {
                "role": "user",
                "content": final_report_content
            },
            {
                "role": "user",
                "content": "Please provide the rewritten and enhanced version of this Vulnerability Assessment Report in Markdown format."
            }
        ],
        stream=False,
    )
    
    enhanced_report = completion.choices[0].message.content
    
    # Save the enhanced report as a Markdown file
    with open("Temp/Final_Report.md", "w", encoding="utf-8") as md_file:
        md_file.write(enhanced_report)

    print("******Final Report saved as Final_Report.md******")


file_path = r"C:\Users\pandu\projects\LLMPatronous\Temp\temp_output.pdf"
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text() + '\n'
    return text

# Extract text from the PDF file
pdf_text = extract_text_from_pdf(file_path)

# Call the final_report function with the extracted text
print('OpenAI -o1 is re-writing the Final Report')
final_report(pdf_text)