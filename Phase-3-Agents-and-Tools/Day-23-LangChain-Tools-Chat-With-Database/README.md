# Day 23 — LangChain Tools + Chat With Your Database

**Phase 3 · Agents & Tools — Day 3.** Days 21–22 gave us LangChain: chains (`prompt | model | parser`),
RAG, and Streamlit apps. But every one of those only **talked**. Today the model learns to **act** —
to call real Python functions, look things up, and run code — using **tools** (a.k.a. function
calling). Then we build the day's project: **Chat With Your Database**, where a model answers
plain-English questions by writing and running live SQL.

> **What you learn:** what a tool is and why an LLM needs one; the `@tool` decorator; binding tools to
> a model with `.bind_tools()`; and the **tool-calling loop** (*model → tool → model*) that turns a
> chatbot into something that takes action. You finish by pointing that loop at a **SQLite database**.

## The one thing an LLM can't do alone

A language model predicts text. It can't do reliable arithmetic, it can't see today's data, and it
can't take any action in the world. A **tool** is just a **Python function** you hand the model. When
a question needs it, the model replies *"call `run_sql_query` with this SQL"*; **your code** runs it
and hands the result back. That hand-off is the whole idea behind agents — and it's what we build,
by hand, today.

## We build the loop by hand — on purpose

Days 24–25 hand you engines that automate this (LangGraph, then `create_agent`). Today you write the
`while` loop yourself, so those engines are never magic:

| Day | What runs the loop |
|-----|--------------------|
| **23 (today)** | **You do** — a hand-written `while` over `.tool_calls` |
| 24 | LangGraph — a proper engine for loops & branching |
| 25 | `create_agent` — builds the whole ReAct loop in one line |

## Learning objectives
By the end of today you can:
- Explain why a tool is needed and what a "tool call" actually is.
- Turn any function into a tool with `@tool`, and write the docstring the **model** reads.
- Bind tools to a Groq model and read `response.tool_calls`.
- Write the **tool-calling loop**: run the tool, return a `ToolMessage`, repeat until answered.
- Build a **text-to-SQL agent** over SQLite, with read-only safety and multi-step tool use.

## What this reuses
| From    | Idea used here                                                    |
|---------|-------------------------------------------------------------------|
| Day 21  | `ChatGroq`, message objects — now carrying tool calls & results    |
| Day 20  | File-per-job project structure — here `db` / `tools` / `agent` / UI |
| Day 19  | Streamlit chat UI (`session_state`, `chat_input`, `cache_resource`) |
| Day 16  | Append-every-turn messages — now including `ToolMessage`s          |

## Module index
| # | Folder | You learn |
|---|--------|-----------|
| 01 | [`01-why-tools/`](01-why-tools/README.md) | Why an LLM needs tools; the model→tool→model idea (pure Python, no key) |
| 02 | [`02-your-first-tool/`](02-your-first-tool/README.md) | The `@tool` decorator; name/description/args; calling a tool by hand |
| 03 | [`03-binding-tools/`](03-binding-tools/README.md) | `.bind_tools()`; reading `response.tool_calls`; the model chooses |
| 04 | [`04-tool-calling-loop/`](04-tool-calling-loop/README.md) | The full loop: run the tool, return a `ToolMessage`, finish the answer |
| 05 | [`05-chat-with-database/`](05-chat-with-database/README.md) | **Project:** a text-to-SQL agent over a SQLite store (CLI + Streamlit) |

### Exercises
| Folder | Practise |
|--------|----------|
| [`exercises/`](exercises/README.md) | Build a tool + run the loop · Add a `count_rows` tool to the DB agent |

## How to run

**Setup (once).** Install with the real CPython (see repo `CLAUDE.md`):
```bash
pip install langchain langchain-core langchain-groq streamlit python-dotenv
```
A free Groq key is only needed for the *live* chat (modules 03–05). Put it in a `.env`:
```
GROQ_API_KEY=your_key_here
```
Get one at [console.groq.com/keys](https://console.groq.com/keys).

**Run the tool modules in order:**
```bash
python 01-why-tools/why_tools.py
python 02-your-first-tool/first_tool.py
python 03-binding-tools/bind_tools.py
python 04-tool-calling-loop/tool_loop.py
```

**Then the project:**
```bash
cd 05-chat-with-database
python build_sample_db.py     # once -> creates store.db (~3,700 rows)
python db.py                  # the read-only data layer (no key)
python tools.py               # the three @tools (no key)
python agent.py               # the full loop via an offline stand-in (no key)
streamlit run app.py          # real chat (needs a key)
```
Modules **01–02** and the project's `db.py`/`tools.py`/`agent.py` all run **with no key** — the tool
machinery is pure Python. Modules **03–05** call Groq for the live answer and print a clear skip (or
run an offline stand-in) without a key.

## Today's exercise
Do both in [`exercises/`](exercises/README.md):
1. **Weather tool** — write a `@tool` and complete the tool-calling loop yourself.
2. **count_rows** — add a fourth tool to the database agent, with safe error handling.

## Latest-syntax notes (LangChain 1.x)
- `from langchain_core.tools import tool` — the `@tool` decorator reads your docstring + type hints.
- `llm.bind_tools([...])` returns a model that can emit `AIMessage.tool_calls`.
- A tool call is `{"name", "args", "id"}`; run it with `tool.invoke(args)`.
- Return results as `ToolMessage(content=..., tool_call_id=call["id"])` — **the id must match**.
- Keep tool functions plain and testable; wrap dangerous power (like SQL) behind read-only guards.

## The big idea
> A chatbot **talks**. Give it tools and a loop, and it **acts** — it looks things up, runs code, and
> works in several steps to reach an answer. That's the leap from "language model" to "agent," and
> "Chat With Your Database" is your first one: plain English in, real SQL run, real numbers out.

➡ Next: **Day 24 — LangGraph** — a real engine for the loops and branches you just hand-wrote, so
your agents can get much bigger without the `while` loop growing out of control.
