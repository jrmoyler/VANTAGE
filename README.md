# VANTAGE
### Visual Arts & Design Intelligence Terminal

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

## Core Screens
1. Prompt Generator
2. Knowledge Base (12-card creative intelligence index)
3. Style Explorer (30+ styles)
4. Principles Index (12 design laws)
5. Command Console (HELP/Menu)

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

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python vantage.py
```

## Example
```text
GENERATE Build a cinematic AI dashboard for creative direction with motion-heavy analytics
```

VANTAGE will return a stack-aligned build spec with deterministic visual and systems guidance.
