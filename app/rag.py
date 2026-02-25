from langchain_chroma import Chroma
from langchain_community.llms import Ollama
from app.config import DB_DIR, OLLAMA_BASE_URL, MODEL_NAME, TOP_K

vectordb = Chroma(persist_directory=DB_DIR)

llm = Ollama(
    model=MODEL_NAME,
    base_url=OLLAMA_BASE_URL,
    temperature=0.2
)

def retrieve_documents(question: str):
    retriever = vectordb.as_retriever(search_kwargs={"k": TOP_K})
    return retriever.invoke(question)

def generate_answer(question: str, docs):
    context_chunks = [doc.page_content for doc in docs]
    context_text = "\n\n".join(context_chunks)

    prompt = f"""
Use ONLY the context below.
If answer not found, say "I don't know."

Context:
{context_text}

Question:
{question}
"""

    answer = llm.invoke(prompt)
    return answer, context_chunks
from langchain_chroma import Chroma
from langchain_community.llms import Ollama
from app.config import DB_DIR, OLLAMA_BASE_URL, MODEL_NAME, TOP_K

vectordb = Chroma(persist_directory=DB_DIR)

llm = Ollama(
    model=MODEL_NAME,
    base_url=OLLAMA_BASE_URL,
    temperature=0.2
)

def retrieve_documents(question: str):
    retriever = vectordb.as_retriever(search_kwargs={"k": TOP_K})
    return retriever.invoke(question)

def generate_answer(question: str, docs):
    context_chunks = [doc.page_content for doc in docs]
    context_text = "\n\n".join(context_chunks)

    prompt = f"""
Use ONLY the context below.
If answer not found, say "I don't know."

Context:
{context_text}

Question:
{question}
"""

    answer = llm.invoke(prompt)
    return answer, context_chunks
