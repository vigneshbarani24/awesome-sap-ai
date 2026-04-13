"""
🎫 SAP Support Agent Team
Multi-agent system for SAP support ticket triage, resolution, and escalation.
Three specialized agents collaborate to handle incoming tickets.
Built with Streamlit + SAP generative-ai-hub-sdk.
"""

import streamlit as st
from gen_ai_hub.proxy.native.openai import openai
import json

st.set_page_config(page_title="SAP Support Agent Team", page_icon="🎫", layout="wide")
st.title("🎫 SAP Support Agent Team")
st.caption("Three AI agents collaborate to classify, resolve, and escalate SAP support tickets")


# --- Agent Definitions ---
CLASSIFIER_PROMPT = """You are an SAP support ticket classifier. Analyze the ticket and return JSON:
{
    "module": "one of: FI, CO, MM, SD, PP, HR, BASIS, SECURITY, FIORI, HANA, BTP, OTHER",
    "severity": "one of: LOW, MEDIUM, HIGH, CRITICAL",
    "category": "one of: Configuration, Authorization, Performance, Data Issue, Integration, Bug, How-To",
    "summary": "one-line summary of the issue",
    "needs_escalation": true/false (true if CRITICAL or requires system access)
}
Respond ONLY with valid JSON."""

RESOLVER_PROMPT = """You are a senior SAP support engineer. Given a classified support ticket, provide a structured resolution:

1. **Root Cause Analysis** - What's likely causing this issue
2. **Resolution Steps** - Numbered steps to fix it, including transaction codes (e.g., SM37, SU01, SE38) and specific paths
3. **Preventive Measures** - How to prevent recurrence
4. **Related SAP Notes** - Suggest relevant SAP Note numbers if applicable

Be specific with SAP terminology, transaction codes, and configuration paths. Reference tables (e.g., BSEG, EKPO, VBAK) when relevant."""

ESCALATION_PROMPT = """You are an SAP escalation manager. Given a critical ticket, write a concise escalation brief:

1. **Impact Assessment** - Business impact and affected users/processes
2. **Urgency Justification** - Why this needs immediate attention
3. **Recommended Team** - Which SAP support team should handle this (Basis, Security, Functional, Development)
4. **Temporary Workaround** - Any interim solution while the issue is being resolved
5. **SLA Recommendation** - Suggested response/resolution time

Keep it professional and actionable for the receiving team."""


def run_agent(system_prompt, user_message):
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
    )
    return response.choices[0].message.content


# --- Sample Tickets ---
SAMPLE_TICKETS = {
    "Authorization Error": "User JSMITH in company code 1000 gets error 'No authorization for transaction ME21N' when trying to create purchase orders. They were recently transferred from the finance department and their role was changed. Other users in the same role can access ME21N without issues.",
    "HANA Performance": "CRITICAL: Production HANA database response time degraded from 200ms to 15 seconds over the past 2 hours. Multiple users reporting timeouts in S/4HANA Fiori apps. SAP EWM warehouse operations are impacted - outbound deliveries cannot be processed. Memory utilization shows 94% on the primary HANA node.",
    "Fiori App Error": "Sales team cannot open the 'Manage Sales Orders' Fiori app (F0842A) after yesterday's transport. Error message: 'Service /sap/opu/odata/sap/SD_SO_MNG is not available'. The app was working before transport request DEVK900123 was imported into QAS.",
    "Data Reconciliation": "Month-end close blocked: GL account balance in FI (transaction FS10N) for account 140000 shows $2.3M, but the corresponding subledger in AP (FK10N vendor balance) shows $2.1M. Difference of $200K appeared after the last payment run on April 10.",
}

with st.sidebar:
    st.header("Sample Tickets")
    selected = st.radio("Load a sample:", list(SAMPLE_TICKETS.keys()))
    if st.button("Load Sample"):
        st.session_state["ticket_text"] = SAMPLE_TICKETS[selected]

ticket = st.text_area(
    "Paste a support ticket",
    value=st.session_state.get("ticket_text", ""),
    height=150,
    placeholder="Describe the SAP issue...",
)

if st.button("Process Ticket", type="primary") and ticket:
    col1, col2 = st.columns(2)

    # Agent 1: Classifier
    with col1:
        st.markdown("### 🏷️ Agent 1: Classifier")
        with st.spinner("Classifying..."):
            classification_raw = run_agent(CLASSIFIER_PROMPT, ticket)
            try:
                classification = json.loads(classification_raw)
                st.json(classification)
                needs_escalation = classification.get("needs_escalation", False)
                severity = classification.get("severity", "MEDIUM")
            except json.JSONDecodeError:
                st.code(classification_raw)
                needs_escalation = False
                severity = "MEDIUM"

    # Agent 2: Resolver
    with col2:
        st.markdown("### 🔧 Agent 2: Resolver")
        with st.spinner("Resolving..."):
            resolver_input = f"Ticket: {ticket}\n\nClassification: {classification_raw}"
            resolution = run_agent(RESOLVER_PROMPT, resolver_input)
            st.markdown(resolution)

    # Agent 3: Escalation (conditional)
    if needs_escalation or severity == "CRITICAL":
        st.divider()
        st.markdown("### 🚨 Agent 3: Escalation Manager")
        with st.spinner("Preparing escalation brief..."):
            escalation_input = f"Ticket: {ticket}\n\nClassification: {classification_raw}"
            escalation = run_agent(ESCALATION_PROMPT, escalation_input)
            st.error("This ticket has been flagged for escalation")
            st.markdown(escalation)
    else:
        st.divider()
        st.success("Ticket resolved - no escalation needed")
