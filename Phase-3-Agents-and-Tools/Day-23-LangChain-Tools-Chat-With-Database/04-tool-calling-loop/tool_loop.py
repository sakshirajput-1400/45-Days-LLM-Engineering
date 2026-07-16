"""
04 - The tool-calling loop: run the tool, hand the result back, finish.

This is the whole engine of an agent, in ~10 lines:

    messages = [HumanMessage(question)]
    while True:
        ai = model.invoke(messages)          # model's turn
        messages.append(ai)
        if not ai.tool_calls: break          # no tool -> final answer
        for call in ai.tool_calls:           # run each requested tool
            result = TOOL_MAP[call["name"]].invoke(call["args"])
            messages.append(ToolMessage(result, tool_call_id=call["id"]))

With GROQ_API_KEY set, a real model drives the loop. Without a key, an offline
STAND-IN model emits a canned tool call so you still see the exact mechanics.

Setup:
    pip install langchain langchain-groq python-dotenv
Run:
    python tool_loop.py
"""

import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

load_dotenv()
MODEL = "llama-3.1-8b-instant"


# ----------------------------------------------------------------------------
# 1. The toolbox + a name->tool lookup so we can dispatch by name.
# ----------------------------------------------------------------------------
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the exact result."""
    return a * b


@tool
def add(a: int, b: int) -> int:
    """Add two integers and return the exact result."""
    return a + b


TOOLS = [multiply, add]
TOOL_MAP = {t.name: t for t in TOOLS}


# ----------------------------------------------------------------------------
# 2. The loop -- identical whether the model is real or the offline stand-in.
# ----------------------------------------------------------------------------
def run_loop(model, question):
    """Drive model -> tool -> model until the model stops asking for tools."""
    messages = [HumanMessage(content=question)]
    step = 0
    while True:
        step += 1
        ai = model.invoke(messages)         # the model's turn
        messages.append(ai)

        if not ai.tool_calls:               # no tool requested -> we're done
            print(f"  [step {step}] model gave the final answer")
            return ai.content

        # The model asked for one or more tools. Run each and feed results back.
        for call in ai.tool_calls:
            result = TOOL_MAP[call["name"]].invoke(call["args"])
            print(f"  [step {step}] ran {call['name']}({call['args']}) -> {result}")
            # ToolMessage MUST quote tool_call_id so the model matches Q to A.
            messages.append(ToolMessage(content=str(result), tool_call_id=call["id"]))


# ----------------------------------------------------------------------------
# 3a. Offline stand-in model (no key). Mimics a real model's two-turn behaviour.
# ----------------------------------------------------------------------------
class OfflineToolModel:
    """
    Not a real LLM -- a teaching stand-in. First turn: ask to multiply. After it
    sees a ToolMessage, it writes a final answer. Shows the loop with no key.
    """
    def invoke(self, messages):
        already_used_a_tool = any(isinstance(m, ToolMessage) for m in messages)
        if not already_used_a_tool:
            # Pretend the model decided to call multiply(6, 7).
            return AIMessage(
                content="",
                tool_calls=[{"name": "multiply", "args": {"a": 6, "b": 7},
                             "id": "call_offline_1"}],
            )
        # It has the tool result now -- read it back and answer.
        last_result = [m for m in messages if isinstance(m, ToolMessage)][-1].content
        return AIMessage(content=f"The answer is {last_result}.")


# ----------------------------------------------------------------------------
# 3b. Pick the model: real Groq if we have a key, else the stand-in.
# ----------------------------------------------------------------------------
if os.getenv("GROQ_API_KEY"):
    from langchain_groq import ChatGroq
    model = ChatGroq(model=MODEL, temperature=0).bind_tools(TOOLS)
    question = "What is 6 times 7, then add 100 to that?"
    print(f"Using real Groq model.\nQ: {question}")
else:
    model = OfflineToolModel()
    question = "What is 6 times 7?"
    print("No GROQ_API_KEY -- using an OFFLINE stand-in model to show the loop.")
    print(f"Q: {question}")

answer = run_loop(model, question)
print(f"\nFinal answer: {answer}")
print("\nThat model -> tool -> model loop is exactly what the database project runs.")
