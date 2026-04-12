## 🛒 SAP Purchase Order Chatbot

Chat with your SAP purchase order data using natural language. Ask questions like "Which vendor has the highest spend?" or "Show me all pending orders" and get instant answers.

### Features

- Natural language chat interface for SAP purchase order data
- Spending analysis, vendor breakdowns, and status summaries
- Conversational memory — ask follow-up questions naturally
- Powered by SAP AI Core via the generative-ai-hub-sdk
- Sidebar with live data preview

### How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/vigneshbarani24/awesome-sap-ai.git
   cd awesome-sap-ai/starter_sap_ai_agents/sap_purchase_order_chatbot
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
   streamlit run sap_purchase_order_chatbot.py
   ```

### Connecting to Live SAP Data

Replace `SAMPLE_PO_DATA` with a real OData call:

```python
import requests

response = requests.get(
    "https://your-sap-system/sap/opu/odata/sap/API_PURCHASEORDER_PROCESS_SRV/A_PurchaseOrder",
    params={"$top": 50, "$format": "json"},
    auth=("user", "password"),
)
po_data = response.json()["d"]["results"]
```

### Tech Stack

- [Streamlit](https://streamlit.io/) — Chat UI
- [SAP generative-ai-hub-sdk](https://pypi.org/project/generative-ai-hub-sdk/) — LLM access via SAP AI Core
