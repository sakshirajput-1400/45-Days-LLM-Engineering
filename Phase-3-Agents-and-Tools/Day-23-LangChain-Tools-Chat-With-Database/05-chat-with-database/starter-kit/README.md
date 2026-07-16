# Starter Kit — Build "Chat With Your Database" Yourself

This is the **build-it-yourself** version of the module-05 project. Instead of
reading the finished code, you fill in the interesting parts and watch the agent
come alive one file at a time.

You type a plain-English question; a Groq model inspects the schema, writes SQL,
runs it with your tools, reads the rows, and answers in words — a **text-to-SQL
agent**, assembled from the tool-calling pieces you learned in modules 01–04.

## What's given vs. what you write

| File | Status | What it is |
|------|:------:|-----------|
| `build_sample_db.py` | ✅ given | Generates `store.db` (the sample data) |
| `db.py` | ✅ given | Safe **read-only** data layer (schema + SELECT-only guard) |
| `tools.py` | ✍️ **you** | Wrap the three db functions as `@tool`s |
| `agent.py` | ✍️ **you** | The **tool-calling loop** (the heart of the project) |
| `cli.py` | ✍️ **you** | The terminal chat loop |
| `app.py` | ✍️ **you** | The Streamlit chat handler |

The two given files are *plumbing* — data generation and database safety. Every
file that teaches the agent idea, you build. Each stub has numbered `TODO`s and a
self-test you can run as you go.

> **Answer key:** the completed versions live one folder up (`../tools.py`,
> `../agent.py`, …). Try the TODOs first; peek only when stuck.

## Setup (once)

```bash
# real CPython -- see repo CLAUDE.md
pip install -r requirements.txt

python build_sample_db.py          # creates store.db
cp .env.example .env               # then paste your free Groq key into .env
```

A key is **optional** while you build — `db.py`, `tools.py`, and the `agent.py`
demo all run offline. You only need `GROQ_API_KEY` to chat with a real model.
Get one free at [console.groq.com/keys](https://console.groq.com/keys).

## Build order (do them in this order — each step you can run)

1. **`python db.py`** — no code to write. Confirms the database exists and the
   read-only guard blocks writes. If this prints a schema and a blocked `DELETE`,
   you're ready.

2. **`tools.py`** → run `python tools.py`. Write the three `@tool` wrappers.
   Success = the three tools print real results and a bad query comes back as
   *text* (not a crash).

3. **`agent.py`** → run `python agent.py`. Write the tool-calling loop in
   `answer_question`. With no key, an **offline stand-in** model drives your loop
   through a real 3-tool sequence — success = *"There are 15 customers from
   Pune."* via `list_tables → describe_table → run_sql_query`.

4. **`cli.py`** → run `python cli.py`. Write the terminal chat loop (needs a key
   to ask your own questions; runs one offline demo without one).

5. **`app.py`** → run `streamlit run app.py`. Write the chat handler. Watch the
   **"How I got this"** expander to see every tool call behind an answer.

## Safety — why `db.py` is locked down

You're handing SQL-writing power to a model, so the given `db.py` takes two
precautions you should understand:

1. **Read-only connection** (`mode=ro`) — any write *fails at the driver*.
2. **SELECT-only validation** — anything that isn't a single `SELECT` (no `DROP`,
   no `;`-stacking) is rejected before it runs.

And your `tools.py` returns errors **as text**, so a bad query becomes feedback
the model reads and corrects on the next loop — not a crash.

## Questions to try (once you have a key)

- How many customers are from Maharashtra?
- Which product category has the most products?
- What are the 5 most expensive products?
- Which customer has placed the most orders?
- What's the total value of all delivered orders?

Often the agent takes three or four tool calls to reach one answer. That
multi-step loop is what makes it an **agent**, not a chatbot.

➡ Back to the [project overview](../README.md) · Then the [exercises](../../exercises/README.md).
