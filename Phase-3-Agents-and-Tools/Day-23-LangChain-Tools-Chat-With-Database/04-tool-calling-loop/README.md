# 04 · The tool-calling loop — run the tool, hand it back, finish

Module 03 stopped at the model *asking* for a tool. To actually get an answer we need the full
**loop**: run the tool, give the result back to the model, let it either ask for another tool or
write the final reply. This loop is the beating heart of every agent — and it's short.

## The four message types in play

A tool conversation is a list of messages, just like Day 21 — but with two new kinds:

| Message | Who | Carries |
|---------|-----|---------|
| `HumanMessage` | you | the question |
| `AIMessage` | model | either a final answer **or** `.tool_calls` (a request) |
| `ToolMessage` | your code | the **result** of running a tool, tagged with the call's `id` |
| `SystemMessage` | you | (optional) instructions |

The rule that makes it work: **every `ToolMessage` must quote the `tool_call_id`** from the request,
so the model knows which answer belongs to which question it asked.

## The loop

```python
messages = [HumanMessage(question)]
while True:
    ai = llm_with_tools.invoke(messages)   # model's turn
    messages.append(ai)
    if not ai.tool_calls:                  # no tool wanted -> it's the final answer
        break
    for call in ai.tool_calls:             # run each tool it asked for
        result = TOOL_MAP[call["name"]].invoke(call["args"])
        messages.append(ToolMessage(content=str(result), tool_call_id=call["id"]))
# ai.content now holds the grounded answer
```

Read the shape: **model → tool → model → (maybe tool →) … → answer**. The `while` matters — a hard
question can take several tool calls (look up the schema, *then* run a query, *then* answer). The loop
keeps going until the model stops asking.

## Why a `while`, not a single call?

Because the model can't do everything in one shot. For our database project it will often:
1. call `list_tables` — "what tables exist?"
2. call `describe_table` — "what columns does `orders` have?"
3. call `run_sql_query` — "now run the SELECT"
4. **then** answer in plain English.

Each step feeds the next. That's the loop earning its keep.

## Run it

```bash
python tool_loop.py
```

**With a Groq key** you'll watch a real model drive the loop. **Without a key** the script runs an
**offline stand-in model** that emits a canned tool call, so you can still see the exact loop
mechanics — request → run → `ToolMessage` → final answer.

➡ Next: [`05-chat-with-database/`](../05-chat-with-database/README.md) — the project. We point this
same loop at a **SQLite database** and let a model answer plain-English questions with live SQL.
