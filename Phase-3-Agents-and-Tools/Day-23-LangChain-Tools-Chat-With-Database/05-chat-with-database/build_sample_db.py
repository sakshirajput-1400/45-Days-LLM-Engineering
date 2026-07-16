"""
Build the sample database for the "Chat With Your Database" project.

Creates `store.db` -- a small but realistic SQLite database for a fictional
Indian online store, with FOUR linked tables and lots of rows:

    customers   (150 rows)  who bought
    products    ( 40 rows)  what we sell
    orders      (~900 rows) each purchase
    order_items (~2700 rows)the lines inside each order

The data is generated with a FIXED random seed, so everyone gets the exact same
database -- your queries and the model's answers are reproducible.

Run this ONCE before using the chat app:
    python build_sample_db.py

Re-running rebuilds the database from scratch (drops and recreates the tables).
No API key needed -- this is pure Python + the sqlite3 module (standard library).
"""

import os
import random
import sqlite3
from datetime import date, timedelta

random.seed(42)  # fixed seed -> the same database every time

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "store.db")

# ----------------------------------------------------------------------------
# Source data to sample from (India-context, so the numbers feel real).
# ----------------------------------------------------------------------------
FIRST_NAMES = ["Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh",
               "Ayaan", "Krishna", "Ishaan", "Ananya", "Diya", "Aadhya", "Saanvi",
               "Pari", "Anika", "Navya", "Myra", "Kiara", "Riya", "Rohan", "Kabir",
               "Neha", "Priya", "Rahul", "Sneha", "Amit", "Pooja", "Vikram", "Meera"]
LAST_NAMES = ["Sharma", "Verma", "Patel", "Gupta", "Reddy", "Nair", "Iyer", "Singh",
              "Kumar", "Das", "Mehta", "Joshi", "Rao", "Chopra", "Bose", "Ghosh"]

# (city, state) pairs -- weighted by list length toward the big metros.
CITIES = [("Mumbai", "Maharashtra"), ("Pune", "Maharashtra"), ("Delhi", "Delhi"),
          ("Bengaluru", "Karnataka"), ("Hyderabad", "Telangana"),
          ("Chennai", "Tamil Nadu"), ("Kolkata", "West Bengal"),
          ("Ahmedabad", "Gujarat"), ("Jaipur", "Rajasthan"), ("Lucknow", "Uttar Pradesh"),
          ("Mumbai", "Maharashtra"), ("Bengaluru", "Karnataka"), ("Delhi", "Delhi")]

# (product name, category, price in rupees)
PRODUCTS = [
    ("Wireless Mouse", "Electronics", 699), ("Mechanical Keyboard", "Electronics", 2499),
    ("USB-C Cable", "Electronics", 299), ("Bluetooth Earbuds", "Electronics", 1999),
    ("Power Bank 10000mAh", "Electronics", 1299), ("Laptop Stand", "Electronics", 899),
    ("Webcam HD", "Electronics", 1599), ("Phone Case", "Electronics", 399),
    ("Python Crash Course", "Books", 549), ("Clean Code", "Books", 699),
    ("The Alchemist", "Books", 299), ("Atomic Habits", "Books", 499),
    ("Sapiens", "Books", 599), ("Rich Dad Poor Dad", "Books", 349),
    ("Cotton T-Shirt", "Clothing", 499), ("Denim Jeans", "Clothing", 1299),
    ("Running Shoes", "Clothing", 2199), ("Hoodie", "Clothing", 999),
    ("Formal Shirt", "Clothing", 899), ("Woolen Socks (3 pack)", "Clothing", 299),
    ("Steel Water Bottle", "Home", 449), ("Ceramic Mug", "Home", 249),
    ("Desk Lamp", "Home", 799), ("Bed Sheet Set", "Home", 1099),
    ("Wall Clock", "Home", 599), ("Storage Box", "Home", 349),
    ("Yoga Mat", "Sports", 799), ("Dumbbell 5kg", "Sports", 899),
    ("Cricket Bat", "Sports", 1499), ("Football", "Sports", 699),
    ("Skipping Rope", "Sports", 199), ("Badminton Racket", "Sports", 1099),
    ("Green Tea (100 bags)", "Grocery", 399), ("Coffee Beans 500g", "Grocery", 649),
    ("Almonds 500g", "Grocery", 549), ("Honey 1kg", "Grocery", 449),
    ("Olive Oil 1L", "Grocery", 799), ("Dark Chocolate", "Grocery", 199),
    ("Protein Bar (box)", "Grocery", 899), ("Masala Chai Mix", "Grocery", 249),
]

STATUSES = ["Delivered", "Delivered", "Delivered", "Shipped", "Processing", "Cancelled"]


def build():
    # Fresh start: delete any old database file so re-runs are clean.
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # --- schema -------------------------------------------------------------
    cur.executescript("""
        CREATE TABLE customers (
            customer_id INTEGER PRIMARY KEY,
            name        TEXT NOT NULL,
            city        TEXT NOT NULL,
            state       TEXT NOT NULL,
            signup_date TEXT NOT NULL
        );
        CREATE TABLE products (
            product_id INTEGER PRIMARY KEY,
            name       TEXT NOT NULL,
            category   TEXT NOT NULL,
            price      REAL NOT NULL
        );
        CREATE TABLE orders (
            order_id    INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL REFERENCES customers(customer_id),
            order_date  TEXT NOT NULL,
            status      TEXT NOT NULL
        );
        CREATE TABLE order_items (
            item_id    INTEGER PRIMARY KEY,
            order_id   INTEGER NOT NULL REFERENCES orders(order_id),
            product_id INTEGER NOT NULL REFERENCES products(product_id),
            quantity   INTEGER NOT NULL,
            unit_price REAL NOT NULL
        );
    """)

    # --- products (fixed list) ---------------------------------------------
    for pid, (name, cat, price) in enumerate(PRODUCTS, start=1):
        cur.execute("INSERT INTO products VALUES (?, ?, ?, ?)", (pid, name, cat, price))

    # --- customers (150, sampled) ------------------------------------------
    start = date(2023, 1, 1)
    for cid in range(1, 151):
        name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
        city, state = random.choice(CITIES)
        signup = start + timedelta(days=random.randint(0, 900))
        cur.execute("INSERT INTO customers VALUES (?, ?, ?, ?, ?)",
                    (cid, name, city, state, signup.isoformat()))

    # --- orders + their line items -----------------------------------------
    order_id = 0
    item_id = 0
    order_start = date(2024, 1, 1)
    for _ in range(900):
        order_id += 1
        customer_id = random.randint(1, 150)
        order_date = order_start + timedelta(days=random.randint(0, 550))
        status = random.choice(STATUSES)
        cur.execute("INSERT INTO orders VALUES (?, ?, ?, ?)",
                    (order_id, customer_id, order_date.isoformat(), status))

        # 1 to 5 distinct products per order.
        for pid in random.sample(range(1, len(PRODUCTS) + 1), random.randint(1, 5)):
            item_id += 1
            qty = random.randint(1, 4)
            unit_price = PRODUCTS[pid - 1][2]      # snapshot price at order time
            cur.execute("INSERT INTO order_items VALUES (?, ?, ?, ?, ?)",
                        (item_id, order_id, pid, qty, unit_price))

    conn.commit()

    # --- report -------------------------------------------------------------
    counts = {t: cur.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
              for t in ("customers", "products", "orders", "order_items")}
    conn.close()

    print(f"Built {DB_PATH}")
    for table, n in counts.items():
        print(f"  {table:12} {n:>5} rows")
    print("\nReady. Now try:  python cli.py   (chat)   or   streamlit run app.py")


if __name__ == "__main__":
    build()
