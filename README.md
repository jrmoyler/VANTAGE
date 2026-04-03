# VANTAGE
### Visual Arts & Design Intelligence Terminal

VANTAGE is an operator-grade creative command console for design technologists and creative operators.

It supports two runtimes:
- **Terminal CLI** for command-driven workflow (`GENERATE`, `ASK`, `STYLES`, etc.)
- **Vercel-hostable API** for web/app integrations
VANTAGE is an operator-grade creative command console built for design technologists. It converts natural-language build intent into:

- a **Component Matrix** (layout, motion, type, color, data tiers),
- a **production-ready Structured Prompt**,
- **Design Intelligence** (top 4 principles + rationale),
- and a **Color Direction map** aligned to the 60:30:10 system.

## Visual DNA
- **60% Environment:** `#080B10`
- **30% Panels/Surfaces:** `#0D1219` / `#121A24`
- **10% Primary Accent:** `#00D2B4`
- **Secondary Accent:** `#FF6B35`
- **Typography direction:** Syne 800 (display), DM Mono (terminal/data)
- **Grid motif:** 40px subtle overlay at 1.5% opacity

## Core Screens (CLI)
## Core Screens
1. Prompt Generator
2. Knowledge Base (12-card creative intelligence index)
3. Style Explorer (30+ styles)
4. Principles Index (12 design laws)
5. Command Console (HELP/Menu)

## Real Seeded Knowledge Base
Data is in `knowledge_base.json` with real references for:
Data is now stored in `knowledge_base.json` and includes real references for all required areas:
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

## CLI Commands
- Photography styles + design psychology layers (game UX, dark patterns, anticipatory design)

## Command System
- `GENERATE [intent]`
- `ASK [query]`
- `STYLES`
- `PRINCIPLES`
- `KNOWLEDGE`
- `SCREEN [1-5]`
- `HELP`
- `CLEAR`
- `EXIT`

## Local Run (CLI)
```bash
python3 main.py
# or
python3 vantage.py
# or installed script
vantage
```

## API Entrypoint (for hosting)
- `api/main.py` (FastAPI app instance: `app`)

### API Endpoints
- `GET /api/health`
- `GET /api/knowledge`
- `GET /api/styles`
- `GET /api/principles`
- `POST /api/generate` with `{ "intent": "..." }`
- `POST /api/ask` with `{ "query": "..." }`

## Vercel Deployment
This repo is configured for Vercel with `vercel.json` routing all requests to `api/main.py`.

```bash
vercel
```

Vercel will install dependencies from `requirements.txt` and deploy the Python API.
## Setup
```bash
python3 vantage.py
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python vantage.py
```

## Example
```text
GENERATE Build a cinematic AI dashboard for creative direction with motion-heavy analytics
ASK kurosawa
ASK rack focus
ASK confirmshaming
```
```

VANTAGE will return a stack-aligned build spec with deterministic visual and systems guidance.
