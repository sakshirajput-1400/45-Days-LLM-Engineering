# Mini-project — SoftKart Support Desk (one example, scaled up 6 times)

We build **one** app — the support desk of *SoftKart*, an imaginary Indian online store — and
grow it step by step. Every step is a complete, runnable script that **adds exactly one LangGraph
idea** on top of the previous one. Read the file, run it, diff it in your head against the step
before, then move on.

> Learning LangGraph from scratch? Start with the [slide deck](../presentation/index.html), skim
> each concept module (`01`–`06`) as it comes up, and use these steps as the thing you actually build.

## The build, at a glance

| Step | File | New idea (and the module that teaches it) | Needs key? |
|------|------|-------------------------------------------|------------|
| 1 | [`step1_hello_graph.py`](step1_hello_graph.py) | The cycle: `State → node → edges → compile → invoke` ([`01`](../01-why-langgraph/README.md)) | No |
| 2 | [`step2_pipeline.py`](step2_pipeline.py) | Several nodes in a line; each returns **only the keys it changed** ([`02`](../02-state-and-nodes/README.md)) | No |
| 3 | [`step3_routing.py`](step3_routing.py) | **Branching**: `classify` node + router + `add_conditional_edges` ([`03`](../03-conditional-edges/README.md)) | No |
| 4 | [`step4_quality_loop.py`](step4_quality_loop.py) | **A cycle**: review → improve → review until the reply passes, with an attempt cap ([`04`](../04-cycles-and-loops/README.md)) | No |
| 5 | [`step5_case_log.py`](step5_case_log.py) | **Reducers**: `log: Annotated[list, add]` — an audit trail that appends, never overwrites ([`05`](../05-reducers-and-messages/README.md)) | No |
| 6 | [`step6_supportdesk_bot.py`](step6_supportdesk_bot.py) | **The real bot**: `MessagesState` + Groq specialists per branch + `MemorySaver` + `thread_id` ([`06`](../06-chatbot-with-memory/README.md)) | Optional* |

\* Step 6 uses your free Groq key from `.env`; without one it runs an offline stand-in model that
still shows the routing and the growing memory.

## How the story grows

```
step 1   START → [acknowledge] → END                      one node, proves the cycle
step 2   START → clean → find_order_id → draft → END      a pipeline (still a line)
step 3            …    → classify ⇢ billing|tech|general  the line FORKS (runtime choice)
step 4                       … → review ⇠ improve         an edge points BACKWARD (loop)
step 5   every node appends to log: Annotated[list, add]  state that accumulates
step 6   MessagesState + checkpointer + thread_id + Groq  it chats, routes, remembers
```

Two things stay fixed the whole way — that's the point:
- **The example never changes.** Same store, same refund/broken-mixer tickets. Only the *shape of
  the graph* grows, so every diff you see is pure LangGraph.
- **Nodes stay tiny functions.** `clean`, `classify`, `review` are the same kind of function in
  step 6 as in step 2 — the framework never asks for more than *state in, changed keys out*.

## Run it

```bash
pip install langgraph langchain-groq python-dotenv

python step1_hello_graph.py
python step2_pipeline.py
python step3_routing.py
python step4_quality_loop.py
python step5_case_log.py
python step6_supportdesk_bot.py    # add GROQ_API_KEY=... to a .env here for live answers
```

## Checkpoint questions (answer before moving to the next step)

1. **After step 1:** what does `graph.invoke(...)` return — the node's return value, or something else?
2. **After step 2:** why does `draft_reply` return `{"reply": ...}` and not the whole state?
3. **After step 3:** what's the difference between `classify` (a node) and `route` (a router)? Which one is allowed to change state?
4. **After step 4:** what are the *two* safety nets that stop the review loop running forever?
5. **After step 5:** what would the case log contain if `log` had no reducer annotation?
6. **After step 6:** why do we send *only the new message* each turn — where does the rest of the conversation come from?

<details><summary>Answers</summary>

1. The **final state** (a dict with all fields) after the graph reaches `END` — node returns are merged into it along the way.
2. A node returns **only the keys it changed**; LangGraph merges the partial update. Returning everything invites accidental overwrites.
3. `classify` writes `category` into the state. `route` only *reads* state and returns a **name** used to pick the next node — it must not change state.
4. Our own `attempts` counter checked in `good_enough` (escalate at `MAX_ATTEMPTS`), plus LangGraph's built-in `recursion_limit`.
5. Only the **last** entry — each node's `{"log": [...]}` would *replace* the previous list instead of appending to it.
6. The **checkpointer** saved the thread's state after every step; `thread_id` tells it which conversation to reload before your new message is appended.

</details>

## Stretch goals (after step 6)
- Add step 4's **quality loop** after each specialist in step 6, so even the model's replies get reviewed.
- Add an `escalate` branch: if `classify` sees "urgent" or "legal", skip the specialists and reply with a human hand-off.
- Swap `MemorySaver` for `SqliteSaver` (`langgraph-checkpoint-sqlite`) so threads survive a restart.
- Let **the model** classify: replace the keyword `if`s with a small Groq call returning one word. Same graph, smarter router — that's one step from Day 25's agent.

➡ Next: [`../exercises/`](../exercises/README.md), then **Day 25 — ReAct agents** (`create_agent`
builds exactly this kind of graph for you, with the model deciding the route).
