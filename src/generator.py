from ctransformers import AutoModelForCausalLM
import re

model = AutoModelForCausalLM.from_pretrained(
    "TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
    model_file="D:\\RAG_Chatbot\\model\\mistral-7b-instruct-v0.1.Q4_K_S.gguf",
    model_type="mistral",  
    max_new_tokens=300,
    temperature=0.7, 
    repetition_penalty=1.1  
)


def truncate_context(context, max_words=380):
    sentences = re.split(r'(?<=[.!?]) +', context)
    result = []
    word_count = 0
    for sentence in sentences:
        words_in_sentence = len(sentence.split())
        if word_count + words_in_sentence > max_words:
            break
        result.append(sentence)
        word_count += words_in_sentence
    return ' '.join(result)

def build_prompt(context_chunks, query, max_words=380):
    raw_context = "\n\n".join(context_chunks)
    safe_context = truncate_context(raw_context, max_words=max_words)
    
    return f"""### Instruction:
You are a helpful assistant. Use the following context to answer the user's question clearly and concisely. If the answer is directly stated or can be logically inferred from the context, provide the best possible answer. If not, reply: "The answer is not available in the provided document."

### Context:
{safe_context}

### Question:
{query}

### Answer:"""

def generate_answer(context_chunks, user_query):
    prompt = build_prompt(context_chunks, user_query)
    return model(prompt).strip()
