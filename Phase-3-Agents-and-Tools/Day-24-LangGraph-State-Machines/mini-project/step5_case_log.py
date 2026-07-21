"""
Mini-project step 5 - A CASE LOG that ACCUMULATES: reducers.

Support teams keep an audit trail: who touched the ticket, what they did.
Let's make every node append one line to a `log` list in the state.

The catch: by default a node's update REPLACES a field -- if clean() returns
{"log": ["cleaned"]} and classify() returns {"log": ["classified"]}, the second
write would WIPE the first. The fix is a REDUCER: annotate the field with HOW
updates merge, and LangGraph appends instead of overwrites:

    log: Annotated[list, add]     # add = operator.add = list concatenation

New ideas vs step 4:
    - Annotated[list, add]: the reducer -> every node's log entry survives
    - nodes now return {"log": ["one new line"]} alongside their real update
    (Same trick, prewritten for chats: add_messages / MessagesState -> step 6.)

Setup:
    pip install langgraph
Run:
    python step5_case_log.py
"""

import re
from operator import add
from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    message: str
    cleaned: str
    order_id: str
    category: str
    reply: str
    issues: list
    attempts: int
    log: Annotated[list, add]   # NEW: updates APPEND (reducer), never overwrite


# --- Same pipeline as step 4, each node now also logs one line -------------
def clean(state: State) -> dict:
    tidy = " ".join(state["message"].split())
    return {"cleaned": tidy, "log": ["clean: normalized text"]}

def find_order_id(state: State) -> dict:
    match = re.search(r"ORD-\d+", state["cleaned"], re.IGNORECASE)
    oid = match.group(0).upper() if match else ""
    return {"order_id": oid,
            "log": [f"find_order_id: {oid or 'none found'}"]}

def classify(state: State) -> dict:
    text = state["cleaned"].lower()
    if any(w in text for w in ("refund", "payment", "charged", "invoice", "money")):
        cat = "billing"
    elif any(w in text for w in ("broken", "crash", "error", "not working", "damaged")):
        cat = "technical"
    else:
        cat = "general"
    return {"category": cat, "log": [f"classify: routed to {cat}"]}

def route(state: State) -> str:
    return state["category"]

def billing(state: State) -> dict:
    return {"reply": "Refund is being processed.",
            "log": ["billing: wrote first draft"]}

def technical(state: State) -> dict:
    return {"reply": "Please send a photo of the damage.",
            "log": ["technical: wrote first draft"]}

def general(state: State) -> dict:
    return {"reply": "We got your message.",
            "log": ["general: wrote first draft"]}

def review(state: State) -> dict:
    reply, issues = state["reply"], []
    if "softkart" not in reply.lower():
        issues.append("no greeting")
    if state["order_id"] and state["order_id"] not in reply:
        issues.append("order not referenced")
    if "within" not in reply.lower():
        issues.append("no timeline promised")
    note = "PASS" if not issues else f"flagged: {', '.join(issues)}"
    return {"issues": issues, "attempts": state["attempts"] + 1,
            "log": [f"review #{state['attempts'] + 1}: {note}"]}

def improve(state: State) -> dict:
    reply, fix = state["reply"], state["issues"][0]
    if fix == "no greeting":
        reply = "SoftKart support here. " + reply
    elif fix == "order not referenced":
        reply = f"{reply} This is regarding your order {state['order_id']}."
    elif fix == "no timeline promised":
        reply = f"{reply} We will update you within 24 hours."
    return {"reply": reply, "log": [f"improve: fixed '{fix}'"]}

MAX_ATTEMPTS = 5

def good_enough(state: State) -> str:
    if not state["issues"] or state["attempts"] >= MAX_ATTEMPTS:
        return "ok"
    return "fix"


# --- Same wiring as step 4 -------------------------------------------------
builder = StateGraph(State)
for name, fn in [("clean", clean), ("find_order_id", find_order_id),
                 ("classify", classify), ("billing", billing),
                 ("technical", technical), ("general", general),
                 ("review", review), ("improve", improve)]:
    builder.add_node(name, fn)

builder.add_edge(START, "clean")
builder.add_edge("clean", "find_order_id")
builder.add_edge("find_order_id", "classify")
builder.add_conditional_edges("classify", route,
    {"billing": "billing", "technical": "technical", "general": "general"})
for name in ("billing", "technical", "general"):
    builder.add_edge(name, "review")
builder.add_conditional_edges("review", good_enough, {"ok": END, "fix": "improve"})
builder.add_edge("improve", "review")

graph = builder.compile()


# --- Run one ticket, then read the whole trail back ------------------------
msg = "My blender from ORD-2481 is not working, it sparks on start"
print(f"Customer : {msg}")
result = graph.invoke({"message": msg, "cleaned": "", "order_id": "",
                       "category": "", "reply": "", "issues": [],
                       "attempts": 0, "log": []})
print(f"SoftKart : {result['reply']}\n")

print(f"Case log ({len(result['log'])} entries -- every node, every loop pass):")
for i, entry in enumerate(result["log"], 1):
    print(f"  {i:2}. {entry}")

print()
print("Without the reducer, only the LAST entry would have survived. This")
print("append-don't-overwrite trick is exactly how chat HISTORY works --")
print("next (step 6): swap the log for messages and make it a real chatbot.")
