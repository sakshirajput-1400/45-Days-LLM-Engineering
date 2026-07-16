# 02 · Your first tool — the `@tool` decorator

In module 01 we hand-wrote a `{"name": ..., "args": ...}` request. LangChain automates all of that
with one decorator: **`@tool`**. Put it on a normal function and LangChain reads the function to build
a **schema** the model can understand — the name, what it does, and each argument's name and type.

```python
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the result."""
    return a * b
```

That's it. `multiply` is now a **tool object** with everything a model needs to call it.

## Two things the model reads — get them right

| Part of your function | Becomes | Why it matters |
|-----------------------|---------|----------------|
| the **function name** | the tool's `name` | how the model refers to it |
| the **docstring** | the tool's `description` | how the model decides *when* to use it |
| the **type hints** (`a: int`) | the argument schema | tells the model what to pass |

> **The docstring is not a comment — it's the instruction manual the model reads.** A vague docstring
> means the model calls the tool at the wrong time or with the wrong arguments. Write it for the model.

## Inspect and call the tool yourself

A tool is still callable — you invoke it with a **dict of arguments**:

```python
multiply.name          # 'multiply'
multiply.description   # 'Multiply two integers and return the result.'
multiply.args          # {'a': {'type': 'integer', ...}, 'b': {...}}
multiply.invoke({"a": 6, "b": 7})   # -> 42
```

Note `.invoke({...})` takes a **dictionary**, not positional arguments — because that's exactly the
shape a model sends back (a bag of named arguments). We're practising the real calling convention.

## Run it

```bash
python first_tool.py
```

No API key needed — this module only *defines and inspects* tools. Binding them to a live model is
the next step.

➡ Next: [`03-binding-tools/`](../03-binding-tools/README.md) — give these tools to a Groq model and
watch it choose one.
