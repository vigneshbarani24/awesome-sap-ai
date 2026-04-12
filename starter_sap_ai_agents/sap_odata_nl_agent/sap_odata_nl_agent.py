"""
🔍 SAP OData Natural Language Agent
Convert natural language queries to OData requests for SAP S/4HANA.
Built with Streamlit + SAP generative-ai-hub-sdk.
"""

import streamlit as st
from gen_ai_hub.proxy.native.openai import openai
import json

st.set_page_config(page_title="SAP OData NL Agent", page_icon="🔍")
st.title("🔍 SAP OData Natural Language Agent")
st.caption("Describe what you need in plain English — get OData queries for SAP")

ODATA_SERVICES = {
    "Purchase Orders": {
        "endpoint": "/sap/opu/odata/sap/API_PURCHASEORDER_PROCESS_SRV/A_PurchaseOrder",
        "fields": [
            "PurchaseOrder",
            "PurchaseOrderType",
            "Supplier",
            "CompanyCode",
            "PurchasingOrganization",
            "CreationDate",
            "PurchaseOrderDate",
        ],
    },
    "Sales Orders": {
        "endpoint": "/sap/opu/odata/sap/API_SALES_ORDER_SRV/A_SalesOrder",
        "fields": [
            "SalesOrder",
            "SalesOrderType",
            "SoldToParty",
            "CreationDate",
            "TotalNetAmount",
            "TransactionCurrency",
        ],
    },
    "Business Partners": {
        "endpoint": "/sap/opu/odata/sap/API_BUSINESS_PARTNER/A_BusinessPartner",
        "fields": [
            "BusinessPartner",
            "BusinessPartnerName",
            "BusinessPartnerCategory",
            "Industry",
            "Country",
            "Region",
        ],
    },
    "Products": {
        "endpoint": "/sap/opu/odata/sap/API_PRODUCT_SRV/A_Product",
        "fields": [
            "Product",
            "ProductType",
            "ProductGroup",
            "BaseUnit",
            "GrossWeight",
            "WeightUnit",
        ],
    },
}

with st.sidebar:
    st.header("Available SAP Services")
    for service, details in ODATA_SERVICES.items():
        with st.expander(service):
            st.code(details["endpoint"], language="text")
            st.write("**Fields:**", ", ".join(details["fields"]))

st.markdown("**Try these examples:**")
cols = st.columns(3)
examples = [
    "Get top 10 purchase orders from supplier 1000 created after January 2026",
    "Find all business partners in Germany in the automotive industry",
    "Show sales orders over $50,000 sorted by amount descending",
]
for col, example in zip(cols, examples):
    col.caption(example)

query = st.text_area(
    "Describe your query in plain English",
    placeholder="e.g., Get the top 10 purchase orders from supplier 1000 created after January 2026, sorted by date",
)

SYSTEM_PROMPT = f"""You are an SAP OData V2 expert. Convert natural language queries into valid OData URL queries for SAP S/4HANA.

Available services:
{json.dumps(ODATA_SERVICES, indent=2)}

Rules:
- Use OData V2 syntax: eq, ne, gt, lt, ge, le, and, or, not
- Dates use format: datetime'2026-01-01T00:00:00'
- String values are quoted with single quotes: 'value'
- Supported query options: $filter, $top, $skip, $orderby, $select, $expand, $count
- Return the full URL path with query parameters

Respond ONLY with valid JSON (no markdown fences):
{{"odata_url": "the full OData URL with query params", "explanation": "plain English description of what this query does", "service": "which service this uses"}}"""

if st.button("Generate OData Query", type="primary") and query:
    with st.spinner("Generating OData query..."):
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": query},
            ],
        )

        result = response.choices[0].message.content
        st.markdown("### Generated OData Query")

        try:
            parsed = json.loads(result)
            st.code(parsed["odata_url"], language="text")
            st.success(parsed["explanation"])
            st.caption(f"Service: {parsed['service']}")
        except (json.JSONDecodeError, KeyError):
            st.code(result, language="text")
