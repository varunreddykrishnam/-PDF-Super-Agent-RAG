import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from app.config import DB_DIR

PDF_DIR = "data/pdfs"

print("Loading PDFs...")

documents = []
for file in os.listdir(PDF_DIR):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(PDF_DIR, file))
        docs = loader.load()
        for doc in docs:
            doc.metadata["source"] = file
        documents.extend(docs)

print("Splitting into chunks...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

chunks = text_splitter.split_documents(documents)

for i, chunk in enumerate(chunks):
    chunk.metadata["chunk_id"] = i

print("Creating embeddings...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Building Chroma DB...")

vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_DIR
)

print("✅ Vector DB built successfully.")
