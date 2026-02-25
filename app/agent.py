from app.intent import classify_intent
from app.validator import validate_question
from app.memory import memory_store
from app.rag import retrieve_documents, generate_answer
from app.evaluation import (
    compute_precision_at_k,
    compute_context_coverage,
    compute_faithfulness,
    compute_confidence
)

def run_agent(question: str, session_id: str = "default"):

    if not validate_question(question):
        return {"error": "Invalid question."}

    intent = classify_intent(question)

    docs = retrieve_documents(question)
    answer, context_chunks = generate_answer(question, docs)

    sources = []
    for i, doc in enumerate(docs):
        sources.append({
            "id": i + 1,
            "source": doc.metadata.get("source"),
            "page": doc.metadata.get("page"),
            "chunk": doc.metadata.get("chunk_id")
        })

    precision = compute_precision_at_k(docs)
    coverage = compute_context_coverage(answer, context_chunks)
    faithfulness = compute_faithfulness(answer, context_chunks)
    confidence = compute_confidence(precision, coverage, faithfulness)

    memory_store.add(session_id, question, answer)

    return {
        "intent": intent,
        "answer": answer,
        "sources": sources,
        "metrics": {
            "precision_at_k": precision,
            "coverage": coverage,
            "faithfulness": faithfulness,
            "confidence": confidence
        }
    }
