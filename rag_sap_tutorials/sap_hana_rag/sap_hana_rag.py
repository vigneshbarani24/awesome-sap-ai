"""
🗄️ SAP HANA RAG Agent
Retrieval-Augmented Generation using SAP HANA Cloud Vector Engine.
Upload documents, embed them, and ask questions with grounded answers.
Built with Streamlit + SAP generative-ai-hub-sdk + hdbcli.
"""

import streamlit as st
from gen_ai_hub.proxy.native.openai import openai
from hdbcli import dbapi
import os
import hashlib

st.set_page_config(page_title="SAP HANA RAG", page_icon="🗄️")
st.title("🗄️ SAP HANA RAG Agent")
st.caption("Ask questions over your documents — grounded by HANA Cloud Vector Engine")

# --- HANA Connection ---
@st.cache_resource
def get_hana_connection():
    return dbapi.connect(
        address=os.environ["HANA_HOST"],
        port=int(os.environ.get("HANA_PORT", 443)),
        user=os.environ["HANA_USER"],
        password=os.environ["HANA_PASSWORD"],
        encrypt=True,
    )


def init_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS RAG_DOCUMENTS (
            ID NVARCHAR(64) PRIMARY KEY,
            CONTENT NCLOB,
            EMBEDDING REAL_VECTOR(1536),
            SOURCE NVARCHAR(256),
            CHUNK_INDEX INTEGER
        )
    """)
    conn.commit()


# --- Chunking ---
def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks


# --- Embedding ---
def get_embedding(text):
    response = openai.embeddings.create(
        model="text-embedding-ada-002",
        input=text,
    )
    return response.data[0].embedding


# --- Sidebar: Document Upload ---
with st.sidebar:
    st.header("📂 Upload Documents")
    uploaded_files = st.file_uploader(
        "Upload text files to index",
        type=["txt"],
        accept_multiple_files=True,
    )

    if uploaded_files and st.button("Index Documents", type="primary"):
        conn = get_hana_connection()
        init_table(conn)
        cursor = conn.cursor()
        progress = st.progress(0)
        total_chunks = 0

        for file in uploaded_files:
            text = file.read().decode("utf-8")
            chunks = chunk_text(text)

            for i, chunk in enumerate(chunks):
                doc_id = hashlib.sha256(f"{file.name}_{i}".encode()).hexdigest()[:64]
                embedding = get_embedding(chunk)
                vec_str = "[" + ",".join(str(v) for v in embedding) + "]"

                cursor.execute(
                    """UPSERT RAG_DOCUMENTS (ID, CONTENT, EMBEDDING, SOURCE, CHUNK_INDEX)
                       VALUES (?, ?, TO_REAL_VECTOR(?), ?, ?)""",
                    (doc_id, chunk, vec_str, file.name, i),
                )
                total_chunks += 1

            progress.progress(
                (uploaded_files.index(file) + 1) / len(uploaded_files)
            )

        conn.commit()
        st.success(f"Indexed {total_chunks} chunks from {len(uploaded_files)} files")

# --- Main: Question Answering ---
question = st.text_input(
    "Ask a question about your documents",
    placeholder="e.g., What are the key configuration steps for AI Core?",
)

if question and st.button("Search & Answer", type="primary"):
    with st.spinner("Searching HANA Vector Engine..."):
        conn = get_hana_connection()
        q_embedding = get_embedding(question)
        vec_str = "[" + ",".join(str(v) for v in q_embedding) + "]"

        cursor = conn.cursor()
        cursor.execute(
            """SELECT TOP 5 CONTENT, SOURCE, COSINE_SIMILARITY(EMBEDDING, TO_REAL_VECTOR(?)) AS SCORE
               FROM RAG_DOCUMENTS
               ORDER BY SCORE DESC""",
            (vec_str,),
        )
        results = cursor.fetchall()

    if not results:
        st.warning("No documents indexed yet. Upload files in the sidebar first.")
    else:
        context = "\n\n---\n\n".join(
            f"[Source: {row[1]}, Score: {row[2]:.3f}]\n{row[0]}" for row in results
        )

        with st.spinner("Generating answer..."):
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an SAP expert assistant. Answer the user's question based ONLY on the provided context. Cite the source file when possible. If the context doesn't contain the answer, say so.",
                    },
                    {
                        "role": "user",
                        "content": f"Context:\n{context}\n\nQuestion: {question}",
                    },
                ],
            )
            st.markdown("### Answer")
            st.write(response.choices[0].message.content)

        with st.expander("📎 Retrieved Chunks"):
            for row in results:
                st.markdown(f"**{row[1]}** (score: {row[2]:.3f})")
                st.text(row[0][:300])
                st.divider()
