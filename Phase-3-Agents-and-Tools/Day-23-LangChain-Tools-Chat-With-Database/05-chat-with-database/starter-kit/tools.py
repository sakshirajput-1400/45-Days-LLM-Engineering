"""
tools.py -- the three tools we hand to the model.  (STARTER -- finish the TODOs)

`db.py` already knows how to talk to the database safely. Your job here is to
WRAP each of its functions in an @tool so a language model can call it.

Remember from modules 02-03:
  - @tool turns a plain function into something the model can call.
  - The tool's NAME comes from the function name.
  - The tool's DESCRIPTION (what the model reads to decide when to use it) comes
    from the DOCSTRING -- so write clear docstrings that spell out the workflow.
  - The tool's ARGS come from the parameters + type hints.

One more trick: catch db.DatabaseError and RETURN the message as text (don't let
it raise). A bad query then comes back to the model as a normal tool result it
can read and fix on the next loop -- errors become feedback, not crashes.

Run this file directly to test your tools with NO model and NO key:
    python build_sample_db.py   # once, to create store.db
    python tools.py
"""

from langchain_core.tools import tool

import db  # our safe, model-free data layer (already written for you)


# TODO 1: list_tables
#   Write an @tool named list_tables that takes no arguments and returns the
#   table names as one comma-separated string. Docstring should tell the model
#   to call this FIRST to see what data exists.
#   Hint: db.list_tables() returns a list of names.
#
# @tool
# def list_tables() -> str:
#     """..."""
#     return ...


# TODO 2: describe_table
#   Write an @tool named describe_table(table_name: str) -> str that returns the
#   columns + types for one table (use db.get_schema). Docstring should tell the
#   model to call this BEFORE writing SQL so it uses real column names.
#   Wrap the call in try/except db.DatabaseError and RETURN str(e) on error.
#
# @tool
# def describe_table(table_name: str) -> str:
#     """..."""
#     try:
#         return ...
#     except db.DatabaseError as e:
#         return str(e)


# TODO 3: run_sql_query
#   Write an @tool named run_sql_query(query: str) -> str that runs a read-only
#   SELECT (use db.run_query) and returns the rows. Docstring should say: only a
#   single SELECT is allowed, and to check the schema with describe_table first.
#   Again, catch db.DatabaseError and return str(e).
#
# @tool
# def run_sql_query(query: str) -> str:
#     """..."""
#     ...


# TODO 4: collect your tools for the agent.
#   The agent will need (a) a list to bind to the model, and (b) a name->tool map
#   so the loop can look up a tool by the name the model asked for.
# TOOLS = [list_tables, describe_table, run_sql_query]
# TOOL_MAP = {t.name: t for t in TOOLS}


# `python tools.py` exercises the tools directly -- no model, no key needed.
if __name__ == "__main__":
    print("list_tables ->", list_tables.invoke({}))
    print()
    print("describe_table('products') ->")
    print(describe_table.invoke({"table_name": "products"}))
    print()
    print("run_sql_query(...) ->")
    print(run_sql_query.invoke(
        {"query": "SELECT category, COUNT(*) AS n FROM products GROUP BY category"}))
    print()
    print("a broken query should come back as text (not crash) ->")
    print(run_sql_query.invoke({"query": "SELECT * FROM nope"}))
