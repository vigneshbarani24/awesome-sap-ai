"""
🛒 SAP Purchase Order Chatbot
Chat with your purchase order data using natural language.
Built with Streamlit + SAP generative-ai-hub-sdk.
"""

import streamlit as st
from gen_ai_hub.proxy.native.openai import openai
import json

st.set_page_config(page_title="SAP PO Chatbot", page_icon="🛒")
st.title("🛒 SAP Purchase Order Chatbot")
st.caption("Chat with your SAP purchase order data using natural language")

# Sample PO data — in production, replace with OData call to SAP S/4HANA
# e.g., GET /sap/opu/odata/sap/API_PURCHASEORDER_PROCESS_SRV/A_PurchaseOrder
SAMPLE_PO_DATA = [
    {
        "PurchaseOrder": "4500001234",
        "Vendor": "Acme Corp",
        "Material": "Raw Steel",
        "Quantity": 500,
        "Unit": "KG",
        "NetAmount": 12500.00,
        "Currency": "USD",
        "Status": "Approved",
        "DeliveryDate": "2026-05-15",
    },
    {
        "PurchaseOrder": "4500001235",
        "Vendor": "TechParts GmbH",
        "Material": "Circuit Board A1",
        "Quantity": 1000,
        "Unit": "EA",
        "NetAmount": 45000.00,
        "Currency": "EUR",
        "Status": "Pending",
        "DeliveryDate": "2026-04-28",
    },
    {
        "PurchaseOrder": "4500001236",
        "Vendor": "Global Logistics",
        "Material": "Packaging Material",
        "Quantity": 2000,
        "Unit": "EA",
        "NetAmount": 3200.00,
        "Currency": "USD",
        "Status": "Delivered",
        "DeliveryDate": "2026-04-10",
    },
    {
        "PurchaseOrder": "4500001237",
        "Vendor": "Acme Corp",
        "Material": "Aluminum Sheets",
        "Quantity": 300,
        "Unit": "KG",
        "NetAmount": 9600.00,
        "Currency": "USD",
        "Status": "Approved",
        "DeliveryDate": "2026-06-01",
    },
    {
        "PurchaseOrder": "4500001238",
        "Vendor": "ChemSupply Ltd",
        "Material": "Industrial Solvent",
        "Quantity": 100,
        "Unit": "L",
        "NetAmount": 1800.00,
        "Currency": "GBP",
        "Status": "Cancelled",
        "DeliveryDate": "2026-05-20",
    },
]

with st.sidebar:
    st.header("📋 PO Data")
    st.dataframe(SAMPLE_PO_DATA, use_container_width=True)
    st.caption("Sample data — replace with live OData in production")

SYSTEM_PROMPT = f"""You are an SAP procurement assistant. Answer questions about purchase orders based on this data:

{json.dumps(SAMPLE_PO_DATA, indent=2)}

Be concise and helpful. Format numbers and currencies properly.
When asked to analyze, provide insights about spending patterns, vendor distribution, and status summaries.
If the user asks something outside the PO data scope, let them know politely."""

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask about purchase orders..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    *st.session_state.messages,
                ],
            )
            reply = response.choices[0].message.content
            st.write(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
