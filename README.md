# MIRA

> **MIRA = MCP Intelligent Routine Assistant**
>
> A personal AI assistant built to help you manage your day, keep track of tasks and notes, remember context over time, and evaluate how well the agent performs.

---

## What is MIRA?

MIRA is a full-stack productivity assistant that combines:

- a **FastAPI backend**
- a **React + Vite frontend**
- **Google integrations** for Calendar, Tasks, Gmail, and authentication
- **long-term memory** using embeddings and Pinecone
- a **LangGraph-based agent** that plans, reasons, acts, and responds
- an **evaluation framework** for measuring tool use, retrieval quality, groundedness, and latency

It is designed to behave more like an intelligent routine companion than a simple chatbot. You can chat with it, manage your schedule, store notes, inspect traces, and review evaluation metrics — the assistant remembers important context automatically behind the scenes.

---

## At a Glance

| Area | What it does |
|---|---|
| Chat | Conversational assistant with agent reasoning and tool use |
| Calendar | View and manage schedule data |
| Tasks | Track and organize Google Tasks |
| Notes | Save and retrieve personal notes |
| Habits | Track recurring habits |
| Trace | Inspect agent execution steps |
| Evaluation | Review benchmark and quality metrics |

---

## Visual Overview

```text
Browser
  ↓
React SPA (Vite + Tailwind)
  ↓ /api
FastAPI backend
  ├─ Auth + routers
  ├─ LangGraph agent runner
  ├─ Google MCP clients
  ├─ RAG memory + Pinecone
  ├─ PostgreSQL database
  └─ Evaluation pipeline
```

### Core flow

1. You send a message from the frontend.
2. The backend authenticates the request and starts an agent run.
3. The agent classifies intent, fetches relevant data, checks memory, and plans actions.
4. Results are stored, traced, and returned to the UI.
5. Conversation context is embedded for future recall.

---

## Key Features

- **Natural language chat** for planning and routine help
- **Google Calendar / Tasks / Gmail integration**
- **Automatic long-term memory** — remembers context without manual input
- **Agent trace viewer** for debugging and transparency
- **Evaluation dashboard** for measuring agent quality
- **Habit and notes support**
- **Fast local frontend development** with Vite
- **Docker support** for running the full stack

---

## Tech Stack

### Backend

- Python 3.11
- FastAPI
- LangGraph
- SQLAlchemy + asyncpg
- Alembic
- Pinecone
- sentence-transformers
- Mistral AI

### Frontend

- React 18
- TypeScript
- Vite
- Tailwind CSS
- React Router
- Axios

---

## Project Structure

```text
.
├─ backend/        # API, agent graph, memory, database, evaluation
├─ frontend/       # React app
├─ docs/           # Architecture, setup, API, evaluation docs
├─ tests/          # Unit tests
├─ run.py          # Local backend launcher
├─ docker-compose.yml
└─ README.md
```

---

## Prerequisites

- Python 3.11+
- Node.js 18+ recommended
- `pip`
- `npm`
- A PostgreSQL database
- Pinecone account and API key
- Google Cloud OAuth credentials
- Mistral API key

---

## Setup

### 1) Create environment variables

Copy `.env.example` to `.env` in the project root and fill in the required values.

Required variables include:

- `MISTRAL_API_KEY`
- `DATABASE_URL`
- `PINECONE_API_KEY`
- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `SECRET_KEY`

Optional but commonly used:

- `MISTRAL_MODEL`
- `MISTRAL_LIGHT_MODEL`
- `PERSIST_SCHEDULE_TO_CALENDAR`
- `PINECONE_INDEX_NAME`
- `PINECONE_ENVIRONMENT`
- `GOOGLE_REDIRECT_URI`
- `FRONTEND_URL`
- `VITE_API_BASE_URL`
- `ENVIRONMENT`
- `LOG_LEVEL`
- `ACCESS_TOKEN_EXPIRE_MINUTES`

For Google OAuth details, see [GOOGLE_OAUTH_SETUP.md](GOOGLE_OAUTH_SETUP.md).

---

## Run Locally

### Backend

From the project root:

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
```

You can also use:

```bash
python run.py
```

### Frontend

In a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend development server:

- `http://localhost:5173`

Backend API:

- `http://localhost:8000`
- API docs: `http://localhost:8000/docs`

---

## Docker

Run the full stack with:

```bash
docker compose up --build
```

This starts the backend and frontend services together.

---

## Testing

```bash
python -m pytest tests -q
```

You can also run additional checks:

```bash
python -m compileall backend
cd frontend
npx tsc --noEmit
```

---

## Documentation

- [Architecture](docs/architecture.md)
- [Agent Graph](docs/agent-graph.md)
- [API Reference](docs/api-reference.md)
- [Database](docs/database.md)
- [RAG Memory](docs/rag-memory.md)
- [Evaluation](docs/evaluation.md)
- [Frontend](docs/frontend.md)
- [Setup & Security](docs/setup-and-security.md)

---

## Notes

- The backend auto-creates tables on startup in development.
- First startup may take longer because the embedding model needs to load.
- Google access tokens are refreshed server-side when needed.

---

## License

No license file is currently included. Add one if you plan to share or distribute the project.
