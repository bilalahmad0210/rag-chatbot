from src.retriever import retrieve_top_k
from src.generator import generate_answer

def get_rag_response(user_query, top_k=1):
    chunks = retrieve_top_k(user_query, k=top_k)
    answer = generate_answer(chunks, user_query)
    return answer, chunks
