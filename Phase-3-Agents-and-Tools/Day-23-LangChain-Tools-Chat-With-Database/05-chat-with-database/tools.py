"""
tools.py -- the three tools we hand to the model.

Each is a thin @tool wrapper around a db.py function. The DOCSTRINGS here are
important: they are the instructions the model reads to decide which tool to call
and when. We spell out the workflow (look up tables -> look up columns -> query)
right in the descriptions so the model follows it.

We also catch DatabaseError and return the message as text. That way a bad query
comes back to the model as a normal tool result ("SQL error: ...") which it can
READ and fix on the next loop -- instead of crashing the program.
"""

from langchain_core.tools import tool

import db  # our safe, model-free data layer


@tool
def list_tables() -> str:
    """List all tables in the database. Call this FIRST to see what data exists."""
    return ", ".join(db.list_tables())


@tool
def describe_table(table_name: str) -> str:
    """
    Show the columns and their types for one table. Call this BEFORE writing SQL
    so you use real column names. Pass a single table name from list_tables.
    """
    try:
        return db.get_schema(table_name)
    except db.DatabaseError as e:
        return str(e)


@tool
def run_sql_query(query: str) -> str:
    """
    Run a read-only SQL SELECT against the database and return the rows.
    Only a single SELECT is allowed (no INSERT/UPDATE/DELETE). Always check the
    schema with describe_table first so your column and table names are correct.
    """
    try:
        return db.run_query(query)
    except db.DatabaseError as e:
        return str(e)


# The list we bind to the model, plus a name -> tool map for the calling loop.
TOOLS = [list_tables, describe_table, run_sql_query]
TOOL_MAP = {t.name: t for t in TOOLS}


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
    print("a broken query comes back as text the model can read and fix ->")
    print(run_sql_query.invoke({"query": "SELECT * FROM nope"}))
