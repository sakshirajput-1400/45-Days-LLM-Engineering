"""
Mini-project step 1 - The smallest possible SoftKart support graph.

SoftKart is our (imaginary) Indian online store. Over 6 steps we grow its
support desk from this one-node toy into a routing, self-checking, remembering
chatbot. THIS step only proves the build-compile-invoke cycle:

    state in  ->  [ acknowledge ]  ->  state out

One state, one node, two edges. If you understand this file, you understand
every LangGraph program -- the rest is just more nodes and smarter edges.

Setup:
    pip install langgraph
Run:
    python step1_hello_graph.py
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# --- 1. The state: the "case file" every node reads and writes -------------
# TypedDict (Day 8) = still a plain dict at runtime, but with a declared shape.
class State(TypedDict):
    message: str    # what the customer wrote (input)
    reply: str      # what we answer (output, filled by our node)


# --- 2. The node: a plain function, state in -> CHANGED KEYS out -----------
# We return ONLY {"reply": ...}. LangGraph merges it into the state for us.
def acknowledge(state: State) -> dict:
    reply = (f"Hello from SoftKart support! We received your message: "
             f"'{state['message']}'. A human-quality answer is coming in step 2.")
    return {"reply": reply}


# --- 3. The graph: nodes + wires, then freeze it with .compile() -----------
builder = StateGraph(State)
builder.add_node("acknowledge", acknowledge)
builder.add_edge(START, "acknowledge")   # entry wire
builder.add_edge("acknowledge", END)     # exit wire
graph = builder.compile()


# --- 4. Run it: dict in -> final state (a dict) out ------------------------
result = graph.invoke({"message": "Where is my order?", "reply": ""})

print("Customer :", result["message"])
print("SoftKart :", result["reply"])
print()
print("That's the whole cycle: State -> node -> edges -> compile -> invoke.")
print("Next (step 2): several nodes in a row, each filling in its own field.")
