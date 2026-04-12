## 🔍 SAP OData Natural Language Agent

Describe what you need in plain English and get valid OData V2 queries for SAP S/4HANA. Supports Purchase Orders, Sales Orders, Business Partners, and Products APIs out of the box.

### Features

- Natural language to OData V2 query conversion
- Covers 4 core SAP S/4HANA APIs (Purchase Orders, Sales Orders, Business Partners, Products)
- Generates properly formatted $filter, $top, $orderby, $select, and $expand parameters
- Example queries to get started quickly
- Sidebar showing all available services and fields

### How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/vigneshbarani24/awesome-sap-ai.git
   cd awesome-sap-ai/starter_sap_ai_agents/sap_odata_nl_agent
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
   streamlit run sap_odata_nl_agent.py
   ```

### Adding More SAP Services

Add any OData service to `ODATA_SERVICES` in the script:

```python
ODATA_SERVICES["Cost Centers"] = {
    "endpoint": "/sap/opu/odata/sap/API_COSTCENTER_SRV/A_CostCenter",
    "fields": ["CostCenter", "CostCenterName", "CompanyCode", "ProfitCenter"],
}
```

### Tech Stack

- [Streamlit](https://streamlit.io/) — Web UI
- [SAP generative-ai-hub-sdk](https://pypi.org/project/generative-ai-hub-sdk/) — LLM access via SAP AI Core
