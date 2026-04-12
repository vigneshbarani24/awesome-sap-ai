## 🗄️ SAP HANA RAG Agent

Retrieval-Augmented Generation using SAP HANA Cloud Vector Engine. Upload documents, chunk and embed them automatically, then ask questions and get grounded answers with source citations.

### Features

- Upload text documents and automatically chunk + embed via SAP GenAI Hub
- Store embeddings in HANA Cloud Vector Engine with cosine similarity search
- Ask natural language questions and get answers grounded in your documents
- View retrieved chunks with relevance scores
- Uses `text-embedding-ada-002` for embeddings, `gpt-4o` for generation

### How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/vigneshbarani24/awesome-sap-ai.git
   cd awesome-sap-ai/rag_sap_tutorials/sap_hana_rag
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
   ```

5. Run the app
   ```bash
   streamlit run sap_hana_rag.py
   ```

### Prerequisites

- SAP BTP account with AI Core provisioned (for embeddings + LLM)
- SAP HANA Cloud instance with Vector Engine enabled

### Tech Stack

- [Streamlit](https://streamlit.io/) — Web UI
- [SAP generative-ai-hub-sdk](https://pypi.org/project/generative-ai-hub-sdk/) — Embeddings + LLM via SAP AI Core
- [hdbcli](https://pypi.org/project/hdbcli/) — SAP HANA Cloud client
- [HANA Cloud Vector Engine](https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-vector-engine-guide/sap-hana-cloud-sap-hana-database-vector-engine-guide) — Vector storage + similarity search
