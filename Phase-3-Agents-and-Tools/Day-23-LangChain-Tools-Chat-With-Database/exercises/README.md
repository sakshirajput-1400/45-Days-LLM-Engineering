# Day 23 · Exercises

Two hands-on problems. The first drills the **tool mechanic** (Part A); the second extends the
**database agent** (Part B). Each has a stub with `# TODO`s and a worked `_solution.py`. Both run
**with no API key** — they use the same offline stand-in model idea you saw in the modules.

Run the real CPython (see repo `CLAUDE.md`):
```bash
python weather_tool.py         # your attempt
python weather_tool_solution.py
python count_rows.py
python count_rows_solution.py
```

---

## 1 · Build a tool and run the loop — `weather_tool.py`

Write a tool the model can call, then complete the tool-calling loop so it actually runs.

**Your job:**
1. Write a `@tool` `get_temperature(city: str) -> str` that looks a city up in the provided dict and
   returns its temperature (or a "not found" message). **Write a clear docstring** — that's what a
   real model would read.
2. Fill in the loop body: call the model, append its `AIMessage`, run each requested tool, and append
   a `ToolMessage` (quoting the `tool_call_id`) — until the model returns a final answer.

**Expected:** the offline stand-in asks for `get_temperature("Pune")`; your loop runs it and prints a
final answer containing the temperature.

*Skills: `@tool`, docstrings, `HumanMessage`/`AIMessage`/`ToolMessage`, the `while` loop.*

---

## 2 · Add a tool to the database agent — `count_rows.py`

The Chat-With-Your-Database agent has three tools. Add a fourth.

**Your job:**
1. Write a `@tool` `count_rows(table_name: str) -> str` that returns how many rows a table has. Use a
   parameterised query on the provided in-memory SQLite connection, and handle a bad table name by
   returning an error string (don't crash — the model should be able to read it and recover).
2. Register it in the `TOOL_MAP` so the loop can dispatch to it.

**Expected:** calling `count_rows.invoke({"table_name": "products"})` returns the count; a bad name
like `"nope"` returns a readable error, not a traceback.

*Skills: wrapping SQL as a tool, safe parameterised queries, returning errors as text.*

---

➡ Back to the [day overview](../README.md).
