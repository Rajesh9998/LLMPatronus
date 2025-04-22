import PyPDF2

file_path = r"C:\Users\pandu\projects\LLMPatronous\Temp\temp_output.pdf"
import fitz
doc = fitz.open(file_path)
text = ""
for page in doc:
   text+=page.get_text()
print(text)
