"""
🔌 SAP MCP Development Agent
AI development assistant that uses SAP MCP servers (CAP, Fiori, UI5) to help you build SAP apps.
Connects to multiple MCP servers and routes your questions to the right one.
Built with Streamlit + SAP generative-ai-hub-sdk + MCP client.
"""

import streamlit as st
from gen_ai_hub.proxy.native.openai import openai
import json

st.set_page_config(page_title="SAP MCP Dev Agent", page_icon="🔌", layout="wide")
st.title("🔌 SAP MCP Development Agent")
st.caption("AI assistant powered by SAP MCP servers — ask about CAP, Fiori, or UI5 development")

# --- MCP Server Registry ---
MCP_SERVERS = {
    "CAP": {
        "description": "SAP Cloud Application Programming Model — data models, services, CDS, Node.js/Java runtime",
        "package": "@cap-js/mcp-server",
        "topics": ["CDS", "entities", "services", "projections", "annotations", "handlers", "Node.js", "Java", "OData", "REST"],
    },
    "Fiori": {
        "description": "SAP Fiori elements — UI generation, adaptation, OPA tests, manifest.json, annotations",
        "package": "@sap-ux/fiori-mcp-server",
        "topics": ["Fiori elements", "List Report", "Object Page", "annotations", "manifest.json", "OPA5", "adaptation"],
    },
    "UI5": {
        "description": "SAPUI5 and OpenUI5 — controls, views, controllers, routing, i18n, custom apps",
        "package": "@niclas.krohne/ui5-mcp-server",
        "topics": ["SAPUI5", "OpenUI5", "controls", "XML views", "controllers", "routing", "models", "binding", "fragments"],
    },
}

with st.sidebar:
    st.header("🔌 Connected MCP Servers")
    for name, info in MCP_SERVERS.items():
        with st.expander(f"{name} MCP"):
            st.write(info["description"])
            st.code(info["package"], language="text")
            st.write("**Topics:**", ", ".join(info["topics"]))

    st.divider()
    st.markdown("""
    **Setup:** Install these MCP servers in your IDE:
    ```json
    {
      "mcpServers": {
        "cap": { "command": "npx", "args": ["-y", "@cap-js/mcp-server"] },
        "fiori": { "command": "npx", "args": ["-y", "@sap-ux/fiori-mcp-server"] },
        "ui5": { "command": "npx", "args": ["-y", "@niclas.krohne/ui5-mcp-server"] }
      }
    }
    ```
    """)

# --- Router Prompt ---
ROUTER_PROMPT = f"""You are an SAP development expert with access to knowledge from three SAP MCP servers:

1. **CAP MCP Server**: {MCP_SERVERS["CAP"]["description"]}
   Topics: {", ".join(MCP_SERVERS["CAP"]["topics"])}

2. **Fiori MCP Server**: {MCP_SERVERS["Fiori"]["description"]}
   Topics: {", ".join(MCP_SERVERS["Fiori"]["topics"])}

3. **UI5 MCP Server**: {MCP_SERVERS["UI5"]["description"]}
   Topics: {", ".join(MCP_SERVERS["UI5"]["topics"])}

When answering:
- Identify which MCP server(s) are relevant and tag your response with [CAP], [Fiori], or [UI5]
- Provide concrete code examples using the correct SAP frameworks
- Include file paths where code should be placed (e.g., srv/cat-service.cds, webapp/view/Main.view.xml)
- Reference official SAP documentation when possible
- If a question spans multiple servers, structure your answer by server"""

# --- Chat Interface ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Example questions
if not st.session_state.messages:
    st.markdown("**Try asking:**")
    examples = [
        "How do I create a CDS entity with associations and expose it as OData?",
        "Generate a Fiori elements List Report for a products service",
        "How do I add a custom action button in a SAPUI5 controller?",
        "Build a full-stack CAP app with a Fiori UI showing a list of employees",
    ]
    for ex in examples:
        st.caption(f"• {ex}")

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask about CAP, Fiori, or UI5 development..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Consulting MCP servers..."):
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": ROUTER_PROMPT},
                    *st.session_state.messages,
                ],
            )
            reply = response.choices[0].message.content
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
