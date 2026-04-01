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

*   There are dozens of amazing AI + SAP projects scattered across GitHub, SAP Community, YouTube, and blogs. Finding them is hard. **This repo brings them all together.**

*   Whether you're building RAG pipelines on HANA Cloud, wiring up MCP servers for vibe coding, deploying agents with Joule Studio, or just trying to get started with AI on BTP — you'll find the best resources here.

*   This is **not** a code repo. There are no working projects inside. This is a **curated index** of what exists out there, with links to external repos, tools, and resources.

---

## How This Repo Differs from Other Lists

| | **Awesome SAP AI** (this repo) | **[marianfoo/sap-ai-mcp-servers](https://github.com/marianfoo/sap-ai-mcp-servers)** |
|---|---|---|
| **Scope** | Full landscape of AI in SAP | MCP servers + AI dev skills |
| **Coverage** | MCP, RAG, agents, voice, SDKs, tutorials, community, ABAP+AI, learning paths | MCP servers, AI skills, adjacent tools |
| **Format** | Curated directory with descriptions | Data-rich tables with stars & license info |
| **Goal** | One-stop-shop for anyone getting started | Deep-dive reference for MCP ecosystem |

> Marian's list is excellent for MCP servers and AI dev skills. We go broader: the **full landscape** of AI in SAP. Use both!

---

## Table of Contents

- [Official SAP AI Tools & SDKs](#-official-sap-ai-tools--sdks)
- [MCP Servers for SAP](#-mcp-servers-for-sap)
- [AI Skills & Prompts for SAP](#-ai-skills--prompts-for-sap)
- [RAG & Knowledge Retrieval](#-rag--knowledge-retrieval)
- [AI Agents for SAP](#-ai-agents-for-sap)
- [ABAP + AI](#-abap--ai)
- [Tutorials & Crash Courses](#-tutorials--crash-courses)
- [SAP Community Content](#-sap-community-content)
- [Adjacent Tools](#-adjacent-tools)
- [Learning Path](#-learning-path)
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

> For the most comprehensive and up-to-date list of SAP MCP servers, see [marianfoo/sap-ai-mcp-servers](https://github.com/marianfoo/sap-ai-mcp-servers)

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

### Notable Authors & Contributors

*   **Marian Zeis** ([marianfoo](https://github.com/marianfoo)) — SAP MCP server ecosystem, ABAP LLM benchmarks, mcp-sap-docs
*   **Eddie** ([secondsky](https://github.com/secondsky)) — 35 Claude Code skills for SAP, MCP servers for SAP BDC and Analytics Cloud
*   **Alice Vinogradova** ([oisee](https://github.com/oisee)) — Vibing Steampunk (ADT-to-MCP), Universal OData-to-MCP bridge
*   **Warren** ([weiserman](https://github.com/weiserman)) — RAP skills for Claude Code across BTP, S/4HANA Cloud, and on-premise
*   **Wouter Lemaire** ([lemaiwo](https://github.com/lemaiwo)) — OData MCP proxy, BTP OData-to-MCP server

---

## Adjacent Tools

*   [Context7 (upstash/context7)](https://github.com/upstash/context7) — MCP server that fetches up-to-date, version-specific code documentation directly into your LLM's context
*   [DocsGPT (arc53/DocsGPT)](https://github.com/arc53/DocsGPT) — Private AI platform for agents, assistants, and enterprise search with RAG
*   [arabold/docs-mcp-server](https://github.com/arabold/docs-mcp-server) — Open-source MCP server for grounded documentation retrieval — alternative to Context7
*   [SAP's Official MCP Servers Directory](https://likweitan.github.io/sap-mcp-servers-official/) — Community-maintained visual directory of all official SAP MCP servers
*   [serpro69/claude-toolbox](https://github.com/serpro69/claude-starter-kit) — Collection of tools for Claude Code workflows: pre-configured MCP servers, skills, sub-agents, and hooks
*   [marcellourbani/vscode_abap_remote_fs](https://github.com/marcellourbani/vscode_abap_remote_fs) — VS Code extension for remote ABAP development — useful alongside AI coding tools

---

## Learning Path

### Where Do I Start?

If you're new to AI in SAP, here's a recommended path:

**Step 1: Understand the Basics**
1. Take the free [Generative AI at SAP (openSAP)](https://open.sap.com/courses/genai1) course
2. Explore the [SAP AI Learning Hub](https://learning.sap.com/artificial-intelligence) for structured paths

**Step 2: Set Up Your Environment**
1. Get a [SAP BTP Trial Account](https://developers.sap.com/tutorials/hcp-create-trial-account.html)
2. Provision AI Core using the [BTP GenAI Starter Kit](https://github.com/SAP-samples/btp-genai-starter-kit)
3. Install MCP servers: start with [CAP MCP](https://github.com/cap-js/mcp-server) + [Fiori MCP](https://github.com/SAP/open-ux-tools/tree/main/packages/fiori-mcp-server) + [UI5 MCP](https://github.com/UI5/mcp-server)

**Step 3: Build Something**
1. Follow the [Generative AI CodeJam](https://github.com/SAP-samples/generative-ai-codejam) for hands-on RAG
2. Try [CAP + LLM CodeJam](https://github.com/SAP-samples/codejam-cap-llm) for CAP integration
3. Explore [RAG with HANA Cloud Vector Engine](https://github.com/SAP-samples/cap-ai-vector-engine-sample)

**Step 4: Go Deeper**
1. Build custom agents with [Joule Studio](https://help.sap.com/docs/joule) or [SAP Cloud SDK for AI](https://github.com/SAP/ai-sdk-js)
2. Install [SAP skills for Claude Code](https://github.com/secondsky/sap-skills) to supercharge your dev workflow
3. Explore [agentic AI use cases](https://github.com/SAP-samples/btp-agentic-ai-use-cases) for real-world patterns

### Prerequisites

| Requirement | Details |
|---|---|
| **SAP BTP Account** | Trial or enterprise — needed for AI Core, HANA Cloud |
| **AI Core Access** | Provision via BTP cockpit or [Starter Kit](https://github.com/SAP-samples/btp-genai-starter-kit) |
| **IDE** | VS Code, Cursor, or any MCP-compatible editor |
| **AI Assistant** | Claude Code, GitHub Copilot, Cursor, or similar |

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add resources to this directory.

---

<p align="center">
  If you found this useful, please <b>star this repo</b> and share it with the SAP community!
  <br><br>
  <a href="https://github.com/vigneshbarani24/awesome-sap-ai">
    <img src="https://img.shields.io/github/stars/vigneshbarani24/awesome-sap-ai?style=social" alt="Star this repo">
  </a>
</p>
