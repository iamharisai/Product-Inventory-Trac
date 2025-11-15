# FastAPI + React Project

A minimal FastAPI backend with a React frontend. This repository contains a Python FastAPI app (backend) and a React app under the `frontend/` directory.

## Prerequisites
- Python 3.10+ (or compatible)
- Node.js 22+ and npm (for the frontend)
- Git (optional)

## Backend (FastAPI) — Setup & Run
1. (Optional) Create a virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install Python dependencies.

```bash
pip install -r requirements.txt
```

3. Run the development server:

```bash
# from project root
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at `http://127.0.0.1:8000`. Open `http://127.0.0.1:8000/docs` for automatic Swagger UI.

## Frontend (React) — Setup & Run
1. Change into the frontend folder and install dependencies:

```bash
cd frontend
npm install
```

2. Start the development server:

```bash
npm start
```

By default the React app runs at `http://localhost:3000`. The frontend expects the backend API to be available (adjust proxy or API base URL in `src` as needed).

## Database (postgresql)
Keep your database username and password as variables DB_USER and DB_PASS in .env file

## Project Structure (important files)
- `main.py` — FastAPI application entrypoint
- `database.py`, `database_models.py`, `models.py` — DB and data models
- `frontend/` — React app (create-react-app style)
  - `frontend/package.json` — frontend scripts & deps
  - `frontend/src/` — frontend source files

## Notes
- If your project uses environment variables (DB connection, secrets), create a `.env` and load them in `main.py` or via your preferred method.
- If you plan to persist data, ensure the database is configured.

## Quick commands recap

```bash
# Backend
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm start
```

### Sample snap of frontend
![The sample snap of frontend](https://iamharisai.in/wp-content/uploads/2025/11/Screenshot-2025-11-15-at-7.43.30-PM.png)

## Disclaimer:
The credits goes to @navinreddy20 from Telusko for teaching this course for free on youtube.