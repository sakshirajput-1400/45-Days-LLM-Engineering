"""
Exercise 2 - Add a tool to the database agent.  (STUB - finish the TODOs)

The project's agent had three DB tools. Here you add a fourth: count_rows. This
file is self-contained -- it builds a tiny in-memory SQLite database so you can
test your tool with no API key and no store.db.

Run:
    python count_rows.py
"""

import sqlite3
from langchain_core.tools import tool

# A tiny in-memory database (built fresh each run) so this exercise stands alone.
conn = sqlite3.connect(":memory:")
conn.executescript("""
    CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL);
    CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT);
    INSERT INTO products (name, price) VALUES ('Mouse', 699), ('Keyboard', 2499), ('Cable', 299);
    INSERT INTO customers (name) VALUES ('Aarav'), ('Diya');
""")


def table_exists(name: str) -> bool:
    row = conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)
    ).fetchone()
    return row is not None


# TODO 1: Write a tool count_rows(table_name: str) -> str.
#   - decorate with @tool and write a docstring describing what it does
#   - if table_exists(table_name) is False, return a readable error string
#     (do NOT raise -- the model should be able to read it and recover)
#   - otherwise run "SELECT COUNT(*) FROM <table>" and return the count as text
#   - NOTE: table names can't be bound as ? parameters, so validate with
#     table_exists FIRST, then it's safe to format the name into the query.
# @tool
# def count_rows(table_name: str) -> str:
#     """..."""
#     ...


# TODO 2: register your tool so a loop could dispatch to it by name.
# TOOL_MAP = {count_rows.name: count_rows}


if __name__ == "__main__":
    # These calls should work once you've written the tool:
    print("products ->", count_rows.invoke({"table_name": "products"}))
    print("customers ->", count_rows.invoke({"table_name": "customers"}))
    print("bad name ->", count_rows.invoke({"table_name": "nope"}))
