# 01 · Why tools? (the thing an LLM cannot do alone)

An LLM is a **text predictor**. Ask it "what is 48973 × 215?" and it will *guess* a
plausible-looking number — often wrong. Ask it "how many orders did we ship yesterday?" and it has
**no idea**: your database wasn't in its training data. The model can *talk* about anything; it can't
*do* anything or *look anything up*.

**Tools** fix that. A tool is just a **normal Python function** we hand to the model. The model
doesn't run it — it can't. Instead the model, when it needs help, replies with a little structured
message that means: *"please call the function `run_sql_query` with these arguments."* Our code runs
the function, hands the result back, and the model uses that real answer to reply.

## The loop, in one picture

```
You:    "How many customers are in Pune?"
Model:  (doesn't know) -> asks to call: run_sql_query("SELECT COUNT(*) ... WHERE city='Pune'")
Your code: runs the SQL -> gets 27 -> hands "27" back to the model
Model:  "There are 27 customers in Pune."
```

The model supplies the **thinking** (which tool, what arguments); your code supplies the **doing**
(actually running it). That hand-off — *model → tool → model* — is the whole idea behind agents.

## Why this matters

| Without tools | With tools |
|---------------|------------|
| Guesses at maths | Calls a calculator — exact |
| Can't see your data | Queries your database — live |
| Can't take actions (send email, book, fetch a URL) | Calls a function that does it |
| Knowledge frozen at training time | Reads fresh, real information |

Today: first the **mechanic** (`@tool`, binding tools to a model, the calling loop), then a real
project — **Chat With Your Database** — where a model answers plain-English questions by writing and
running SQL against a SQLite store.

## Run it

```bash
python why_tools.py
```

No API key needed — this module **simulates** the model's tool request with plain Python so you can
see the mechanic before we bring in a real model.

➡ Next: [`02-your-first-tool/`](../02-your-first-tool/README.md) — turn a function into a real
LangChain tool with `@tool`.
