
# 🤖 RAG Chatbot — Amlgo Labs Assignment

This project is a Retrieval-Augmented Generation (RAG) chatbot based on local vector search and a quantized LLM. It enables fast, offline answering of questions based on uploaded documents, using FAISS for retrieval and Mistral-7B-Instruct in GGUF format for local inference.

---

## 🔹 Key Features

- **📄 Context-Aware Retrieval**: Uses FAISS + MiniLM embeddings to fetch top relevant document chunks.
- **🧠 Local Model Inference**: Runs `Mistral-7B-Instruct.Q4_K_S.gguf` using `ctransformers` with no GPU or internet required.
- **🖼️ Streamlit Interface**: Simple input form, context display, and reset capability.
- **📑 Source Context View**: Shows which document chunks were used for the answer.
- **💡 Token-Safe Prompting**: Ensures model input stays within context length to avoid token overflow.

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/bilalahmad0210/rag-chatbot.git
cd rag-chatbot
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv env
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 📥 Download the Model (Required)

1. Visit: https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF
2. Download: `mistral-7b-instruct-v0.1.Q4_K_S.gguf`
3. Place it in the `model/` folder like so:

```
rag-chatbot/
└── model/
    └── mistral-7b-instruct-v0.1.Q4_K_S.gguf
```

---

## ▶️ Run the App

Start the chatbot locally:

```bash
streamlit run app.py
```

Open your browser to: [http://localhost:8501](http://localhost:8501)

---

## 📄 Project Structure

```
rag-chatbot/
├── app.py                # Streamlit front-end
├── src/
│   ├── pipeline.py       # Orchestrates retrieval and generation
│   ├── retriever.py      # Uses FAISS + MiniLM for vector search
│   └── generator.py      # Loads quantized model and generates response
├── vectordb/             # FAISS index + metadata (not uploaded to GitHub)
├── model/                # Place your GGUF model here (not uploaded)
├── requirements.txt
└── README.md
```

---

## 🧠 Example Questions

Ask questions like:

- What services does eBay offer?
- What is the role of the arbitrator?
- Can users follow AI-generated suggestions?
- Is eBay a broker or vehicle dealer?

---

## ❌ .gitignore Highlights

The following are ignored:

- `model/` folder
- `vectordb/` folder
- `env/` (virtual environment)
- `__pycache__/`, `.pyc`, `.DS_Store`, etc.

---

## 📜 License

MIT — feel free to modify and use this project.

---

## ✍️ Author

Built by Bilal Ahmad for the Amlgo Labs RAG challenge.
