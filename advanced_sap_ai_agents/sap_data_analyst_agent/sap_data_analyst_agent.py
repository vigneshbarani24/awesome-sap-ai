"""
📊 SAP Data Analyst Agent
Ask questions about your SAP data in plain English — generates SQL, runs it on HANA, and visualizes results.
Built with Streamlit + SAP generative-ai-hub-sdk + hdbcli.
"""

import streamlit as st
from gen_ai_hub.proxy.native.openai import openai
from hdbcli import dbapi
import pandas as pd
import os
import json

st.set_page_config(page_title="SAP Data Analyst", page_icon="📊", layout="wide")
st.title("📊 SAP Data Analyst Agent")
st.caption("Ask questions about your SAP data in natural language — get SQL, results, and insights")


@st.cache_resource
def get_hana_connection():
    return dbapi.connect(
        address=os.environ["HANA_HOST"],
        port=int(os.environ.get("HANA_PORT", 443)),
        user=os.environ["HANA_USER"],
        password=os.environ["HANA_PASSWORD"],
        encrypt=True,
    )


@st.cache_data(ttl=300)
def get_schema_info(_conn, schema):
    cursor = _conn.cursor()
    cursor.execute(
        """SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE_NAME
           FROM TABLE_COLUMNS
           WHERE SCHEMA_NAME = ?
           ORDER BY TABLE_NAME, POSITION""",
        (schema,),
    )
    rows = cursor.fetchall()
    tables = {}
    for table, column, dtype in rows:
        tables.setdefault(table, []).append(f"{column} ({dtype})")
    return tables


SYSTEM_PROMPT = """You are an SAP HANA SQL expert. Given a natural language question and database schema, generate a SELECT query.

Rules:
- Generate ONLY read-only SELECT statements — never INSERT, UPDATE, DELETE, DROP, or ALTER
- Use SAP HANA SQL syntax (e.g., TOP instead of LIMIT for row limiting)
- Use column aliases for readability
- Include ORDER BY for sorted results
- Use aggregations (SUM, COUNT, AVG) when the question implies summaries

Respond with JSON:
{"sql": "the SELECT query", "explanation": "what this query does in plain English"}"""

# --- Sidebar: Schema Browser ---
with st.sidebar:
    st.header("Database Schema")
    schema = st.text_input("HANA Schema", value=os.environ.get("HANA_SCHEMA", ""))

    if schema:
        try:
            conn = get_hana_connection()
            tables = get_schema_info(conn, schema)
            st.caption(f"{len(tables)} tables found")
            for table, columns in list(tables.items())[:20]:
                with st.expander(table):
                    for col in columns:
                        st.text(col)
        except Exception as e:
            st.error(f"Connection error: {e}")
            tables = {}
    else:
        tables = {}
        st.info("Enter a schema name to browse tables")

# --- Main: Natural Language Query ---
st.markdown("**Try asking:**")
examples = [
    "Show total sales by customer for the last quarter",
    "Which purchase orders are overdue?",
    "Top 10 materials by quantity ordered",
]
cols = st.columns(3)
for col, ex in zip(cols, examples):
    col.caption(ex)

question = st.text_input(
    "Ask a question about your data",
    placeholder="e.g., What are the top 10 customers by revenue?",
)

if question and st.button("Analyze", type="primary") and schema:
    schema_context = "\n".join(
        f"Table: {t}\n  Columns: {', '.join(cs[:15])}"
        for t, cs in list(tables.items())[:30]
    )

    with st.spinner("Generating SQL..."):
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": f"Schema ({schema}):\n{schema_context}\n\nQuestion: {question}",
                },
            ],
        )
        result = response.choices[0].message.content

    try:
        parsed = json.loads(result)
        sql = parsed["sql"]
        explanation = parsed.get("explanation", "")
    except (json.JSONDecodeError, KeyError):
        sql = result
        explanation = ""

    st.markdown("### Generated SQL")
    st.code(sql, language="sql")
    if explanation:
        st.info(explanation)

    # Safety check
    sql_upper = sql.strip().upper()
    if not sql_upper.startswith("SELECT"):
        st.error("Safety check: Only SELECT statements are allowed.")
    else:
        if st.button("Run Query"):
            try:
                conn = get_hana_connection()
                df = pd.read_sql(sql, conn)
                st.markdown("### Results")
                st.dataframe(df, use_container_width=True)

                if len(df.columns) >= 2 and df.dtypes.iloc[-1] in ["int64", "float64"]:
                    st.markdown("### Visualization")
                    st.bar_chart(df.set_index(df.columns[0]))
            except Exception as e:
                st.error(f"Query error: {e}")
