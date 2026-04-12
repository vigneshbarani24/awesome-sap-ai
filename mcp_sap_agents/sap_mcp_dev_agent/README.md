## 🔌 SAP MCP Development Agent

AI development assistant that combines knowledge from SAP's CAP, Fiori, and UI5 MCP servers. Ask questions about SAP development and get context-aware answers with code examples, file paths, and best practices.

### Features

- Routes questions across CAP, Fiori, and UI5 knowledge domains
- Generates concrete code examples with correct file paths
- Conversational memory for follow-up questions
- Sidebar shows all connected MCP servers and their topics
- Includes MCP server configuration snippet for your IDE

### How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/vigneshbarani24/awesome-sap-ai.git
   cd awesome-sap-ai/mcp_sap_agents/sap_mcp_dev_agent
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Set your SAP AI Core credentials
   ```bash
   export AICORE_AUTH_URL=https://your-auth-url.authentication.sap.hana.ondemand.com
   export AICORE_CLIENT_ID=your-client-id
   export AICORE_CLIENT_SECRET=your-client-secret
   export AICORE_BASE_URL=https://api.ai.your-region.aws.ml.hana.ondemand.com
   export AICORE_RESOURCE_GROUP=default
   ```

4. Run the app
   ```bash
   streamlit run sap_mcp_dev_agent.py
   ```

### Companion MCP Servers

For the full experience, install these MCP servers in your IDE (VS Code, Cursor, etc.):

```json
{
  "mcpServers": {
    "cap": { "command": "npx", "args": ["-y", "@cap-js/mcp-server"] },
    "fiori": { "command": "npx", "args": ["-y", "@sap-ux/fiori-mcp-server"] },
    "ui5": { "command": "npx", "args": ["-y", "@niclas.krohne/ui5-mcp-server"] }
  }
}
```

### Tech Stack

- [Streamlit](https://streamlit.io/) — Chat UI
- [SAP generative-ai-hub-sdk](https://pypi.org/project/generative-ai-hub-sdk/) — LLM access via SAP AI Core
- [CAP MCP Server](https://github.com/cap-js/mcp-server) — CAP knowledge
- [Fiori MCP Server](https://github.com/SAP/open-ux-tools/tree/main/packages/fiori-mcp-server) — Fiori elements knowledge
- [UI5 MCP Server](https://github.com/UI5/mcp-server) — UI5 knowledge
