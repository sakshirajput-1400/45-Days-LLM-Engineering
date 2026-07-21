"""
Mini-project step 4 - A QUALITY LOOP: review the reply, redraft until good.

SoftKart has reply standards: greet the customer, reference their order, give
a timeline. Step 3's specialists now write a quick first draft, and a NEW
reviewer node checks it. Not up to standard? An improver node patches it and
sends it BACK to review -- an edge pointing backward. A | chain can never do this.

    ... classify --> (billing|technical|general)
                          |
                          v
                against   [ review ] --ok--> END
                standards     ^  |
                              |  +--fix--> [ improve ] ---+
                              +---------------------------+   (the cycle)

New ideas vs step 3:
    - review(): a node that judges the draft and lists what's missing
    - a conditional edge whose target is BEHIND it -> a cycle
    - loop safety: our own attempt cap in state (+ LangGraph's recursion_limit)

Setup:
    pip install langgraph
Run:
    python step4_quality_loop.py
"""

import re
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    message: str
    cleaned: str
    order_id: str
    category: str
    reply: str
    issues: list     # NEW: what review() found wrong with the current draft
    attempts: int    # NEW: our own safety counter for the loop


# --- Carried over (unchanged from step 3) ----------------------------------
def clean(state: State) -> dict:
    return {"cleaned": " ".join(state["message"].split())}

def find_order_id(state: State) -> dict:
    match = re.search(r"ORD-\d+", state["cleaned"], re.IGNORECASE)
    return {"order_id": match.group(0).upper() if match else ""}

def classify(state: State) -> dict:
    text = state["cleaned"].lower()
    if any(w in text for w in ("refund", "payment", "charged", "invoice", "money")):
        return {"category": "billing"}
    if any(w in text for w in ("broken", "crash", "error", "not working", "damaged")):
        return {"category": "technical"}
    return {"category": "general"}

def route(state: State) -> str:
    return state["category"]


# --- The specialists now write a LAZY first draft (on purpose) -------------
# Too short, no greeting, no order reference -- so the reviewer has work to do.
def billing(state: State) -> dict:
    return {"reply": "Refund is being processed."}

def technical(state: State) -> dict:
    return {"reply": "Please send a photo of the damage."}

def general(state: State) -> dict:
    return {"reply": "We got your message."}


# --- NEW 1. review: judge the draft against SoftKart's reply standards -----
def review(state: State) -> dict:
    reply, issues = state["reply"], []
    if "softkart" not in reply.lower():
        issues.append("no greeting")
    if state["order_id"] and state["order_id"] not in reply:
        issues.append("order not referenced")
    if "within" not in reply.lower():
        issues.append("no timeline promised")
    verdict = "PASS" if not issues else f"NEEDS WORK ({', '.join(issues)})"
    print(f"[review]  draft {state['attempts'] + 1}: {verdict}")
    return {"issues": issues, "attempts": state["attempts"] + 1}


# --- NEW 2. improve: patch ONE missing thing, then go around again ---------
# One fix per pass so you can WATCH the loop converge run by run.
def improve(state: State) -> dict:
    reply, fix = state["reply"], state["issues"][0]
    if fix == "no greeting":
        reply = "SoftKart support here. " + reply
    elif fix == "order not referenced":
        reply = f"{reply} This is regarding your order {state['order_id']}."
    elif fix == "no timeline promised":
        reply = f"{reply} We will update you within 24 hours."
    print(f"[improve] fixed: {fix}")
    return {"reply": reply}


# --- NEW 3. The loop decision: out, around again, or bail out --------------
MAX_ATTEMPTS = 5

def good_enough(state: State) -> str:
    if not state["issues"]:
        return "ok"
    if state["attempts"] >= MAX_ATTEMPTS:
        print("[guard] attempt cap hit -- escalating to a human, not looping forever")
        return "ok"
    return "fix"


# --- Wire it: step 3's shape + the backward edge ---------------------------
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

# Every specialist's draft goes to review (instead of straight to END)...
for name in ("billing", "technical", "general"):
    builder.add_edge(name, "review")

# ...and review either exits or loops back through improve. THE cycle:
builder.add_conditional_edges("review", good_enough, {"ok": END, "fix": "improve"})
builder.add_edge("improve", "review")

graph = builder.compile()


# --- Watch one ticket loop until the draft passes --------------------------
msg = "I was charged Rs. 999 twice for ORD-1104, I want a refund"
print(f"Customer : {msg}\n")
result = graph.invoke({"message": msg, "cleaned": "", "order_id": "",
                       "category": "", "reply": "", "issues": [], "attempts": 0})
print(f"\nFinal reply after {result['attempts']} review passes:")
print(f"SoftKart : {result['reply']}")
print()
print("draft -> check -> fix -> check ... is the skeleton of every agent: on")
print("Day 25 the 'improve' step becomes a MODEL deciding what to try next.")
print("Next (step 5): keep a case LOG that accumulates instead of overwrites.")
