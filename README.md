<p align="center">
  <img src="https://img.shields.io/badge/SAP-AI%20%26%20GenAI-0FAAFF?style=for-the-badge&logo=sap&logoColor=white" alt="SAP AI">
  <img src="https://img.shields.io/badge/MCP-Servers-blue?style=for-the-badge" alt="MCP Servers">
  <img src="https://img.shields.io/badge/RAG-Vector%20Engine-green?style=for-the-badge" alt="RAG">
  <img src="https://img.shields.io/badge/Agents-Agentic%20AI-orange?style=for-the-badge" alt="Agents">
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/vigneshbarani24/awesome-sap-ai?style=social" alt="GitHub Stars">
  <img src="https://img.shields.io/github/forks/vigneshbarani24/awesome-sap-ai?style=social" alt="GitHub Forks">
  <img src="https://img.shields.io/github/license/vigneshbarani24/awesome-sap-ai" alt="License">
</p>

<hr/>

# Awesome SAP AI

> A curated, community-driven directory of the best AI + SAP resources, tools, repos, MCP servers, skills, tutorials, and projects across the ecosystem. Your one-stop shop for everything AI in SAP.

<p align="center">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white" alt="OpenAI">
  <img src="https://img.shields.io/badge/Anthropic-191919?style=flat&logo=anthropic&logoColor=white" alt="Anthropic">
  <img src="https://img.shields.io/badge/Google%20Gemini-8E75B2?style=flat&logo=googlegemini&logoColor=white" alt="Google Gemini">
  <img src="https://img.shields.io/badge/Meta%20Llama-0467DF?style=flat&logo=meta&logoColor=white" alt="Meta Llama">
  <img src="https://img.shields.io/badge/Mistral-FF7000?style=flat&logo=mistral&logoColor=white" alt="Mistral">
</p>

---

## Why This Repo?

*   Dozens of amazing AI + SAP projects are scattered across GitHub, SAP Community, YouTube, and blogs. Finding them is hard. **This repo brings them all together.**

*   Building RAG pipelines on HANA Cloud? Wiring up MCP servers for vibe coding? Deploying agents with Joule Studio? Just trying to get started with AI on BTP? **Everything you need is here.**

*   This is **not** a code repo. No working projects inside. This is the **complete open-source directory** of AI in SAP — every tool, SDK, MCP server, tutorial, and community resource, organized and linked so you can find what you need fast.

---

## Table of Contents

- [Official SAP AI Tools & SDKs](#-official-sap-ai-tools--sdks)
- [MCP Servers for SAP](#-mcp-servers-for-sap)
- [AI Skills & Prompts for SAP](#-ai-skills--prompts-for-sap)
- [RAG & Knowledge Retrieval](#-rag--knowledge-retrieval)
- [AI Agents for SAP](#-ai-agents-for-sap)
- [SAP AI Use Cases by Category](#-sap-ai-use-cases-by-category)
- [ABAP + AI](#-abap--ai)
- [Tutorials & Crash Courses](#-tutorials--crash-courses)
- [SAP Community Content](#-sap-community-content)
- [People to Follow](#-people-to-follow)
- [Adjacent Tools](#-adjacent-tools)
- [Zero to Hero](#-zero-to-hero)
- [Contributing](#contributing)

---

## Official SAP AI Tools & SDKs

### SAP AI Core & Generative AI Hub

*   [SAP AI Core Documentation](https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/generative-ai-hub-in-sap-ai-core) — Central service for deploying and managing AI models on SAP BTP
*   [SAP AI Launchpad](https://help.sap.com/docs/ai-launchpad) — Cockpit for managing, monitoring, and orchestrating generative AI scenarios on BTP
*   [SAP Business AI](https://www.sap.com/products/technology-platform/ai.html) — SAP's enterprise AI platform overview and capabilities

### SAP Cloud SDK for AI

*   [SAP Cloud SDK for AI (JavaScript)](https://github.com/SAP/ai-sdk-js) — Official SDK for SAP AI Core, Generative AI Hub, and Orchestration Service in JS/TS
*   [SAP Cloud SDK for AI (Java)](https://github.com/SAP/ai-sdk-java) — Official SDK for integrating chat completion and AI capabilities into Java apps
*   [SAP Cloud SDK for AI Docs](https://sap.github.io/ai-sdk/) — Documentation portal covering both JS and Java SDKs with RAG and Business AI features

### CAP LLM Plugin & GenAI Toolkit

*   [SAP/cap-llm-plugin](https://github.com/SAP/cap-llm-plugin) — CAP plugin for building GenAI apps with HANA Cloud Vector Engine and AI Core integration
*   [Generative AI Toolkit for HANA Cloud](https://github.com/SAP/generative-ai-toolkit-for-sap-hana-cloud) — Extension of HANA ML Python client for GenAI use cases and HANA Vector Engine

### SAP Joule

*   [SAP Joule](https://www.sap.com/products/artificial-intelligence/ai-assistant.html) — SAP's AI copilot embedded across the SAP portfolio
*   [Joule for Developers](https://www.sap.com/products/artificial-intelligence/joule-for-developers.html) — SAP's AI copilot for developers across SAP Build and ABAP (free until Sept 2026)
*   [Joule Studio](https://help.sap.com/docs/joule) — No-code/low-code agent builder for creating custom AI agents on SAP BTP

---

## MCP Servers for SAP

### Official SAP MCP Servers

*   [SAP Fiori MCP Server](https://github.com/SAP/open-ux-tools/tree/main/packages/fiori-mcp-server) — Generate and adapt SAP Fiori elements applications with AI coding assistants
*   [CAP MCP Server](https://github.com/cap-js/mcp-server) — AI-assisted development of CAP applications with model introspection and docs search
*   [UI5 MCP Server](https://github.com/UI5/mcp-server) — Comprehensive UI5 knowledge for AI agents: app scaffolding, linting, API docs, and guidelines
*   [UI5 Web Components MCP Server](https://github.com/UI5/webcomponents-mcp-server) — AI-assisted development with UI5 Web Components across React, Angular, Vue, and vanilla JS
*   [MDK MCP Server](https://github.com/SAP/mdk-mcp-server) — AI-assisted development of cross-platform mobile apps with SAP Mobile Development Kit

### Community MCP Servers

*   [marianfoo/mcp-sap-docs](https://github.com/marianfoo/mcp-sap-docs) — Unified search across 50,000+ SAP docs (SAPUI5, CAP, ABAP, wdi5) with BM25 + semantic search
*   [marianfoo/mcp-sap-notes](https://github.com/marianfoo/mcp-sap-notes) — Search and retrieve SAP Notes/KB articles using SAP Passport authentication
*   [oisee/vibing-steampunk](https://github.com/oisee/vibing-steampunk) — ADT-to-MCP bridge for vibe coding in ABAP — read, write, debug, deploy, test via natural language
*   [lemaiwo/btp-sap-odata-to-mcp-server](https://github.com/lemaiwo/btp-sap-odata-to-mcp-server) — Expose SAP OData services as MCP tools on BTP Cloud Foundry
*   [lemaiwo/odata-mcp-proxy](https://www.npmjs.com/package/odata-mcp-proxy) — Config-driven framework that turns any OData V2/REST API into an MCP server — no code needed
*   [oisee/odata_mcp](https://github.com/oisee/odata_mcp) — Universal OData-to-MCP bridge turning 15,000+ enterprise services into MCP tools
*   [abap-ai/mcp](https://github.com/abap-ai/mcp) — ABAP MCP Server SDK for building MCP servers natively in ABAP
*   [akivaMishan/sap-mcp-server](https://github.com/akivaMishan/sap-mcp-server) — MCP server exposing SAP ABAP systems to AI via ADT REST API through Eclipse bridge
*   [gavdilabs/cap-mcp-plugin](https://github.com/gavdilabs/cap-mcp-plugin) — CAP plugin that auto-generates MCP servers from your CAP services using annotations
*   [mario-andreschak/mcp-abap-adt](https://github.com/mario-andreschak/mcp-abap-adt) — ABAP system interaction via ADT APIs — source code, table structures, and search
*   [mario-andreschak/mcp-sap-gui](https://github.com/mario-andreschak/mcp-sap-gui) — SAP GUI automation via coordinate input and screenshot capture
*   [kts982/mcp-sap-gui](https://github.com/kts982/mcp-sap-gui) — SAP GUI automation using the SAP Scripting API with 52 tools for Windows
*   [HatriGt/hana-mcp-server](https://github.com/HatriGt/hana-mcp-server) — Enterprise MCP server for SAP HANA / HANA Cloud — schema discovery and SQL execution
*   [vadimklimov/cpi-mcp-server](https://github.com/vadimklimov/cpi-mcp-server) — Access SAP Cloud Integration resources (packages, flows, mappings, scripts) via MCP
*   [oisee/odata_mcp_go](https://github.com/oisee/odata_mcp_go) — Go implementation of OData-to-MCP bridge with 97.6% token overhead reduction
*   [secondsky/mcp-sap-bdc](https://github.com/secondsky) — MCP server for SAP Business Data Cloud with Delta Sharing and data product tools
*   [MarioDeFelipe/sap-datasphere-plugin-for-claude](https://github.com/MarioDeFelipe/sap-datasphere-plugin-for-claude-cowork) — SAP Datasphere analytics operations via Claude
*   [AWS ABAP Accelerator for Amazon Q](https://github.com/aws-solutions-library-samples/guidance-for-deploying-sap-abap-accelerator-for-amazon-q-developer) — Enterprise MCP server for SAP ABAP development with Amazon Q Developer

---

## AI Skills & Prompts for SAP

*   [secondsky/sap-skills](https://github.com/secondsky/sap-skills) — 35 production-ready Claude Code skills covering BTP, CAP, Fiori, ABAP, HANA, Analytics Cloud, and more
*   [weiserman/rap-skills](https://github.com/weiserman/rap-skills) — Claude Code skills for SAP RAP development with branch-per-scenario for BTP, S/4HANA Cloud, and on-premise
*   [michal-majer/sap-cap-fiori-ai-agents](https://github.com/michal-majer/sap-cap-fiori-ai-agents) — AI agents for building enterprise SAP CAP and Fiori applications with guided end-to-end development

---

## RAG & Knowledge Retrieval

*   [SAP-samples/btp-cap-genai-rag](https://github.com/SAP-samples/btp-cap-genai-rag) — GenAI samples on BTP with LangChain in CAP, single/multitenant RAG, and LLM integration via AI Core
*   [SAP-samples/cap-ai-vector-engine-sample](https://github.com/SAP-samples/cap-ai-vector-engine-sample) — CAP app using CAP-LLM-Plugin for vector embeddings, similarity search, and RAG with HANA Cloud
*   [SAP-samples/btp-generative-ai-hub-use-cases](https://github.com/SAP-samples/btp-generative-ai-hub-use-cases) — Industry solutions with GenAI on BTP including Knowledge Graph Engine, Vector Engine, and self-hosted LLMs
*   [SAP-samples/sap-genai-hub-with-sap-hana-cloud-vector-engine](https://github.com/SAP-samples/sap-genai-hub-with-sap-hana-cloud-vector-engine) — Workshop content with Jupyter notebooks for RAG using HANA Cloud Vector Engine
*   [SAP-samples/btp-gen-ai-hub-sdk-samples](https://github.com/SAP-samples/btp-gen-ai-hub-sdk-samples) — Python/Jupyter samples for SAP BTP AI Core with Generative AI Hub SDK
*   [SAP-samples/btp-cap-genai-semantic-search](https://github.com/SAP-samples/btp-cap-genai-semantic-search) — Semantic search engine using CAP + GenAI Hub + HANA Cloud Vector Engine
*   [SAP-samples/cap-llm-plugin-samples](https://github.com/SAP-samples/cap-llm-plugin-samples) — CAP LLM Plugin samples with data anonymization and vector embeddings
*   [HANA Cloud Vector Engine Guide](https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-vector-engine-guide/sap-hana-cloud-sap-hana-database-vector-engine-guide) — Official documentation for SAP HANA Cloud Vector Engine

---

## AI Agents for SAP

*   [SAP-samples/btp-agentic-ai-use-cases](https://github.com/SAP-samples/btp-agentic-ai-use-cases) — Custom industry AI agents using Joule Studio (LCNC), Joule Studio Code Editor (low-code), and SAP Cloud SDK for AI (pro-code)
*   [SAP-samples/teched2025-AI160](https://github.com/SAP-samples/teched2025-AI160) — Hands-on: Build AI agent-based solutions with Generative AI Hub — PO Management Agent demo
*   [SAP-samples/teched2025-IN162](https://github.com/SAP-samples/teched2025-IN162) — Real-time data for AI agents: Grounding with event-driven architecture
*   [SAP-samples/sap-btp-ai-best-practices](https://github.com/SAP-samples/sap-btp-ai-best-practices) — AI paradigm implementations following best practices with code samples in TypeScript, Python, Java, and CAP
*   [michal-majer/sap-cap-fiori-ai-agents](https://github.com/michal-majer/sap-cap-fiori-ai-agents) — Multi-agent orchestrator for SAP CAP + Fiori application development
*   [SAP-samples/cloud-cap-vibe-with-cline](https://github.com/SAP-samples/cloud-cap-vibe-with-cline) — Vibe coding with Cline + SAP AI Core to build CAP apps with Fiori UI

---

## SAP AI Use Cases by Category

> 150+ real-world AI applications across the SAP ecosystem — organized by business domain.

### Procurement & Supply Chain

*   [Intelligent Procurement Assistant](https://github.com/SAP-samples/sap-btp-ai-best-practices) — AI-powered procurement assistant with contract analysis on BTP (use-cases directory)
*   [Touchless GR & Invoice Workflows](https://github.com/SAP-samples/sap-btp-ai-best-practices) — AI agent for touchless goods receipt and invoice processing
*   [Vendor Selection Optimization](https://github.com/SAP-samples/sap-btp-ai-best-practices) — AI-based vendor evaluation and selection optimization
*   [PO Management Agent (TechEd)](https://github.com/SAP-samples/teched2025-AI160) — Build an AI agent for purchase order management with LangGraph and Spring AI
*   [Real-Time PO Insights with GenAI](https://github.com/SAP-samples/real-time-business-insights-with-genai) — Dynamic GenAI app for real-time purchase order and maintenance order insights
*   [BTP Procurement Data Extractor](https://github.com/SAP-samples/btp-procurement-data-extractor) — Extract SAP Ariba data into BTP for procurement extensibility
*   [Custom Joule Agent for Ariba SLP](https://community.sap.com/t5/spend-management-blog-posts-by-sap/custom-joule-agent-for-sap-ariba-slp-building-an-ai-agent-for-supplier/ba-p/14368044) — AI agent for supplier registration approval in SAP Ariba
*   [Joule in SAP Ariba](https://community.sap.com/t5/spend-management-blog-posts-by-sap/joule-in-sap-ariba-applications/ba-p/14160181) — AI copilot for procurement navigation, supplier profiles, and approvals
*   [GenAI Supply Chain Planning Assistant](https://community.sap.com/t5/technology-blog-posts-by-sap/smarter-supply-chains-a-generative-ai-use-case-powered-by-the-sap-hana/ba-p/13868379) — Deloitte's GenAI assistant powered by HANA Cloud Vector Engine for supply chain exception management
*   [SAP Business AI for Procurement](https://www.sap.com/products/artificial-intelligence/procurement.html) — AI-powered sourcing, contract analysis, and supplier management
*   [AI in Supply Chain Management](https://www.sap.com/resources/ai-in-supply-chain-management) — SAP's guide to AI use cases in supply chain with real examples

### Finance & Accounting

*   [Invoice Validation with DOX + CAP](https://github.com/SAP-samples/btp-cap-dox-invoice-validation) — Invoice validation on BTP using Document Information Extraction with SAP CAP
*   [Customer Credit Check AI](https://github.com/SAP-samples/sap-btp-ai-best-practices) — AI-powered customer credit check use case on BTP
*   [Cash Flow & Payment Delay Prediction](https://github.com/SAP-samples/teched2025-DA266) — Operationalizing AI with SAP Databricks for cashflow prediction and payment delay analysis
*   [Invoice Object Recommendation](https://developers.sap.com/group.cp-aibus-dar-predict-invoice.html) — Use ML to predict G/L accounts and cost centers for incoming invoices
*   [Expense Anomaly Detection (RealSpend)](https://community.sap.com/t5/technology-blog-posts-by-sap/machine-learning-behind-the-scenes-of-sap-realspend-an-expense-anomaly/ba-p/13379924) — ML algorithm detecting wrong bookings and fraud in expense management
*   [AI-Powered Anomaly Insights in Integration Suite](https://community.sap.com/t5/integration-blog-posts/introducing-ai-powered-anomaly-insights-amp-recommendations-in-sap/ba-p/14286013) — AI anomaly detection and recommendations for API traffic
*   [Intelligent Invoice Processing](https://community.sap.com/t5/technology-blog-posts-by-sap/intelligent-finance-invoice-processing-with-sap-ai-business-services/ba-p/13515923) — End-to-end intelligent invoice processing with SAP AI Business Services
*   [Invoice Processing with Build Process Automation](https://developers.sap.com/mission.invoice-processing-approval-spa.html) — Mission: automate invoice processing and approval with Document Information Extraction
*   [SAP Business AI for Finance](https://www.sap.com/products/artificial-intelligence/finance.html) — AI-powered financial close, cash management, and treasury
*   [AI in S/4HANA Cloud Finance](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/artificial-intelligence-and-technologies-in-sap-s-4hana-cloud-public/ba-p/13596117) — AI technologies in S/4HANA Cloud Public Edition for financial insights and invoice matching

### HR & Workforce Intelligence

*   [Timesheet Tracking with GenAI](https://github.com/SAP-samples/btp-ai-core-simplifying-timesheet-tracking-task-in-s-4hana-cloud) — Full-stack CAP app using AI Core GenAI to simplify timesheet tracking in S/4HANA
*   [SuccessFactors Extension on BTP](https://github.com/SAP-samples/cloud-sf-extension-cap-sample) — Reference app extending SuccessFactors with CAP on BTP
*   [AI Payroll Anomaly Monitoring](https://community.sap.com/t5/human-capital-management-blog-posts-by-sap/ai-based-anomaly-monitoring-using-sap-payroll-control-center/ba-p/13965841) — ML algorithms detecting payroll discrepancies in SAP Payroll Control Center
*   [Talent Intelligence Hub](https://community.sap.com/t5/human-capital-management-blog-posts-by-sap/talent-intelligence-hub-2024-updates-and-behind-the-scenes/bc-p/13751269) — AI-powered skills inference, learning recommendations, and workforce planning
*   [AI for HR: Top Blogs 2026](https://community.sap.com/t5/human-capital-management-blog-posts-by-sap/ai-for-hr-top-blogs-2026/ba-p/14370281) — Curated collection of the best SAP AI for HR content
*   [SuccessFactors AI Roadmap](https://community.sap.com/t5/human-capital-management-blog-posts-by-members/sap-successfactors-ai-roadmap-key-takeaways-from-successconnect-2024/ba-p/13928945) — Key AI takeaways from SuccessConnect 2024
*   [SuccessFactors 2H 2025: AI & Skills](https://news.sap.com/2025/10/sap-successfactors-2h-2025-release-ai-skills-people-insights/) — AI-driven succession planning, skills-based recommendations, People Intelligence Agent
*   [Generative AI Solves Skills Gap](https://news.sap.com/2023/05/sap-successfactors-helps-hr-solve-skills-gap-with-generative-ai/) — How SuccessFactors uses GenAI to close the skills gap
*   [AI Learning & Talent Strategy](https://learning.sap.com/learning-journeys/configuring-sap-successfactors-platform-advanced-topics/sap-business-ai-capabilities-in-talent-intelligence-hub) — SAP Learning: Business AI capabilities in Talent Intelligence Hub

---

## ABAP + AI

### Benchmarks & Research

*   [marianfoo/LLM-Benchmark-ABAP-Code-Generation](https://github.com/marianfoo/LLM-Benchmark-ABAP-Code-Generation) — Benchmark comparing LLMs for ABAP code generation with live results at [abap-llm-benchmark.marianzeis.de](https://abap-llm-benchmark.marianzeis.de)
*   [timkoehne/LLM-Benchmark-ABAP-Code-Generation](https://github.com/timkoehne/LLM-Benchmark-ABAP-Code-Generation) — Original ABAP code generation benchmark from TH Koln with 180 tasks

### ABAP AI Libraries

*   [abap-ai/llm_client](https://github.com/abap-ai/llm_client) — Universal LLM client for ABAP supporting Ollama, OpenAI, Azure, Anthropic, Bedrock, and more
*   [abap-ai/mcp](https://github.com/abap-ai/mcp) — ABAP MCP Server SDK for building Model Context Protocol servers natively in ABAP
*   [oisee/zllm](https://github.com/oisee/zllm) — "LangChain-lite for ABAP" — LLM orchestration framework with lazy execution, caching, and token prediction

### Vibe Coding in ABAP

*   [oisee/vibing-steampunk](https://github.com/oisee/vibing-steampunk) — ADT-to-MCP bridge giving AI full access to SAP ADT APIs — vibe code in ABAP/AMDP anywhere ADT is available

### Hands-On & Tutorials

*   [SAP-samples/abap-platform-rap120](https://github.com/SAP-samples/abap-platform-rap120) — Hands-on: Build Fiori Apps with Joule — predictive code completion and unit test generation for ABAP
*   [ABAP AI 2026 Roadmap](https://community.sap.com/t5/technology-blog-posts-by-sap/our-2026-roadmap-for-joule-for-developers-abap-ai-capabilities/ba-p/14360358) — SAP's official 2026 roadmap for Joule, ABAP AI, and ABAP MCP server for VS Code

### Community Resources

*   [saptechbites/GenerativeAI-with-SAP-ABAP](https://saptechbites.github.io/GenerativeAI-with-SAP-ABAP/) — Generative AI use cases for SAP ABAP and Clean Core

---

## Tutorials & Crash Courses

### Official SAP CodeJams & Workshops

*   [SAP-samples/generative-ai-codejam](https://github.com/SAP-samples/generative-ai-codejam) — CodeJam covering Generative AI Hub, RAG implementation, embeddings, and the Python SDK on SAP AI Core
*   [SAP-samples/codejam-cap-llm](https://github.com/SAP-samples/codejam-cap-llm) — CodeJam for CAP + Generative AI Hub integration with hands-on exercises
*   [SAP-samples/btp-genai-starter-kit](https://github.com/SAP-samples/btp-genai-starter-kit) — Automated AI Core + HANA Vector Engine provisioning with Terraform to get started fast with GenAI on BTP
*   [SAP-samples/ui5con-2026-fiori-mcp-server](https://github.com/SAP-samples/ui5con-2026-fiori-mcp-server) — Hands-on: Create great UX with AI, SAP Fiori elements, and the MCP Server
*   [SAP-samples/ai-core-samples](https://github.com/SAP-samples/ai-core-samples) — Workflow templates and ML notebooks using SAP AI Core SDK
*   [SAP-samples/btp-ai-sustainability-bootcamp](https://github.com/SAP-samples/btp-ai-sustainability-bootcamp) — Computer vision, defect detection, and sound classification on BTP

### Free Online Courses

*   [Generative AI at SAP (openSAP)](https://open.sap.com/courses/genai1) — Free self-paced course covering AI approaches, generative AI, and SAP AI use cases (4.5 stars, 33K+ votes)
*   [Discovering SAP's Generative AI Hub (SAP Learning)](https://learning.sap.com/courses/discovering-sap-s-generative-ai-hub/exploring-the-generative-ai-hub) — Learn about the Generative AI Hub, LLM deployment, and prompt engineering
*   [SAP AI Learning Hub](https://learning.sap.com/artificial-intelligence) — Central hub for all SAP AI learning paths, certifications, and courses
*   [SAP Generative AI Developer Certification](https://learning.sap.com/certifications/sap-certified-associate-sap-generative-ai-developer) — Official certification for SAP Business AI capabilities and extending BTP apps with LLMs

### Community Tutorials

*   [SAP AI Certifications, Free Courses & Sample Projects (2025)](https://community.sap.com/t5/technology-blog-posts-by-sap/sap-ai-certifications-free-courses-sample-projects-and-many-more-2025/ba-p/13866605) — Comprehensive list of free courses, missions, and certifications for SAP AI

---

## SAP Community Content

### Key Blog Series

*   [ABAP AI: 2025 Set the Pace, 2026 Wins the Race](https://community.sap.com/t5/technology-blog-posts-by-sap/2025-set-the-pace-2026-wins-the-race-abap-ai-with-joule-vs-code-and-ccm/ba-p/14302433) — ABAP AI roadmap covering Joule, VS Code, Custom Code Migration, and agentic flows
*   [Evaluating SAP's New MCP Servers: UI5, CAP, and Fiori Tools](https://community.sap.com/t5/technology-blog-posts-by-members/evaluating-sap-s-new-mcp-servers-ui5-cap-and-fiori-tools-in-practice/ba-p/14205611) — Practical evaluation of SAP's official MCP servers
*   [Universal OData-to-MCP Bridge](https://community.sap.com/t5/technology-blog-posts-by-members/universal-odata-mcp-bridge-or-how-i-accidentally-made-15-000-enterprise/ba-p/14134696) — How one OData translator turned 15,000+ enterprise services into MCP tools
*   [Claude Code via MCP: Poor Man's Joule?](https://community.sap.com/t5/artificial-intelligence-blogs-posts/claude-code-via-mcp-poor-man-s-joule-or-a-practical-tool/ba-p/14344261) — Practical look at using Claude Code with SAP MCP servers
*   [Build Your Own SAP MCP Server with odata-mcp-proxy](https://community.sap.com/t5/technology-blog-posts-by-members/build-your-own-sap-mcp-server-in-minutes-with-odata-mcp-proxy/ba-p/14348685) — Step-by-step guide to building an SAP MCP server in minutes
*   [Try Vibing Steampunk to Generate ABAP](https://community.sap.com/t5/technology-blog-posts-by-members/try-vibing-steampunk-to-generate-abap-setting-up-vsp-with-a-cal-instance/ba-p/14341656) — Hands-on setup guide for ABAP vibe coding with Vibing Steampunk
*   [Agentic Coding with MCP: Extending CAP and Fiori](https://community.sap.com/t5/technology-blog-posts-by-sap/agentic-coding-with-mcp-extending-cap-and-fiori-applications/ba-p/14290686) — SAP official blog on using MCP servers for CAP and Fiori development
*   [ABAP MCP: Precise Answers from ABAP Keyword Documentation](https://community.sap.com/t5/technology-blog-posts-by-members/abap-mcp-precise-answers-from-abap-keyword-documentation-and-other-best/ba-p/14203228) — Using MCP for precise ABAP keyword docs access
*   [The SAP MCP Dilemma](https://www.itsfullofstars.de/2026/03/the-sap-mcp-dilemma/) — Critical analysis of the SAP MCP landscape and its challenges

### Podcasts

*   [ABAP AI Podcast: Reflecting on 2025 and Looking Ahead to 2026](https://community.sap.com/t5/technology-blog-posts-by-sap/abap-ai-podcast-reflecting-on-2025-and-looking-ahead-to-2026/ba-p/14322098) — The year ABAP AI stopped being a promise and became something developers could use

### YouTube

*   [SAP Developers](https://www.youtube.com/@sapdevs) — Official SAP Developers channel with AI, GenAI, and MCP content

---

## People to Follow

The builders, advocates, and thought leaders pushing AI + SAP forward. Follow them to stay on the cutting edge.

### Community Builders (Open Source)

| Who | GitHub | Known For |
|---|---|---|
| **Marian Zeis** | [marianfoo](https://github.com/marianfoo) | mcp-sap-docs, mcp-sap-notes, ABAP LLM Benchmarks, SAP AI MCP Servers list |
| **Alice Vinogradova** | [oisee](https://github.com/oisee) | Vibing Steampunk (ADT-to-MCP), Universal OData-to-MCP bridge, ZLLM |
| **Eddie** | [secondsky](https://github.com/secondsky) | 35 Claude Code skills for SAP, MCP servers for BDC and Analytics Cloud |
| **Warren** | [weiserman](https://github.com/weiserman) | RAP skills for Claude Code across BTP, S/4HANA Cloud, and on-premise |
| **Wouter Lemaire** | [lemaiwo](https://github.com/lemaiwo) | odata-mcp-proxy, BTP OData-to-MCP server |
| **Mario Andreschak** | [mario-andreschak](https://github.com/mario-andreschak) | mcp-abap-adt, mcp-sap-gui |
| **Michal Majer** | [michal-majer](https://github.com/michal-majer) | SAP CAP + Fiori multi-agent orchestrator |
| **Tobias Hofmann** | [tobiashofmann](https://github.com/tobiashofmann) | SAP Dev Tech Radar, "It's Full of Stars" blog, critical SAP MCP analysis |

### SAP Developer Advocates & Leaders

| Who | LinkedIn | Focus |
|---|---|---|
| **Thomas Jung** | [thomasjungsap](https://www.linkedin.com/in/thomasjungsap/) | Head of SAP Developer Advocacy, SAP Developers YouTube |
| **DJ Adams** | [djadams](https://www.linkedin.com/in/djadams/) | Developer Advocate, CAP, Hands-on SAP Dev streams ([qmacro.org](https://qmacro.org)) |
| **Antonio Maradiaga** | [ajmaradiaga](https://www.linkedin.com/in/ajmaradiaga/) | Developer Advocate, Integration Suite, AI CodeJams |
| **Rich Heilman** | [rich-heilman](https://www.linkedin.com/in/rich-heilman/) | Developer Advocate, ABAP Cloud, RAP |
| **Simona Marincei** | — | Head of AI - SAP ABAP Platform, driving Joule + ABAP AI strategy |
| **Alexander Rother** | — | VP & Head of ABAP Platform Product Management |

### Voices to Watch on SAP Community

| Who | Contribution |
|---|---|
| **Tobias Hofmann** | [The SAP MCP Dilemma](https://www.itsfullofstars.de/2026/03/the-sap-mcp-dilemma/) — honest, critical SAP AI analysis |
| **Marian Zeis** | [ABAP LLM Benchmark Blog](https://blog.zeis.de/posts/2026-02-09-abap-llm-benchmark/) — data-driven ABAP AI insights |
| **SAP Tech Bites** | [GenerativeAI-with-SAP-ABAP](https://saptechbites.github.io/GenerativeAI-with-SAP-ABAP/) — practical GenAI + ABAP patterns |

---

## Adjacent Tools

*   [Context7 (upstash/context7)](https://github.com/upstash/context7) — MCP server that fetches up-to-date, version-specific code documentation directly into your LLM's context
*   [DocsGPT (arc53/DocsGPT)](https://github.com/arc53/DocsGPT) — Private AI platform for agents, assistants, and enterprise search with RAG
*   [arabold/docs-mcp-server](https://github.com/arabold/docs-mcp-server) — Open-source MCP server for grounded documentation retrieval — alternative to Context7
*   [SAP's Official MCP Servers Directory](https://likweitan.github.io/sap-mcp-servers-official/) — Community-maintained visual directory of all official SAP MCP servers
*   [serpro69/claude-toolbox](https://github.com/serpro69/claude-starter-kit) — Collection of tools for Claude Code workflows: pre-configured MCP servers, skills, sub-agents, and hooks
*   [marcellourbani/vscode_abap_remote_fs](https://github.com/marcellourbani/vscode_abap_remote_fs) — VS Code extension for remote ABAP development — useful alongside AI coding tools

---

## Zero to Hero

New to AI in SAP? This is your roadmap. Follow these levels in order — each one builds on the last.

### Level 0: Prerequisites

Before you start, make sure you have:

| Requirement | How to Get It |
|---|---|
| **SAP BTP Account** | [Create a free trial account](https://developers.sap.com/tutorials/hcp-create-trial-account.html) or use your enterprise account |
| **AI Core Access** | Provision via BTP cockpit or automate with the [BTP GenAI Starter Kit](https://github.com/SAP-samples/btp-genai-starter-kit) |
| **IDE** | VS Code, Cursor, or any MCP-compatible editor |
| **AI Assistant** | Claude Code, GitHub Copilot, Cursor, Cline, or similar |
| **Basic SAP Knowledge** | Familiarity with BTP, CAP, or Fiori (any one is enough to start) |

### Level 1: Learn the Fundamentals

Understand what AI on SAP actually means — the platform, the tools, the terminology.

1. Take the free [Generative AI at SAP (openSAP)](https://open.sap.com/courses/genai1) course — 4.5 stars, 33K+ completions
2. Read about [SAP AI Core](https://help.sap.com/docs/sap-ai-core/sap-ai-core-service-guide/generative-ai-hub-in-sap-ai-core) and what the Generative AI Hub does
3. Explore [SAP AI Learning Hub](https://learning.sap.com/artificial-intelligence) for structured learning paths
4. Browse this repo top-to-bottom to see what's out there

### Level 2: Set Up Your AI Development Environment

Get your hands dirty. Provision services. Connect tools.

1. Use the [BTP GenAI Starter Kit](https://github.com/SAP-samples/btp-genai-starter-kit) to automate AI Core + HANA Vector Engine setup with Terraform
2. Install your first MCP servers — the trio that covers most SAP dev work:
   - [CAP MCP Server](https://github.com/cap-js/mcp-server) — `npx -y @cap-js/mcp-server`
   - [Fiori MCP Server](https://github.com/SAP/open-ux-tools/tree/main/packages/fiori-mcp-server) — `npx -y @sap-ux/fiori-mcp-server`
   - [UI5 MCP Server](https://github.com/UI5/mcp-server) — `npx -y @ui5/mcp-server`
3. Add [mcp-sap-docs](https://github.com/marianfoo/mcp-sap-docs) so your AI assistant can search 50,000+ SAP docs

### Level 3: Build Your First AI-Powered SAP App

Follow guided workshops. Get a working app running.

1. Complete the [Generative AI CodeJam](https://github.com/SAP-samples/generative-ai-codejam) — learn RAG, embeddings, and the Python SDK on AI Core
2. Try the [CAP + LLM CodeJam](https://github.com/SAP-samples/codejam-cap-llm) — integrate GenAI Hub into a CAP app
3. Build a [RAG app with HANA Cloud Vector Engine](https://github.com/SAP-samples/cap-ai-vector-engine-sample) — vector embeddings + similarity search

### Level 4: Supercharge Your Dev Workflow

Use AI skills and MCP servers to 10x your daily SAP development.

1. Install [SAP skills for Claude Code](https://github.com/secondsky/sap-skills) — 35 skills covering BTP, CAP, Fiori, ABAP, HANA, and more
2. Try [vibe coding with Cline](https://github.com/SAP-samples/cloud-cap-vibe-with-cline) — build CAP + Fiori apps conversationally
3. For ABAP developers: set up [Vibing Steampunk](https://github.com/oisee/vibing-steampunk) to vibe code in ABAP via ADT
4. Add [RAP skills](https://github.com/weiserman/rap-skills) if you work with SAP RAP Business Objects

### Level 5: Build AI Agents

Move from AI-assisted development to building AI agents that automate business processes.

1. Study the [BTP Agentic AI Use Cases](https://github.com/SAP-samples/btp-agentic-ai-use-cases) — real-world agent patterns using Joule Studio and SAP Cloud SDK for AI
2. Try the [TechEd AI160 Hands-On](https://github.com/SAP-samples/teched2025-AI160) — build a PO Management Agent with LangGraph or Spring AI
3. Learn the [SAP Cloud SDK for AI (JS)](https://github.com/SAP/ai-sdk-js) or [(Java)](https://github.com/SAP/ai-sdk-java) for pro-code agent development
4. Read [SAP BTP AI Best Practices](https://github.com/SAP-samples/sap-btp-ai-best-practices) for production patterns in TypeScript, Python, Java, and CAP

### Level 6: Go Pro

Get certified. Contribute back. Stay on the cutting edge.

1. Earn the [SAP Generative AI Developer Certification](https://learning.sap.com/certifications/sap-certified-associate-sap-generative-ai-developer)
2. Follow the [ABAP AI 2026 Roadmap](https://community.sap.com/t5/technology-blog-posts-by-sap/our-2026-roadmap-for-joule-for-developers-abap-ai-capabilities/ba-p/14360358) to stay ahead of what's coming
3. Build your own MCP server using the [ABAP MCP SDK](https://github.com/abap-ai/mcp) or [odata-mcp-proxy](https://www.npmjs.com/package/odata-mcp-proxy)
4. Contribute a resource to this repo — open a [PR](CONTRIBUTING.md) or [issue](https://github.com/vigneshbarani24/awesome-sap-ai/issues/new/choose)

---

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add resources to this directory.

---

<p align="center">
  If you found this useful, please <b>star this repo</b> and share it with the SAP community!
  <br><br>
  <a href="https://github.com/vigneshbarani24/awesome-sap-ai">
    <img src="https://img.shields.io/github/stars/vigneshbarani24/awesome-sap-ai?style=social" alt="Star this repo">
  </a>
</p>
