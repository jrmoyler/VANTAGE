# VANTAGE
### Visual Arts & Design Intelligence Terminal

VANTAGE is an operator-grade creative command console for design technologists and creative operators.

It supports two runtimes:
- **Terminal CLI** for command-driven workflow (`GENERATE`, `ASK`, `STYLES`, etc.)
- **Vercel-hostable API** for web/app integrations

## Visual DNA
- **60% Environment:** `#080B10`
- **30% Panels/Surfaces:** `#0D1219` / `#121A24`
- **10% Primary Accent:** `#00D2B4`
- **Secondary Accent:** `#FF6B35`
- **Typography direction:** Syne 800 (display), DM Mono (terminal/data)
- **Grid motif:** 40px subtle overlay at 1.5% opacity

## Core Screens (CLI)
1. Prompt Generator
2. Knowledge Base (12-card creative intelligence index)
3. Style Explorer (30+ styles)
4. Principles Index (12 design laws)
5. Command Console (HELP/Menu)

## Real Seeded Knowledge Base
Data is in `knowledge_base.json` with real references for:
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
