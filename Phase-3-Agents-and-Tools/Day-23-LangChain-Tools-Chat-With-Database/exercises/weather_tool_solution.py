"""
Exercise 1 - Build a tool and run the loop.  (SOLUTION)

Run:
    python weather_tool_solution.py
"""

from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

TEMPS = {"Pune": "31 C", "Mumbai": "33 C", "Delhi": "29 C"}


@tool
def get_temperature(city: str) -> str:
    """Return the current temperature for a given city name."""
    if city in TEMPS:
        return TEMPS[city]
    return f"No temperature on record for {city!r}."


TOOL_MAP = {get_temperature.name: get_temperature}


def run_loop(model, question):
    """Drive model -> tool -> model until the model stops asking for tools."""
    messages = [HumanMessage(content=question)]
    while True:
        ai = model.invoke(messages)
        messages.append(ai)                       # 2a

        if not ai.tool_calls:                     # 2b: final answer
            return ai.content

        for call in ai.tool_calls:                # 2c: run each requested tool
            result = TOOL_MAP[call["name"]].invoke(call["args"])
            messages.append(ToolMessage(content=str(result),
                                        tool_call_id=call["id"]))


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
    # Prove the tool itself works, too:
    print("Direct call:", get_temperature.invoke({"city": "Delhi"}))
    print("Unknown city:", get_temperature.invoke({"city": "Nowhere"}))
