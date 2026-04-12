## 📊 SAP Data Analyst Agent

Ask questions about your SAP data in plain English. The agent generates HANA SQL, executes it, and visualizes the results — all through a chat-like interface.

### Features

- Natural language to SAP HANA SQL conversion
- Auto-discovers your HANA schema (tables and columns) in the sidebar
- Safety-first: only generates and runs SELECT statements
- Auto-visualizes numeric results as bar charts
- Example queries to get started

### How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/vigneshbarani24/awesome-sap-ai.git
   cd awesome-sap-ai/advanced_sap_ai_agents/sap_data_analyst_agent
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

4. Set your HANA Cloud credentials
   ```bash
   export HANA_HOST=your-hana-host.hanacloud.ondemand.com
   export HANA_PORT=443
   export HANA_USER=your-user
   export HANA_PASSWORD=your-password
   export HANA_SCHEMA=YOUR_SCHEMA
   ```

5. Run the app
   ```bash
   streamlit run sap_data_analyst_agent.py
   ```

### Tech Stack

- [Streamlit](https://streamlit.io/) — Web UI
- [SAP generative-ai-hub-sdk](https://pypi.org/project/generative-ai-hub-sdk/) — LLM access via SAP AI Core
- [hdbcli](https://pypi.org/project/hdbcli/) — SAP HANA Cloud client
- [Pandas](https://pandas.pydata.org/) — Data manipulation and display
