"""
db.py -- the safe data-access layer for the Chat-With-Your-Database project.

This file knows how to talk to store.db and NOTHING about the LLM. Keeping it
separate means we can test the database logic on its own (no key, no model), and
the tools in tools.py just wrap these functions.

Three jobs, all READ-ONLY:
  list_tables()          -> table names
  get_schema(table)      -> columns + types for one table
  run_query(sql)         -> rows for a SELECT (and ONLY a SELECT)

Safety matters: we're about to let a language model send SQL. We take two
precautions so it can never damage the data:
  1. Open the database in read-only mode (mode=ro) -- writes fail at the driver.
  2. Reject any statement that isn't a single SELECT before we even run it.
"""

import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "store.db")

# A generous cap so a careless "SELECT * FROM order_items" can't flood the model
# (or your screen) with thousands of rows.
MAX_ROWS = 50


class DatabaseError(Exception):
    """Raised for a missing database or a rejected/invalid query."""


def _connect():
    """Open store.db READ-ONLY. Any write attempt will raise, by design."""
    if not os.path.exists(DB_PATH):
        raise DatabaseError(
            "store.db not found. Run `python build_sample_db.py` first.")
    # The file: URI with mode=ro makes the whole connection read-only.
    return sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)


def list_tables() -> list[str]:
    """Return the names of the tables in the database."""
    conn = _connect()
    try:
        rows = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        ).fetchall()
        return [r[0] for r in rows]
    finally:
        conn.close()


def get_schema(table: str) -> str:
    """Return a human-readable column list for one table (name + type)."""
    if table not in list_tables():
        raise DatabaseError(f"No such table: {table!r}. "
                            f"Tables are: {', '.join(list_tables())}")
    conn = _connect()
    try:
        # PRAGMA table_info returns one row per column: (cid, name, type, ...).
        cols = conn.execute(f"PRAGMA table_info({table})").fetchall()
        lines = [f"  {c[1]} ({c[2]})" for c in cols]
        return f"Table {table}:\n" + "\n".join(lines)
    finally:
        conn.close()


def _is_safe_select(sql: str) -> bool:
    """
    Allow exactly one read-only SELECT. Block writes, PRAGMAs, and statement
    stacking (the classic 'SELECT ...; DROP TABLE ...' trick).
    """
    stripped = sql.strip().rstrip(";").strip()
    if ";" in stripped:                     # more than one statement
        return False
    lowered = stripped.lower()
    if not (lowered.startswith("select") or lowered.startswith("with")):
        return False
    # Belt and braces: reject obvious write keywords anywhere in the text.
    banned = ("insert", "update", "delete", "drop", "alter", "create",
              "replace", "attach", "pragma")
    return not any(f" {word} " in f" {lowered} " for word in banned)


def run_query(sql: str) -> str:
    """
    Run a single read-only SELECT and return the rows as readable text
    (header + up to MAX_ROWS rows). Raises DatabaseError on anything unsafe.
    """
    if not _is_safe_select(sql):
        raise DatabaseError(
            "Only a single read-only SELECT statement is allowed.")
    conn = _connect()
    try:
        cur = conn.execute(sql)
        columns = [d[0] for d in cur.description]
        rows = cur.fetchmany(MAX_ROWS + 1)   # grab one extra to detect truncation
    except sqlite3.Error as e:
        raise DatabaseError(f"SQL error: {e}")
    finally:
        conn.close()

    if not rows:
        return "(no rows)"

    truncated = len(rows) > MAX_ROWS
    rows = rows[:MAX_ROWS]
    header = " | ".join(columns)
    body = "\n".join(" | ".join(str(v) for v in row) for row in rows)
    note = f"\n... (showing first {MAX_ROWS} rows)" if truncated else ""
    return f"{header}\n{body}{note}"


# Quick self-test: `python db.py` exercises the layer with NO model and NO key.
if __name__ == "__main__":
    print("Tables:", list_tables(), "\n")
    print(get_schema("orders"), "\n")
    print("Top 3 products by price:")
    print(run_query(
        "SELECT name, price FROM products ORDER BY price DESC LIMIT 3"), "\n")
    print("Blocking a write attempt:")
    try:
        run_query("DELETE FROM customers")
    except DatabaseError as e:
        print("  rejected ->", e)
