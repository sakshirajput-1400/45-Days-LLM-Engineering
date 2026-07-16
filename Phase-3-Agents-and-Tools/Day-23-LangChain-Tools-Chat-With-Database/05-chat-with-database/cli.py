"""
cli.py -- chat with your database from the terminal.

A thin loop around agent.answer_question: read a question, print the answer,
repeat. Type 'quit' to exit. This is the same brain the Streamlit app uses.

Setup:
    pip install langchain langchain-groq python-dotenv
    # put GROQ_API_KEY=... in a .env file in this folder
Run:
    python build_sample_db.py   # once
    python cli.py
"""

import os
from dotenv import load_dotenv

from agent import answer_question, build_model, OfflineDBModel

load_dotenv()


def main():
    print("=" * 60)
    print("  Chat With Your Database  (type 'quit' to exit)")
    print("=" * 60)

    if not os.getenv("GROQ_API_KEY"):
        # No key: show the loop once with the offline stand-in, then explain.
        print("No GROQ_API_KEY found -- running ONE offline demo question.\n")
        model = OfflineDBModel()
        q = "How many customers are from Pune?"
        print(f"You: {q}")
        print(f"Bot: {answer_question(model, q, verbose=False)}\n")
        print("Add a free Groq key to a .env file to ask your own questions.")
        return

    model = build_model()
    print("Ask about customers, products, orders. e.g. "
          "'Which city has the most customers?'\n")
    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break
        if not question:
            continue
        if question.lower() in {"quit", "exit", "q"}:
            print("Bye!")
            break
        # verbose=True prints each tool call so students see the agent working.
        answer = answer_question(model, question, verbose=True)
        print(f"Bot: {answer}\n")


if __name__ == "__main__":
    main()
