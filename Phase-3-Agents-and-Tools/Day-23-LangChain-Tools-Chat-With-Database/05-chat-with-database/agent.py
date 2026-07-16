"""
agent.py -- the brain of the project. NO Streamlit here, so we can test it plain.

It's the module-04 tool-calling loop, pointed at the database tools:

    model -> (list_tables) -> model -> (describe_table) -> model
          -> (run_sql_query) -> model -> final English answer

The model is bound to our three DB tools and told, via the system prompt, to
inspect the schema before writing SQL. We cap the loop at MAX_STEPS so a confused
model can never spin forever.

With GROQ_API_KEY set, a real model answers your questions. Without a key, an
OFFLINE stand-in runs a scripted 3-tool sequence so you can watch the loop work.

Setup:
    pip install langchain langchain-groq python-dotenv
Run:
    python build_sample_db.py   # once, to create store.db
    python agent.py             # a couple of demo questions
"""

import os
from dotenv import load_dotenv
from langchain_core.messages import (SystemMessage, HumanMessage, AIMessage,
                                     ToolMessage)

from tools import TOOLS, TOOL_MAP

load_dotenv()
MODEL = "llama-3.1-8b-instant"
MAX_STEPS = 8   # safety cap: at most this many model<->tool round-trips

SYSTEM_PROMPT = (
    "You are a helpful data analyst for an online store. You answer questions by "
    "querying a SQLite database with the tools provided. Follow this process:\n"
    "1. Call list_tables to see what tables exist.\n"
    "2. Call describe_table on the tables you need, to learn the exact columns.\n"
    "3. Call run_sql_query with a single read-only SELECT to get the data.\n"
    "4. Read the rows and answer the user in plain English with the numbers.\n"
    "Never invent table or column names -- always check with the tools first. "
    "If a query errors, read the error and try a corrected query."
)


def answer_question(model, question, verbose=True, on_tool=None):
    """
    Run the tool-calling loop and return the model's final text answer.

    on_tool: optional callback(name, args, result) fired for each tool call.
    The Streamlit app uses it to show the agent's steps; the CLI uses verbose.
    """
    messages = [SystemMessage(content=SYSTEM_PROMPT),
                HumanMessage(content=question)]

    for _ in range(MAX_STEPS):
        ai = model.invoke(messages)
        messages.append(ai)

        if not ai.tool_calls:              # no tool requested -> final answer
            return ai.content

        for call in ai.tool_calls:         # run every tool the model asked for
            result = TOOL_MAP[call["name"]].invoke(call["args"])
            if verbose:
                print(f"   -> {call['name']}({call['args']})")
            if on_tool:
                on_tool(call["name"], call["args"], str(result))
            messages.append(ToolMessage(content=str(result),
                                        tool_call_id=call["id"]))

    return "(Stopped after too many steps -- the question may be too complex.)"


def build_model():
    """Return a Groq model bound to our DB tools (requires GROQ_API_KEY)."""
    from langchain_groq import ChatGroq
    return ChatGroq(model=MODEL, temperature=0).bind_tools(TOOLS)


# ----------------------------------------------------------------------------
# Offline stand-in: scripts a real 3-tool sequence for one demo question, so the
# loop can be seen with no key. It is NOT an LLM -- it just replays fixed steps.
# ----------------------------------------------------------------------------
class OfflineDBModel:
    def invoke(self, messages):
        # Count how many tools have run so far to decide the next scripted step.
        tool_results = [m for m in messages if isinstance(m, ToolMessage)]
        n = len(tool_results)
        if n == 0:
            return AIMessage(content="", tool_calls=[
                {"name": "list_tables", "args": {}, "id": "c1"}])
        if n == 1:
            return AIMessage(content="", tool_calls=[
                {"name": "describe_table", "args": {"table_name": "customers"},
                 "id": "c2"}])
        if n == 2:
            return AIMessage(content="", tool_calls=[
                {"name": "run_sql_query",
                 "args": {"query": "SELECT COUNT(*) FROM customers WHERE city='Pune'"},
                 "id": "c3"}])
        count = tool_results[-1].content.splitlines()[-1]
        return AIMessage(
            content=f"There are {count} customers from Pune. "
                    f"(Offline stand-in: with a Groq key, a real model answers "
                    f"any question you type.)")


if __name__ == "__main__":
    if os.getenv("GROQ_API_KEY"):
        model = build_model()
        demo_questions = [
            "How many customers are from Pune?",
            "Which product category has the most products?",
            "What are our 3 most expensive products?",
        ]
        print("Using real Groq model.\n")
    else:
        model = OfflineDBModel()
        demo_questions = ["How many customers are from Pune?"]
        print("No GROQ_API_KEY -- using an OFFLINE stand-in to demo the loop.\n")

    for q in demo_questions:
        print(f"Q: {q}")
        print(f"A: {answer_question(model, q)}\n")
