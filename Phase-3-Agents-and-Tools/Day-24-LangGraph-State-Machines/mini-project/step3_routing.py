"""
Mini-project step 3 - BRANCHING: route each ticket to the right team.

SoftKart gets three kinds of tickets. One generic reply is bad support --
billing questions should go to billing, breakage to tech, the rest to general.

    START -> clean -> find_order_id -> classify --(route)--> billing
                                                       |---> technical
                                                       |---> general
                                                 (all three) -> END

New ideas vs step 2:
    - classify(): a node that RECORDS a category in the state
    - route(): a ROUTER function that returns the NAME of the next node
    - add_conditional_edges(): the fork -- the move an LCEL | chain can't make

Note the separation of jobs: the node changes STATE, the router picks the PATH.

Setup:
    pip install langgraph
Run:
    python step3_routing.py
"""

import re
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    message: str
    cleaned: str
    order_id: str
    category: str    # NEW: filled by classify(), read by the router
    reply: str


# --- Nodes carried over from step 2 (unchanged) ----------------------------
def clean(state: State) -> dict:
    return {"cleaned": " ".join(state["message"].split())}


def find_order_id(state: State) -> dict:
    match = re.search(r"ORD-\d+", state["cleaned"], re.IGNORECASE)
    return {"order_id": match.group(0).upper() if match else ""}


# --- NEW 1. classify: look at the text, record a category ------------------
# Rule-based on purpose: the lesson is the GRAPH SHAPE, not the classifier.
# (In step 6 -- and for real -- a model makes this call. Same wiring.)
def classify(state: State) -> dict:
    text = state["cleaned"].lower()
    if any(w in text for w in ("refund", "payment", "charged", "invoice", "money")):
        category = "billing"
    elif any(w in text for w in ("broken", "crash", "error", "not working", "damaged")):
        category = "technical"
    else:
        category = "general"
    print(f"[classify] -> {category}")
    return {"category": category}


# --- NEW 2. The router: reads state, returns a NAME (changes nothing) ------
def route(state: State) -> str:
    return state["category"]     # "billing" | "technical" | "general"


# --- NEW 3. One specialist node per branch ---------------------------------
def billing(state: State) -> dict:
    ref = f" for order {state['order_id']}" if state["order_id"] else ""
    return {"reply": f"SoftKart billing team here. We are reviewing the payment{ref}; "
                     f"any wrongly deducted amount is auto-refunded in 5-7 working days."}


def technical(state: State) -> dict:
    ref = f" (order {state['order_id']})" if state["order_id"] else ""
    return {"reply": f"SoftKart tech support here{ref}. Sorry about that! Please share "
                     f"a photo/screenshot of the issue and we will arrange a replacement."}


def general(state: State) -> dict:
    return {"reply": "SoftKart support here. Thanks for reaching out -- "
                     "a team member will reply within one working day."}


# --- Wire it: the straight part, then the fork -----------------------------
builder = StateGraph(State)
for name, fn in [("clean", clean), ("find_order_id", find_order_id),
                 ("classify", classify), ("billing", billing),
                 ("technical", technical), ("general", general)]:
    builder.add_node(name, fn)

builder.add_edge(START, "clean")
builder.add_edge("clean", "find_order_id")
builder.add_edge("find_order_id", "classify")

# The fork: after classify, call route(state); its return value picks the node.
builder.add_conditional_edges(
    "classify",
    route,
    {"billing": "billing", "technical": "technical", "general": "general"},
)

for name in ("billing", "technical", "general"):
    builder.add_edge(name, END)

graph = builder.compile()


# --- Same compiled graph, three different paths ----------------------------
for msg in [
    "I was charged Rs. 999 twice for ORD-1104, I want a refund",
    "The mixer I got in ORD-2481 arrived broken",
    "Do you deliver to Lucknow?",
]:
    print(f"\nCustomer : {msg}")
    result = graph.invoke({"message": msg, "cleaned": "", "order_id": "",
                           "category": "", "reply": ""})
    print(f"SoftKart : [{result['category']}] {result['reply']}")

print()
print("Which path ran was decided AT RUNTIME by the data. Next (step 4): a")
print("reviewer node that can send a bad reply BACK for another try -- a loop.")
