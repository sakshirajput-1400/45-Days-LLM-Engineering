"""
02 - Your first tool: the @tool decorator.

@tool turns an ordinary function into a "tool object" a model can understand. It
reads three things from your function:
  - the NAME        -> how the model refers to the tool
  - the DOCSTRING   -> how the model decides WHEN to use it
  - the TYPE HINTS  -> what arguments to pass, and their types

No API key needed: here we only DEFINE and INSPECT tools, and call them by hand
using the same dict-of-arguments convention a real model uses.

Setup:
    pip install langchain-core
Run:
    python first_tool.py
"""

from langchain_core.tools import tool


# ----------------------------------------------------------------------------
# 1. Define a tool. The docstring is written FOR THE MODEL, not for humans.
# ----------------------------------------------------------------------------
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the exact result."""
    return a * b


@tool
def word_count(text: str) -> int:
    """Count how many words are in a piece of text. Use for length questions."""
    return len(text.split())


# ----------------------------------------------------------------------------
# 2. Inspect what LangChain built. THIS is what the model gets to see.
# ----------------------------------------------------------------------------
print("=" * 60)
print("What the model sees about each tool")
print("=" * 60)
for t in (multiply, word_count):
    print(f"name        : {t.name}")
    print(f"description : {t.description}")
    print(f"args        : {t.args}")
    print("-" * 60)

# ----------------------------------------------------------------------------
# 3. Call a tool the way a model would: .invoke(<dict of arguments>).
# ----------------------------------------------------------------------------
# A model never passes positional args -- it sends a bag of NAMED arguments.
# So tools are invoked with a dict. We mimic that exactly.
print("\nCalling tools by hand (dict of arguments, just like a model sends):")
print("  multiply.invoke({'a': 6, 'b': 7}) =", multiply.invoke({"a": 6, "b": 7}))
print("  word_count.invoke({'text': 'tools let models act'}) =",
      word_count.invoke({"text": "tools let models act"}))

# ----------------------------------------------------------------------------
# 4. The tool is still a real object -- prove the underlying function runs.
# ----------------------------------------------------------------------------
print("\nUnder the hood it's still your function -- exact, not guessed:")
print("  48973 * 215 =", multiply.invoke({"a": 48973, "b": 215}))

print("\nNext: hand these tools to a real model with .bind_tools([...]) and let")
print("the model pick which one to call.")
