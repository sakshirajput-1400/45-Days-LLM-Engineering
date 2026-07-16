"""
Exercise 1 - Build a tool and run the loop.  (STUB - finish the TODOs)

Write a @tool the model can call, then complete the tool-calling loop so it
actually runs the tool and produces a final answer. Runs with NO API key: an
offline stand-in model asks for the tool, exactly like module 04.

Run:
    python weather_tool.py
"""

from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

TEMPS = {"Pune": "31 C", "Mumbai": "33 C", "Delhi": "29 C"}


# TODO 1: Write a tool get_temperature(city: str) -> str.
#   - decorate it with @tool
#   - give it a clear docstring (the model reads this to decide when to call it)
#   - look the city up in TEMPS; if missing, return a helpful "not found" message
# @tool
# def get_temperature(city: str) -> str:
#     """..."""
#     ...


# Build the name -> tool map once you've written the tool.
# TOOL_MAP = {get_temperature.name: get_temperature}


def run_loop(model, question):
    """Drive model -> tool -> model until the model stops asking for tools."""
    messages = [HumanMessage(content=question)]
    while True:
        ai = model.invoke(messages)
        # TODO 2a: append the model's message (ai) to messages.

        # TODO 2b: if ai has no tool_calls, return ai.content (the final answer).

        # TODO 2c: for each call in ai.tool_calls:
        #   - look up the tool in TOOL_MAP by call["name"]
        #   - run it with .invoke(call["args"])
        #   - append a ToolMessage(content=str(result), tool_call_id=call["id"])
        raise NotImplementedError("Finish run_loop (remove this line).")


# --- Offline stand-in model: asks for the tool, then answers. Do not edit. ---
class OfflineModel:
    def invoke(self, messages):
        used = any(isinstance(m, ToolMessage) for m in messages)
        if not used:
            return AIMessage(content="", tool_calls=[
                {"name": "get_temperature", "args": {"city": "Pune"}, "id": "c1"}])
        result = [m for m in messages if isinstance(m, ToolMessage)][-1].content
        return AIMessage(content=f"It's currently {result} in Pune.")


if __name__ == "__main__":
    answer = run_loop(OfflineModel(), "What's the temperature in Pune?")
    print("Final answer:", answer)
