## 🎫 SAP Support Agent Team

Three AI agents collaborate to handle SAP support tickets: a Classifier triages the ticket, a Resolver provides step-by-step fixes with transaction codes, and an Escalation Manager writes escalation briefs for critical issues.

### Features

- **Agent 1 - Classifier**: Identifies SAP module, severity, category, and escalation need
- **Agent 2 - Resolver**: Provides root cause analysis, resolution steps with transaction codes, and preventive measures
- **Agent 3 - Escalation Manager**: Activates on CRITICAL tickets with impact assessment and SLA recommendations
- 4 built-in sample tickets (authorization, HANA performance, Fiori app error, data reconciliation)
- Multi-agent pipeline with conditional escalation logic

### How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/vigneshbarani24/awesome-sap-ai.git
   cd awesome-sap-ai/advanced_sap_ai_agents/sap_support_agent_team
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
   streamlit run sap_support_agent_team.py
   ```

### Tech Stack

- [Streamlit](https://streamlit.io/) - Web UI
- [SAP generative-ai-hub-sdk](https://pypi.org/project/generative-ai-hub-sdk/) - LLM access via SAP AI Core
