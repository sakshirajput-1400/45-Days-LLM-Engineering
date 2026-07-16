# 03 · Binding tools to a model — let it choose

We have tools. Now we **give them to the model** so it can decide, on its own, which one to call.
One method does it: **`.bind_tools([...])`**.

```python
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
llm_with_tools = llm.bind_tools([multiply, word_count])
```

`llm_with_tools` is the same model, but every request now also carries the **schemas** of your tools
(the name/description/args from module 02). The model reads them and, when a question needs one,
answers with a **tool call** instead of prose.

## What comes back is *not* an answer — it's a request

```python
resp = llm_with_tools.invoke("What is 24 * 7?")
resp.content       # '' (empty — the model didn't answer, it wants a tool)
resp.tool_calls    # [{'name': 'multiply', 'args': {'a': 24, 'b': 7}, 'id': 'call_abc'}]
```

Read `resp.tool_calls`. That's the model saying *"call `multiply(a=24, b=7)` for me."* Each entry has:

| Field | Meaning |
|-------|---------|
| `name` | which tool to run |
| `args` | the arguments to pass (a dict — exactly what `tool.invoke()` wants) |
| `id`   | a ticket number; the result must be returned quoting this id (module 04) |

For a question that needs **no** tool ("Say hello"), `tool_calls` is empty and `content` has the
reply — the model only reaches for a tool when it helps.

## The key idea

> **You never tell the model which tool to use. It decides.** You just bind the toolbox and read
> `tool_calls`. This is the moment a chatbot starts behaving like an agent.

## Run it

```bash
python bind_tools.py
```

With a **free Groq key** (`GROQ_API_KEY` in a `.env`) you'll see the model pick the right tool for
each question. **Without a key** the script still runs: it prints the exact tool **schemas** that get
sent to the model, so you can see what binding actually does.

➡ Next: [`04-tool-calling-loop/`](../04-tool-calling-loop/README.md) — run the tool the model asked
for, hand the result back, and get a final answer. The full loop.
