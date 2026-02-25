import os
import streamlit as st
import requests

API_URL = os.getenv("API_URL", "http://api:8000")

st.title("📘 PDF Super Agent RAG")
st.caption("Multi-PDF • Chunk Citations • Evaluation Dashboard")

question = st.text_input("Ask a question from the PDFs")

if st.button("Ask") and question:
    try:
        res = requests.post(
            f"{API_URL}/ask",
            json={"question": question},
            timeout=300
        ).json()

        st.subheader("Answer")
        st.write(res["answer"])

        st.subheader("Sources")
        for src in res["sources"]:
            st.write(f"[{src['id']}] {src['source']} — page {src['page']} — chunk {src['chunk']}")

        st.subheader("📊 Evaluation Metrics")
        metrics = res["metrics"]

        st.metric("Precision@3", metrics["precision_at_k"])
        st.metric("Coverage", metrics["coverage"])
        st.metric("Faithfulness", metrics["faithfulness"])
        st.metric("Confidence", metrics["confidence"])

    except Exception as e:
        st.error(f"API Error: {e}")
