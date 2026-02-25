# 🧠 PDF Super Agent RAG

Multi-PDF Agentic Retrieval-Augmented Generation (RAG) system with chunk-level citations, hallucination detection, confidence scoring, and Dockerized deployment.

---

## 🚀 Overview

PDF Super Agent RAG is a production-ready, multi-document Question Answering system built using:

- FastAPI (Backend API)
- Streamlit (Frontend UI)
- ChromaDB (Vector Database)
- Sentence Transformers (Embeddings)
- Ollama (Llama3 – Local LLM)
- Docker (Containerized Deployment)

The system retrieves relevant chunks from multiple PDFs, generates grounded answers using a local LLM, and evaluates response quality using precision, coverage, and faithfulness metrics.

---

## 🏗 System Architecture

User → Streamlit UI → FastAPI → Super Agent → RAG Engine → ChromaDB → Ollama → Evaluation Engine → Structured Response

### Flow:

1. User submits question
2. Intent classification & validation
3. Top-K chunk retrieval (k=3)
4. Context injection into prompt
5. LLM generates grounded answer
6. Evaluation metrics computed
7. Structured response returned with:
   - Answer
   - Chunk-level citations
   - Precision, Coverage, Faithfulness
   - Confidence Score

---

## 🧩 Core Components

### 🔹 agent.py
Central orchestrator that:
- Handles intent detection
- Applies guardrails
- Calls RAG engine
- Calls evaluation engine
- Returns structured output

### 🔹 rag.py
- Embedding generation
- Vector retrieval (ChromaDB)
- Prompt construction
- LLM invocation (Ollama – llama3)

### 🔹 evaluation.py
Computes:
- Precision@K
- Context Coverage
- Faithfulness
- Confidence Score

Confidence formula:

confidence = 0.4*precision + 0.3*coverage + 0.3*faithfulness

### 🔹 intent.py
Classifies user queries:
- definition
- explanation
- unknown

### 🔹 validator.py
Validates input structure and domain compliance.

### 🔹 memory.py
Maintains session-level conversation memory.

---

## 🛡 Guardrails

- No retrieval → No answer
- If context not found → "I don't know."
- Strict grounding to retrieved chunks
- Faithfulness threshold enforcement
- Hallucination flagging

---

## 📊 Evaluation Metrics

| Metric        | Purpose |
|--------------|----------|
| Precision@K  | Measures relevance of retrieved chunks |
| Coverage     | % of answer grounded in retrieved context |
| Faithfulness | Detects hallucination likelihood |
| Confidence   | Weighted overall reliability score |

Example Output:

Precision@3: 1.0  
Coverage: 0.99  
Faithfulness: 0.98  
Confidence: 0.99  

---

## 📁 Project Structure


pdf-super-agent-rag/
│
├── app/
│ ├── agent.py
│ ├── rag.py
│ ├── evaluation.py
│ ├── api.py
│ ├── intent.py
│ ├── validator.py
│ ├── memory.py
│ └── config.py
│
├── ingestion/
│ └── ingest.py
│
├── chroma_db/
│
├── ui.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


---

## ⚙️ Configuration

Environment variables:

MODEL_NAME=llama3  
EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2  
DB_DIR=chroma_db  
TOP_K=3  
CONFIDENCE_THRESHOLD=0.6  

---

## ▶️ Local Setup

### 1️⃣ Install dependencies

pip install -r requirements.txt

### 2️⃣ Ingest PDFs

python -m ingestion.ingest

### 3️⃣ Start Backend

uvicorn app.api:app --reload

### 4️⃣ Run UI

streamlit run ui.py

---

## 🐳 Docker Setup

docker compose up --build

---

## 🧪 Run Tests

pytest -q

---

## 🔐 Security

- Fully local LLM (no external API dependency)
- No cloud vector DB
- Docker container isolation
- Environment variable configuration

---

## 🎯 Key Features

✔ Multi-PDF Retrieval  
✔ Chunk-Level Citations  
✔ Hallucination Detection  
✔ Confidence Scoring  
✔ Agent-Based Orchestration  
✔ Structured API Output  
✔ Evaluation Dashboard  
✔ Fully Dockerized  

---

## 💡 Interview Summary

"I designed and deployed a multi-PDF Agentic RAG system using FastAPI, ChromaDB, and a local LLM. The system includes chunk-level citations, hallucination detection, confidence scoring, and a structured evaluation dashboard. It is fully containerized and production-ready."

---

## 🏆 Why This Project Stands Out

Unlike basic RAG implementations, this system includes:

- Guardrails enforcement
- Evaluation metrics beyond retrieval
- Confidence scoring formula
- Structured JSON API response
- Agent-based orchestration
- Production-ready Docker deployment

---

## 📜 License

MIT License
