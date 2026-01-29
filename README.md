# 🧠 BrainByte: Goal-Based AI Assistant

BrainByte is an **advanced multi-agent orchestration system** designed to automate **technical research and content creation**.

It follows a hierarchical **Manager–Worker (Strategist–Researcher)** pattern to:

* search the live web
* log raw evidence
* and synthesize a polished, professional final output

This project is ideal for **research automation, technical comparisons, agentic workflows, and AI-driven analysis**.

---

## ✨ Key Capabilities

* 🔍 **Live Web Research** using DuckDuckGo
* 🧠 **Multi-Agent Reasoning** (Planner + Worker pattern)
* 📝 **Automatic Research Logging** for transparency
* 📄 **Clean Markdown Output** for reports & scripts
* ⚡ **Fast, Reproducible Environments** using `uv`

---

## 📥 Installation Guide

### 1️⃣ Install `uv` (Package Manager)

`uv` is a modern, ultra-fast Python package manager written in **Rust**.

#### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### macOS / Linux (Terminal)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

> 💡 macOS users can also install via Homebrew:

```bash
brew install uv
```

---

### 2️⃣ Setup Project & Dependencies

Clone the repository and install all required dependencies using `uv`:

```bash
# Create a virtual environment
uv venv

# Install project dependencies
uv pip install openai-agents ddgs trafilatura python-dotenv
```

---

## 🔐 Environment Variables (.env)

Create a `.env` file in the project root and add your API keys:

```env
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

> 🔒 These keys are loaded securely using `python-dotenv` and are **never hard-coded**.

---

## 🛠️ Package Requirements

This project relies on the following core libraries:

* **openai-agents** → Framework for building multi-agent workflows
* **ddgs** → Lightweight DuckDuckGo Search API
* **trafilatura** → Extracts clean article text from web pages
* **python-dotenv** → Secure environment variable management

---

## 📂 Project Structure

```
.
├── src/
│   ├── tools/
│   │   ├── search.py       # Web search & scraping tool
│   │   └── file_ops.py     # Local file management utilities
│   ├── main.py             # Orchestrator & entry point
│   └── my_agents.py        # Agent definitions (Strategist & Researcher)
│
├── goal.txt                # Define your objective here
├── raw_research.md         # Auto-generated log of web research
└── final_output.md         # Polished final Markdown output
```

---

## 🚀 How to Run

1️⃣ Add your API keys to the `.env` file

2️⃣ Write your objective inside `goal.txt`

Example:

```
Compare Pydantic V2 vs V1 performance
```

3️⃣ Execute the project:

```bash
uv run python -m src.main
```

---

## 📊 Process Flow

BrainByte follows a **strict Planning & Execution loop**:

1. **Clean Start**
   Previous research logs are wiped for a fresh session

2. **Strategic Planning**
   The Strategist analyzes the goal and decides what research is needed

3. **Deep Research**
   The Researcher uses the `web_search` tool to fetch live web data

4. **Auto-Logging**
   All raw findings are appended to `raw_research.md`

5. **Final Synthesis**
   The Strategist compiles insights into `final_output.md`

---

## 🎯 Output Artifacts

* **raw_research.md** → Transparent evidence & source log
* **final_output.md** → Clean, human-readable Markdown report

---

## 🧠 Why BrainByte?

BrainByte is built to demonstrate **agentic AI best practices**:

* deterministic workflows
* evidence-backed reasoning
* async-friendly orchestration
* reproducible environments

Perfect for:

* technical research automation
* AI demos & experiments
* interview projects
* internal tooling

---

Happy building 🚀
