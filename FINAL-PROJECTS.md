# Final Project Ideas — SSAI-101

**15 Streamlit-based capstone projects** for the 46-day AI Development Summer Training.

Every project here is:
- **Streamlit-based** — a real web UI students can demo live and share as a link.
- **Free-tier only** — Groq (`llama-3.1-8b-instant`) for generation + local
  `sentence-transformers` / `HuggingFaceEmbeddings` for retrieval. No paid API keys required.
- **Deployable free** on [Streamlit Community Cloud](https://streamlit.io/cloud) — students get a
  shareable live URL for their resume/portfolio.
- **Mapped to the course** — built only from skills taught across Days 1–25+ (Python → Groq → prompt
  engineering → embeddings → semantic search → RAG → LangChain → LangGraph → agents & tools → memory).

> **How to read each card:** *Teaches* = the core concepts it exercises · *Wow* = the moment that
> lands in a live demo.

---

## Tier 1 — RAG & Document Intelligence
*Skills from Days 16–22 (embeddings, semantic search, RAG, LangChain).*

### 1. Chat With Your Documents (Pro)
Upload PDFs/DOCX/TXT → chunk → embed → retrieve → grounded answers with a **"Sources used"**
citation panel. The Day-20 mini-project, leveled up with multi-file support, model/temperature
controls, and a chat-history sidebar.
- **Teaches:** full RAG pipeline · file handling · citations
- **Wow:** ask a question about a 40-page PDF and get a cited, grounded answer

### 2. Chat With a Website / YouTube Video
Paste a URL (or YouTube transcript) → scrape/clean text → RAG over it. The source is live and
relatable, which makes for a strong demo.
- **Teaches:** RAG + real-world ingestion
- **Wow:** "summarize this blog and let me ask follow-ups"

### 3. Study Buddy / Exam-Prep Assistant
Upload lecture notes/textbook chapters → generate **flashcards, MCQ quizzes, and a summary**, then
chat with the material. Directly relatable to the student audience.
- **Teaches:** RAG + structured output (Pydantic / `with_structured_output`)
- **Wow:** an auto-generated quiz from their own notes

### 4. Resume vs Job-Description Matcher
Paste a resume + a JD → semantic similarity score, missing-keywords gap analysis, and AI-rewritten
bullet points. Ties directly into the **Career Launchpad** track.
- **Teaches:** embeddings / cosine similarity · prompt engineering
- **Wow:** an ATS-style match % with actionable fixes

### 5. Legal / Policy Document Explainer
Upload a rental agreement, insurance policy, or terms-of-service → plain-English explanation +
"ask about clause X" + red-flag detection.
- **Teaches:** grounded RAG + system-prompt design
- **Wow:** "explain this clause like I'm 15"

---

## Tier 2 — Chatbots, Memory & Personas
*Skills from Days 16, 19, 21–23 (chat loops, session state, memory, LCEL).*

### 6. Multi-Persona AI Chatbot
One app, switchable personas (strict professor, startup mentor, coding tutor, motivational coach)
with **conversation memory** and streaming responses.
- **Teaches:** system prompts · session state · memory
- **Wow:** same question, radically different personalities

### 7. Customer-Support Bot for a Fake Business
RAG over an FAQ/policy doc + memory + an "escalate to human" fallback when confidence is low
(the confidence-threshold trick from Day 18).
- **Teaches:** RAG + graceful "I don't know" handling
- **Wow:** a realistic product demo worth a portfolio slot

### 8. Language Learning / Translation Tutor
Chat in Hindi/English, get corrections, translations, and vocabulary explanations. Built on
LangChain LCEL chains + `batch`.
- **Teaches:** LCEL chains · prompt templates
- **Wow:** real-time bilingual conversation practice

---

## Tier 3 — Agents, Tools & LangGraph
*Skills from Days 21–25+ (LangGraph, `@tool`, `bind_tools`, routing, agent loops).*

### 9. Research Assistant Agent
A LangGraph agent that takes a topic → searches/reads sources → synthesizes a cited mini-report,
with the **Think → Act → Observe** loop visible in the UI.
- **Teaches:** LangGraph · tools · agent loops
- **Wow:** watch the agent "reason" step by step on screen

### 10. AI Data Analyst ("Chat With Your CSV")
Upload a CSV → ask questions in English → the agent writes/runs pandas → returns answers **and
charts** (`st.dataframe`, `st.bar_chart`).
- **Teaches:** tool use · agents · Streamlit data viz
- **Wow:** "which month had the highest sales?" → instant chart

### 11. Multi-Tool Personal Assistant
An agent with tools: calculator, unit converter, dictionary, "current date," and a notes store.
A router decides which tool to call (Day-23 conditional edges).
- **Teaches:** `@tool` · `bind_tools` · routing
- **Wow:** one chatbox that intelligently picks the right tool

### 12. Smart Support-Ticket Router
Paste a customer complaint → LangGraph classifies it (billing/technical/refund) → routes to the
right handler → drafts a reply. The Day-23 exercise, productized.
- **Teaches:** conditional edges · classification
- **Wow:** a clean state-machine visualization

---

## Tier 4 — Creative & Utility Apps
*Skills usable from any day (prompt engineering, templates, Streamlit layout, streaming).*

### 13. AI Content Studio
One dashboard to generate LinkedIn posts, tweets, cold emails, and blog outlines from a topic —
with tone controls. Pairs perfectly with the "build content" career thesis.
- **Teaches:** prompt engineering · templates · Streamlit layout (tabs/columns)
- **Wow:** pick tone + platform → a polished, ready-to-post draft

### 14. Code Explainer & Reviewer
Paste code → get a line-by-line explanation, bug spotting, and improvement suggestions.
Optionally RAG over docs.
- **Teaches:** prompt engineering · streaming output
- **Wow:** highly relatable for a coding cohort

### 15. Personal Knowledge Base ("Second Brain")
Save notes/links over time → semantic search + chat across everything you've saved (persistent
Chroma). Grows more useful the more it is used.
- **Teaches:** persistent vector store · semantic search + RAG
- **Wow:** "what did I save about transformers last month?"

---

## Choosing a project

| Goal | Best picks |
|------|-----------|
| **Easiest to ship** (Days 16–22 skills only) | #1, #3, #6, #13 |
| **Most impressive** (agents track, Days 23–25) | #9, #10, #11 |
| **Best career-portfolio value** | #4, #7, #10, #13 |
| **Most relatable to students** | #3, #4, #14 |

## What every project should include (rubric)

1. A working **Streamlit UI** with sensible layout (sidebar controls, chat or tabs).
2. A **Groq**-powered generation step (streaming where it makes sense).
3. Graceful handling of a **missing API key** (`st.stop()` + a clear message).
4. A short **README** with what it does, how to run it, and a screenshot/GIF.
5. **Deployed free** on Streamlit Community Cloud — submit the live link.
6. A **2–3 minute demo script** for the final presentation.

## Tech stack (all free)

- **UI:** `streamlit`
- **LLM:** `groq` — `llama-3.1-8b-instant`
- **Embeddings / retrieval:** `sentence-transformers` / `langchain-huggingface` (`all-MiniLM-L6-v2`)
- **Vector store:** `chromadb` / `langchain-chroma`
- **Orchestration (Tier 3):** `langchain`, `langgraph`
- **Config:** `python-dotenv`
