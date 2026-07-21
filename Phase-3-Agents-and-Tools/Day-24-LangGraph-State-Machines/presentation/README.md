# Day 24 deck — *LangGraph: when a line becomes a map* (speaker notes)

Open [`index.html`](index.html) in any browser. `→` / `Space` to advance, `F` for fullscreen.
17 slides ≈ 35–40 min, leaving the rest of the 3-hour block for the modules + mini-project.

**The through-line:** Day 21 gave us a straight line (`prompt | model | parser`). Real apps need
*if / until / remember*. LangGraph is nothing but **three words — State, Node, Edge** — plus four
moves (branch, loop, accumulate, remember). Keep repeating the three words; everything hangs off them.

| # | Slide | Time | What to say / do |
|---|-------|------|------------------|
| 1 | Cover | 1′ | "By tonight your app will make decisions at runtime. That's the doorway to agents." |
| 2 | Three things a `\|` chain cannot do | 3′ | Ask the class to shout app ideas; show each one contains an *if*, an *until*, or a *remember*. That's the tell. Remind them Day 23's tool loop was a hand-written `while` — today we get the proper machine for it. |
| 3 | Flowchart that runs | 2′ | Point at the dashed arrows: "your code draws this; LangGraph runs it." Don't explain syntax yet. |
| 4 | State · Node · Edge | 3′ | **The most important slide.** Make them say it back: "nodes are functions, edges are wires, state is a dict." Everything later is detail. |
| 5 | State | 3′ | The case-file analogy lands well: each employee writes their bit in the shared file. `TypedDict` = Day 8 callback. |
| 6 | Nodes | 3′ | Emphasise the #1 beginner surprise: **return only the keys you changed**, LangGraph merges. Don't mutate, don't return everything. |
| 7 | The 6-line recipe | 4′ | Live-type this if you can. Land the payoff: the compiled graph is a **Runnable** — same `.invoke()` as Day 21. |
| 8 | Conditional edges | 4′ | Router = tiny function returning a *name*; map turns name → node. Stress the separation: nodes change state, routers pick paths. Tease Day 25: "soon the *model* is the router." |
| 9 | Cycles | 4′ | The headline move — a chain can never do this. Walk the red backward arrow. Hammer safety: exit condition + attempt cap + `recursion_limit`. |
| 10 | Reducers | 4′ | Show the broken (overwrite) column first, let them feel the bug, then the `Annotated[list, add]` fix. `MessagesState` = Day 16's append-every-turn, automated. |
| 11 | Memory | 4′ | Checkpointer saves after every step; `thread_id` names the conversation; you send **only the new message**. Mention the SQLite upgrade path = same code in production. |
| 12 | Chain vs graph table | 2′ | Rule of thumb: straight line → chain; any *if/until/remember* → graph. Chains are not obsolete! |
| 13 | Mini-project | 3′ | Sell the build: **one** example (SoftKart Support Desk) scaled six times, each step = one new move. Steps 1–5 no key. |
| 14 | Roadmap | 2′ | The money slide for motivation: Day 23 = hands, today = engine, Day 25 `create_agent` = the same loop drawn for you. |
| 15 | Recap | 2′ | Read the six bullets aloud, class fills in the blanks. |
| 16 | Your move | 1′ | Modules 01→06, then `mini-project/` steps 1→6, then the two exercises. |
| 17 | Close | 1′ | "Once your app decides what to do next, it's an agent. Tomorrow we hand the deciding to the model." |

## Q&A ammo
- **"Why not just write `if`/`while` in Python?"** You can — Day 23 did! The graph buys you:
  every step checkpointed (memory, resume, time-travel), streaming per node, a drawable/inspectable
  structure, and the shape agents (`create_agent`) are actually built from. Small scripts don't need
  it; agents do.
- **"Is LCEL dead then?"** No — inside a node you'll happily call a chain. Graph = control flow,
  chain = one step's plumbing.
- **"What's the difference between the router and a node?"** A node returns a *state update* (dict);
  a router returns a *name* (string) and must not change state.
- **"Does `MemorySaver` survive a restart?"** No — RAM only. Same API with SQLite/Postgres savers
  does. That's deliberate: swap one line, keep the code.

➡ After the deck: run `01-why-langgraph/` together, then let them drive the rest.
