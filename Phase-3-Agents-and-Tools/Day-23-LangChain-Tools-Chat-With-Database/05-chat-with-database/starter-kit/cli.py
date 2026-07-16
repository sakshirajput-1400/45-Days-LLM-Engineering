"""
cli.py -- chat with your database from the terminal.  (STARTER -- finish the TODOs)

Once answer_question() works in agent.py, the CLI is a thin loop around it: read
a question, print the answer, repeat. This is the same brain the Streamlit app
uses -- the UI is just a wrapper.

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

    # No key? Show the loop once with the offline stand-in, then explain. (Done.)
    if not os.getenv("GROQ_API_KEY"):
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

    # TODO: the chat loop. Repeat forever:
    #   1. question = input("You: ").strip()
    #      (wrap input() in try/except (EOFError, KeyboardInterrupt) to exit cleanly)
    #   2. if the question is empty, continue
    #   3. if question.lower() in {"quit", "exit", "q"}: print "Bye!" and break
    #   4. answer = answer_question(model, question, verbose=True)
    #      (verbose=True prints each tool call so you SEE the agent working)
    #   5. print(f"Bot: {answer}\n")
    raise NotImplementedError("Write the chat loop above.")


if __name__ == "__main__":
    main()
