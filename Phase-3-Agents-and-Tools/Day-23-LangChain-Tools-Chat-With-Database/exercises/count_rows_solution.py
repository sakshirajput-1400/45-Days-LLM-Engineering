"""
Exercise 2 - Add a tool to the database agent.  (SOLUTION)

Run:
    python count_rows_solution.py
"""

import sqlite3
from langchain_core.tools import tool

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


@tool
def count_rows(table_name: str) -> str:
    """Return how many rows are in the given table. Use to count records."""
    # Validate FIRST -- a table name can't be a ? parameter, so we must be sure
    # it's a real table before formatting it into the SQL (blocks injection).
    if not table_exists(table_name):
        return f"No such table: {table_name!r}."
    n = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
    return f"{table_name} has {n} rows."


TOOL_MAP = {count_rows.name: count_rows}


if __name__ == "__main__":
    print("products ->", count_rows.invoke({"table_name": "products"}))
    print("customers ->", count_rows.invoke({"table_name": "customers"}))
    print("bad name ->", count_rows.invoke({"table_name": "nope"}))
