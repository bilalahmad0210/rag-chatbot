from PyPDF2 import PdfReader
import os

reader = PdfReader("D:\RAG_Chatbot\data\AI Training Document.pdf")
full_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        full_text += text + "\n"

full_text = full_text.replace("  ", " ").replace("\n\n", "\n").strip()

with open("data/training_doc.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print("Text extracted to data/training_doc.txt")
