## 📄 SAP Document Summarizer

Upload any SAP document (PDF or text) and get an AI-powered summary using SAP GenAI Hub. Choose between executive briefs, technical details, or action item extraction.

### Features

- Upload PDF or text files and extract content automatically
- Three summary styles: Executive Brief, Technical Detail, Action Items Only
- Powered by SAP AI Core via the generative-ai-hub-sdk
- Choose your model: GPT-4o, GPT-4, GPT-3.5, or Gemini 1.5 Pro

### How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/vigneshbarani24/awesome-sap-ai.git
   cd awesome-sap-ai/starter_sap_ai_agents/sap_document_summarizer
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
   streamlit run sap_document_summarizer.py
   ```

### Tech Stack

- [Streamlit](https://streamlit.io/) — Web UI
- [SAP generative-ai-hub-sdk](https://pypi.org/project/generative-ai-hub-sdk/) — LLM access via SAP AI Core
- [PyPDF2](https://pypi.org/project/PyPDF2/) — PDF text extraction
