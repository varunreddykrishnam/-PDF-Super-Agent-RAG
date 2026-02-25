from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import run_agent

app = FastAPI(title="PDF Super Agent RAG")

class Question(BaseModel):
    question: str
    session_id: str = "default"

@app.post("/ask")
def ask(q: Question):
    return run_agent(q.question, q.session_id)
