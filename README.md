# VANTAGE
### Visual Arts & Design Intelligence Terminal

VANTAGE is an operator-grade creative command console for design technologists and creative operators.

It supports two runtimes:
- **Terminal CLI** for command-driven workflows (`GENERATE`, `ASK`, `STYLES`, etc.)
- **FastAPI web app + API** for browser and app integrations (Vercel-compatible)

## Visual DNA
- **60% Environment:** `#080B10`
- **30% Panels/Surfaces:** `#0D1219` / `#121A24`
- **10% Primary Accent:** `#00D2B4`
- **Secondary Accent:** `#FF6B35`
- **Typography direction:** Syne 800 (display), DM Mono (terminal/data)
- **Grid motif:** 40px subtle overlay at 1.5% opacity

## Core Screens
1. Prompt Generator
2. Knowledge Base (12-card creative intelligence index)
3. Style Explorer
4. Principles Index
5. Command Console

## Data + Knowledge
Data is stored in `knowledge_base.json` and includes curated references for:
- Anime artists & mangakas
- Graphic design artists
- Modern/contemporary artists
- Cartoon and animation styles
- Art movements
- Animated films
- Structural rules of design
- Design theories and color psychology
- Film directors
- Cinematography lexicon
- Camera and lens catalog
- Photography styles + psychology layers (game UX, dark patterns, anticipatory design)

## Command System (CLI)
- `GENERATE [intent]`
- `ASK [query]`
- `STYLES`
- `PRINCIPLES`
- `KNOWLEDGE`
- `SCREEN [1-5]`
- `HELP`
- `CLEAR`
- `EXIT`

## Local Run
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# CLI
python3 main.py

# Web app / API
uvicorn api.main:app --reload
```

Open: `http://127.0.0.1:8000/`

## API Endpoints
- `GET /` (web UI)
- `GET /api/health`
- `GET /api/knowledge`
- `GET /api/styles`
- `GET /api/principles`
- `POST /api/generate` with `{ "intent": "..." }`
- `POST /api/ask` with `{ "query": "..." }`

## Security + Reliability Baseline
- Input-length validation on mutation/search endpoints
- Security headers middleware (CSP, clickjacking, nosniff, referrer policy)
- `prefers-reduced-motion` fallback in UI stylesheet

## Vercel Deployment
This repo is configured for Vercel with `vercel.json` routing all requests to `api/main.py`.

```bash
vercel
```
