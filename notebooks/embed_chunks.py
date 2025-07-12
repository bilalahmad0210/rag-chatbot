import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

model = SentenceTransformer('all-MiniLM-L6-v2')

chunk_dir = "chunks"
chunks = []
filenames = sorted(os.listdir(chunk_dir))

for fname in tqdm(filenames):
    with open(os.path.join(chunk_dir, fname), "r", encoding="utf-8") as f:
        chunks.append(f.read())

embeddings = model.encode(chunks, show_progress_bar=True)

# Save FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

os.makedirs("vectordb", exist_ok=True)
faiss.write_index(index, "vectordb/index.faiss")

# Save metadata
with open("vectordb/chunks.pkl", "wb") as f:
    pickle.dump({"chunks": chunks, "filenames": filenames}, f)

print("FAISS index and metadata saved.")
