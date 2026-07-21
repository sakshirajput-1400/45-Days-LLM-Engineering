"""
Mini-project step 6 - THE SOFTKART SUPPORT BOT: everything, together.

The finale combines the whole day into one small, real app:
    - MessagesState        (step 5's reducer trick, prewritten for chat)
    - classify + routing   (step 3) -- now routing to MODEL-backed specialists
    - MemorySaver + thread_id      -- the bot REMEMBERS across .invoke() calls
    - Groq (llama-3.1-8b-instant)  -- each specialist answers with its own
                                      persona system prompt

    START -> classify --> billing_agent ----+
                    |---> technical_agent --+--> END
                    |---> general_agent ----+
    (compiled WITH a checkpointer; every turn lands on a named thread)

Without a GROQ_API_KEY it still runs: an offline stand-in model shows the
routing and the growing memory, so the mechanics are visible either way.

Setup:
    pip install langgraph langchain-groq python-dotenv
    echo GROQ_API_KEY=your_key > .env      (free key: console.groq.com/keys)
Run:
    python step6_supportdesk_bot.py
"""

import os
from dotenv import load_dotenv

from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()
MODEL = "llama-3.1-8b-instant"


# --- 1. Real Groq if we have a key, else an offline stand-in ---------------
if os.getenv("GROQ_API_KEY"):
    from langchain_groq import ChatGroq
    model = ChatGroq(model=MODEL, temperature=0)
    print(f"Using real Groq model: {MODEL}\n")
else:
    from langchain_core.messages import AIMessage

    class FakeModel:
        """Echoes its persona + how much history it sees -- memory made visible."""
        def invoke(self, messages):
            persona = messages[0].content.split(".")[0]     # first system line
            human = [m for m in messages if m.type == "human"]
            return AIMessage(content=f"(offline {persona!r}) I can see "
                                     f"{len(human)} customer messages so far. "
                                     f"Latest: {human[-1].content!r}")
    model = FakeModel()
    print("No GROQ_API_KEY -- offline stand-in model (mechanics still visible).\n")


# --- 2. State: MessagesState (auto-appending history) + our category -------
class ChatState(MessagesState):
    category: str


# --- 3. classify + router, same as step 3 -- on the LATEST customer msg ----
def classify(state: ChatState) -> dict:
    latest = [m for m in state["messages"] if m.type == "human"][-1]
    text = latest.content.lower()
    if any(w in text for w in ("refund", "payment", "charged", "invoice", "money")):
        cat = "billing"
    elif any(w in text for w in ("broken", "crash", "error", "not working", "damaged")):
        cat = "technical"
    else:
        cat = "general"
    print(f"    [classify -> {cat}]")
    return {"category": cat}


def route(state: ChatState) -> str:
    return state["category"]


# --- 4. Model-backed specialists: same persona trick, different prompts ----
PERSONAS = {
    "billing": "You are SoftKart's billing specialist. Be precise about amounts "
               "and always state the refund timeline (5-7 working days). "
               "Answer in 2-3 sentences.",
    "technical": "You are SoftKart's tech support engineer. Be practical, ask for "
                 "photos/details when useful, offer replacement if damaged. "
                 "Answer in 2-3 sentences.",
    "general": "You are SoftKart's friendly customer-care agent for an Indian "
               "online store. Be warm and helpful. Answer in 2-3 sentences.",
}

def make_specialist(category: str):
    """One node per persona: system prompt + FULL history -> model -> reply."""
    def specialist(state: ChatState) -> dict:
        msgs = [SystemMessage(PERSONAS[category])] + state["messages"]
        reply = model.invoke(msgs)
        return {"messages": [reply]}     # add_messages appends it for us
    return specialist


# --- 5. Wire it, and compile WITH a checkpointer ---------------------------
builder = StateGraph(ChatState)
builder.add_node("classify", classify)
for cat in PERSONAS:
    builder.add_node(f"{cat}_agent", make_specialist(cat))

builder.add_edge(START, "classify")
builder.add_conditional_edges("classify", route,
    {cat: f"{cat}_agent" for cat in PERSONAS})
for cat in PERSONAS:
    builder.add_edge(f"{cat}_agent", END)

graph = builder.compile(checkpointer=MemorySaver())   # <- the memory


# --- 6. One customer, one thread: watch it route AND remember --------------
def say(thread: str, text: str) -> None:
    cfg = {"configurable": {"thread_id": thread}}
    result = graph.invoke({"messages": [("human", text)]}, cfg)  # only the new msg
    print(f"Customer : {text}")
    print(f"SoftKart : {result['messages'][-1].content}\n")

print("=== Thread 'aditi' ===")
say("aditi", "My mixer from order ORD-2481 arrived broken and sparks on start.")
say("aditi", "Also I was charged Rs. 999 extra -- when do I get that money back?")
say("aditi", "Remind me, which order was I complaining about?")   # memory test!

saved = graph.get_state({"configurable": {"thread_id": "aditi"}}).values["messages"]
print(f"(thread 'aditi' now stores {len(saved)} messages, both sides)\n")

print("=== Thread 'rahul' (separate memory) ===")
say("rahul", "Which order was I complaining about?")   # fresh thread knows nothing

print("Routing chose the specialist per message; the checkpointer kept each")
print("customer's history separate. Branch + loop-ready + memory = the exact")
print("machine Day 25's create_agent hands to the model. You built it yourself.")
