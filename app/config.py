import os

DB_DIR = "chroma_db"

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

MODEL_NAME = "llama3"
TOP_K = 3
