import faiss
import pickle
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("vectordb/index.faiss")

with open("vectordb/chunks.pkl", "rb") as f:
    metadata = pickle.load(f)

chunks = metadata["chunks"]

def retrieve_top_k(query, k=3):
    query_vector = embedding_model.encode([query])
    distances, indices = index.search(query_vector, k)
    return [chunks[i] for i in indices[0]]

def load_chunks():
    return chunks