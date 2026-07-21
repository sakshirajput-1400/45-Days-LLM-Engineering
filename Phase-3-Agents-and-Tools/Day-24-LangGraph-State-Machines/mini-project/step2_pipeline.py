"""
Mini-project step 2 - A linear PIPELINE: three nodes, each does one job.

Step 1 had one node do everything. Real support flows have stages:

    START -> clean -> find_order_id -> draft_reply -> END

Each node reads the shared state and returns ONLY the field it filled in --
like three desk employees passing one case file down the counter.

New ideas vs step 1:
    - a richer State (several fields, filled in gradually)
    - multiple nodes chained with fixed edges (a "chain", but graph-style)

Setup:
    pip install langgraph
Run:
    python step2_pipeline.py
"""

import re
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# --- 1. The state grows: one field per stage of the pipeline ---------------
class State(TypedDict):
    message: str     # raw customer text (input)
    cleaned: str     # filled by clean()
    order_id: str    # filled by find_order_id() ("" if none found)
    reply: str       # filled by draft_reply()


# --- 2. Three small nodes, one job each ------------------------------------
def clean(state: State) -> dict:
    """Normalize whitespace and trim -- garbage in, tidy text out."""
    tidy = " ".join(state["message"].split())
    print(f"[clean]         {tidy!r}")
    return {"cleaned": tidy}


def find_order_id(state: State) -> dict:
    """Pull out a SoftKart order id like ORD-1234, if the customer gave one."""
    match = re.search(r"ORD-\d+", state["cleaned"], re.IGNORECASE)
    order_id = match.group(0).upper() if match else ""
    print(f"[find_order_id] {order_id or '(none found)'}")
    return {"order_id": order_id}


def draft_reply(state: State) -> dict:
    """Write the answer, using whatever earlier nodes put in the state."""
    if state["order_id"]:
        reply = (f"Thanks for contacting SoftKart! We are checking order "
                 f"{state['order_id']} and will update you within 24 hours.")
    else:
        reply = ("Thanks for contacting SoftKart! Please share your order id "
                 "(it looks like ORD-1234) so we can look it up.")
    return {"reply": reply}


# --- 3. Wire them in a straight line ---------------------------------------
builder = StateGraph(State)
builder.add_node("clean", clean)
builder.add_node("find_order_id", find_order_id)
builder.add_node("draft_reply", draft_reply)

builder.add_edge(START, "clean")
builder.add_edge("clean", "find_order_id")
builder.add_edge("find_order_id", "draft_reply")
builder.add_edge("draft_reply", END)

graph = builder.compile()


# --- 4. Run it on two messages: with and without an order id ---------------
for msg in [
    "   hi,   my parcel  ord-2481   has not arrived  ",
    "My payment of Rs. 999 failed but money was deducted!",
]:
    print(f"\nCustomer : {msg.strip()}")
    result = graph.invoke({"message": msg, "cleaned": "", "order_id": "", "reply": ""})
    print(f"SoftKart : {result['reply']}")

print()
print("A pipeline is a graph whose edges happen to form a line -- so far a")
print("| chain could do this too. Next (step 3): a fork a chain CANNOT do.")
