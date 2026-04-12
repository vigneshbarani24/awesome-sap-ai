"""
📄 SAP Document Summarizer
Summarize SAP documents using GenAI Hub on SAP BTP.
Built with Streamlit + SAP generative-ai-hub-sdk.
"""

import streamlit as st
from gen_ai_hub.proxy.native.openai import openai
import PyPDF2
import io

st.set_page_config(page_title="SAP Document Summarizer", page_icon="📄")
st.title("📄 SAP Document Summarizer")
st.caption("Upload any SAP document and get an AI-powered summary via SAP GenAI Hub")

model = st.selectbox(
    "Select Model (deployed on SAP AI Core)",
    ["gpt-4o", "gpt-4", "gpt-35-turbo", "gemini-1.5-pro"],
)

summary_style = st.radio(
    "Summary style",
    ["Executive Brief", "Technical Detail", "Action Items Only"],
    horizontal=True,
)

STYLE_PROMPTS = {
    "Executive Brief": "Provide a concise executive summary highlighting business impact, key decisions, and next steps. Keep it under 200 words.",
    "Technical Detail": "Provide a detailed technical summary covering architecture, configurations, dependencies, and implementation details relevant to SAP systems.",
    "Action Items Only": "Extract only the action items, tasks, deadlines, and responsible parties. Format as a numbered checklist.",
}

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt"])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
        text = "\n".join(
            page.extract_text() for page in reader.pages if page.extract_text()
        )
    else:
        text = uploaded_file.read().decode("utf-8")

    st.info(f"Extracted {len(text):,} characters from document")

    with st.expander("Preview extracted text"):
        st.text(text[:2000] + ("..." if len(text) > 2000 else ""))

    if st.button("Summarize", type="primary"):
        with st.spinner("Summarizing via SAP GenAI Hub..."):
            response = openai.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": f"You are an SAP domain expert. {STYLE_PROMPTS[summary_style]}",
                    },
                    {
                        "role": "user",
                        "content": f"Summarize this document:\n\n{text[:15000]}",
                    },
                ],
            )
            st.markdown("### Summary")
            st.write(response.choices[0].message.content)
