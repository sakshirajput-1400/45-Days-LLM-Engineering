"""
app.py -- the Streamlit front-end for Chat With Your Database.  (STARTER -- TODOs)

Same brain (agent.answer_question), a web UI on top. It reuses everything from
Day 19/22: chat history in st.session_state, @st.cache_resource for the model,
st.chat_input / st.chat_message for the conversation. The new bit here is the
"How I got this" expander: we pass an on_tool callback so we can SHOW the exact
tools the agent used to reach each answer.

The setup (title, "database must exist" guard, sidebar schema, key guard, cached
model) is written for you. Your job is the two chat pieces marked TODO.

Setup:
    pip install streamlit langchain langchain-groq python-dotenv
    # put GROQ_API_KEY=... in a .env file in this folder
Run:
    python build_sample_db.py     # once, to create store.db
    streamlit run app.py
"""

import os
from dotenv import load_dotenv
import streamlit as st

import db
from agent import answer_question, build_model

load_dotenv()

st.set_page_config(page_title="Chat With Your Database", page_icon=":bar_chart:")
st.title(":bar_chart: Chat With Your Database")
st.caption("Ask questions in plain English. A Groq model writes and runs the SQL for you.")

# --- 1. The database must exist first (done) --------------------------------
if not os.path.exists(db.DB_PATH):
    st.error("store.db not found. Run `python build_sample_db.py` in this folder first.")
    st.stop()

# --- 2. Sidebar: show the schema so users know what they can ask (done) ------
with st.sidebar:
    st.header("Database")
    for table in db.list_tables():
        with st.expander(table):
            st.code(db.get_schema(table), language="text")
    st.caption("Read-only. The agent can only run SELECT queries.")

# --- 3. Need a key to actually chat (done) ----------------------------------
if not os.getenv("GROQ_API_KEY"):
    st.warning("Set GROQ_API_KEY in a .env file to chat. "
               "The schema on the left comes straight from the database (no key needed).")
    st.stop()


# --- 4. Build the model once and cache it (done) ----------------------------
@st.cache_resource
def get_model():
    return build_model()


model = get_model()

# --- 5. Conversation history lives in session_state (done) ------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Replay the history on every rerun (Streamlit reruns top-to-bottom each time).
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("steps"):
            with st.expander("How I got this (tool calls)"):
                for name, args, result in msg["steps"]:
                    st.markdown(f"**{name}**  `{args}`")
                    st.code(result, language="text")

# --- 6. Handle a new question -----------------------------------------------
# TODO: complete this block.
if question := st.chat_input("e.g. Which city has the most customers?"):
    # a) save + show the user's message:
    #      st.session_state.messages.append({"role": "user", "content": question})
    #      with st.chat_message("user"):
    #          st.markdown(question)
    #
    # b) get + show the assistant's answer inside a st.chat_message("assistant"):
    #      steps = []   # on_tool fills this so we can show the agent's work
    #      with st.spinner("Querying the database..."):
    #          answer = answer_question(
    #              model, question, verbose=False,
    #              on_tool=lambda n, a, r: steps.append((n, a, r)))
    #      st.markdown(answer)
    #      if steps:
    #          with st.expander("How I got this (tool calls)"):
    #              for name, args, result in steps:
    #                  st.markdown(f"**{name}**  `{args}`")
    #                  st.code(result, language="text")
    #
    # c) save the assistant turn (WITH its steps) so it survives the next rerun:
    #      st.session_state.messages.append(
    #          {"role": "assistant", "content": answer, "steps": steps})
    st.info("TODO: build the chat handler -- see the comments in app.py.")
