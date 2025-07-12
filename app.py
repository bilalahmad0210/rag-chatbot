import streamlit as st
from src.pipeline import get_rag_response
from src.retriever import load_chunks  
st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title(" RAG Chatbot")

st.sidebar.title("Info Panel")
st.sidebar.markdown("Model in Use: Mistral-7B-Instruct (Q4_K_S.GGUF)")
st.sidebar.markdown("Vector DB: FAISS")
st.sidebar.markdown("Embeddings: MiniLM-L6-v2")

chunks = load_chunks()
st.sidebar.markdown(f"** Indexed Chunks:** {len(chunks)}")

if st.sidebar.button(" Reset"):
    st.session_state.pop("user_query", None)
    st.session_state.pop("answer", None)
    st.session_state.pop("context_chunks", None)
    st.rerun()

user_query = st.text_input("Ask a question based on the training document:")

if user_query:
    with st.spinner("Generating answer..."):
        answer, context_chunks = get_rag_response(user_query)
        st.session_state.user_query = user_query
        st.session_state.answer = answer
        st.session_state.context_chunks = context_chunks

if "answer" in st.session_state:
    st.markdown(f"**Question:** {st.session_state.user_query}")
    st.markdown(f"**Answer:** {st.session_state.answer}")
    st.markdown("**Context Used:**")
    for i, ch in enumerate(st.session_state.context_chunks):
        st.markdown(f"**Chunk {i+1}:** {ch[:300]}...")
