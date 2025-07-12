import nltk
from nltk.tokenize import sent_tokenize
import os

nltk.download('punkt')

with open("data/training_doc.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

cleaned_text = raw_text.replace("\n", " ").replace("  ", " ")
sentences = sent_tokenize(cleaned_text)

chunks = []
current_chunk = ""
current_length = 0

for sentence in sentences:
    if current_length + len(sentence.split()) <= 250:
        current_chunk += " " + sentence
        current_length += len(sentence.split())
    else:
        chunks.append(current_chunk.strip())
        current_chunk = sentence
        current_length = len(sentence.split())

if current_chunk:
    chunks.append(current_chunk.strip())

os.makedirs("chunks", exist_ok=True)

for i, ch in enumerate(chunks):
    with open(f"chunks/chunk_{i}.txt", "w", encoding="utf-8") as f:
        f.write(ch)

print(f"{len(chunks)} chunks created.")
