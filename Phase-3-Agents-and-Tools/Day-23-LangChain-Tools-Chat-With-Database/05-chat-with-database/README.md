# 05 · Project — Chat With Your Database

The payoff. We take the tool-calling loop from module 04 and point it at a **real SQLite database**.
You type a plain-English question; a Groq model inspects the schema, writes SQL, runs it with our
tools, reads the rows, and answers you in words. This is a **text-to-SQL agent** — and it's built
from exactly the pieces you just learned.

```
"Which city has the most customers?"
   -> list_tables            (agent: what tables are there?)
   -> describe_table customers  (agent: what columns?)
   -> run_sql_query "SELECT city, COUNT(*) ... GROUP BY city ORDER BY ... LIMIT 1"
   -> "Mumbai has the most customers, with 38."
```

## What's in the database

`build_sample_db.py` generates a fictional Indian online store — four linked tables, ~3,700 rows
total, same data every time (fixed random seed):

| Table | Rows | Columns |
|-------|-----:|---------|
| `customers` | 150 | customer_id, name, city, state, signup_date |
| `products` | 40 | product_id, name, category, price |
| `orders` | 900 | order_id, customer_id, order_date, status |
| `order_items` | ~2,700 | item_id, order_id, product_id, quantity, unit_price |

Enough data that the answers are non-obvious — you can't eyeball "which category sells most"; the
agent has to actually query for it.

## The files — one job each

| File | Job | Needs a key? |
|------|-----|:-:|
| `build_sample_db.py` | Create `store.db` with all the sample data | no |
| `db.py` | Safe **read-only** data layer: `list_tables` / `get_schema` / `run_query` | no |
| `tools.py` | Wrap those three as `@tool`s the model can call | no |
| `agent.py` | The **tool-calling loop** + system prompt (the brain, no UI) | key to chat |
| `cli.py` | Chat from the terminal | key to chat |
| `app.py` | Chat in the browser (Streamlit) with a "how I got this" panel | key to chat |

The split is deliberate: **the database layer knows nothing about the LLM, and the brain knows
nothing about the UI.** You can test each piece on its own — and the first three run with no key at all.

## Safety: never let a model wreck your data

We're handing SQL-writing power to a model, so `db.py` takes two precautions:

1. **Read-only connection** — the database is opened with `mode=ro`; any write *fails at the driver*.
2. **SELECT-only validation** — anything that isn't a single `SELECT` (no `DROP`, no `;` stacking) is
   rejected before it runs.

A bad query isn't a crash, either — the tool returns the error **as text**, the model reads it on the
next loop, and tries a corrected query. Errors become feedback.

## How to run

```bash
# 0. install (real CPython -- see repo CLAUDE.md)
pip install langchain langchain-groq streamlit python-dotenv

# 1. build the database (once)
python build_sample_db.py

# 2a. try the pieces with NO key -- they really work
python db.py            # schema + a query + a blocked write
python tools.py         # the three tools, called directly
python agent.py         # the full loop, via an offline stand-in model

# 2b. real chat -- put GROQ_API_KEY=... in a .env file, then:
python cli.py           # terminal
streamlit run app.py    # browser
```

Get a free key at [console.groq.com/keys](https://console.groq.com/keys).

## Build it yourself first

Prefer to *build* this instead of reading the finished code? The
[`starter-kit/`](starter-kit/README.md) has the same project with the plumbing
(`build_sample_db.py`, `db.py`) given and the interesting parts — the `@tool`
wrappers, the tool-calling loop, the two UIs — left as guided `TODO`s. The files
in this folder are the answer key.

## Questions to try (once you have a key)

- How many customers are from Maharashtra?
- Which product category has the most products?
- What are the 5 most expensive products?
- How many orders were cancelled?
- Which customer has placed the most orders?
- What's the total value of all delivered orders?

Watch the **"How I got this"** panel (web) or the printed tool calls (CLI): often the agent takes
three or four tool calls to reach one answer. That multi-step loop is what separates an *agent* from
a chatbot.

## Where this goes next

Right now **we** hand-wrote the loop (`while` in `agent.py`). On **Day 24** LangGraph gives us a
proper engine for loops and branching; on **Day 25** `create_agent` builds this whole loop for us in
one line — a **ReAct agent**. You're seeing, by hand, what those tools automate.

➡ Back to the [day overview](../README.md) · Then do the [exercises](../exercises/README.md).
