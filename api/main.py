"""Vercel-compatible ASGI app for VANTAGE."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from vantage import VantageEngine

app = FastAPI(title="VANTAGE API", version="0.2.0")
engine = VantageEngine()

static_dir = Path(__file__).with_name("static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


@app.middleware("http")
async def security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
    response.headers["Content-Security-Policy"] = "default-src 'self'; style-src 'self'; script-src 'self'; img-src 'self' data:"
    return response


class GenerateRequest(BaseModel):
    intent: str = Field(min_length=8, max_length=2000)


class AskRequest(BaseModel):
    query: str = Field(min_length=2, max_length=240)


@app.get("/")
def root() -> FileResponse:
    return FileResponse(static_dir / "index.html")


@app.get("/api/health")
def health() -> dict:
    return {"ok": True}


@app.get("/api/knowledge")
def knowledge_index() -> dict:
    return {
        "domains": [
            {
                "key": key,
                "title": title,
                "count": len(engine.knowledge_db[key]),
            }
            for key, title in engine.knowledge_cards
        ]
    }


@app.get("/api/styles")
def styles() -> dict:
    return {"styles": engine.style_explorer}


@app.get("/api/principles")
def principles() -> dict:
    return {
        "principles": [
            {
                "name": p.name,
                "summary": p.summary,
                "when_to_use": p.when_to_use,
            }
            for p in engine.principles
        ]
    }


@app.post("/api/generate")
def generate(body: GenerateRequest) -> dict:
    return engine.generate(body.intent)


@app.post("/api/ask")
def ask(body: AskRequest) -> dict:
    hits = engine.search_knowledge(body.query, limit=20)
    return {
        "query": body.query,
        "results": hits,
        "total": len(hits),
    }


@app.get("/api/ask")
def ask_get(query: str) -> dict:
    if len(query.strip()) < 2:
        raise HTTPException(status_code=400, detail="query must be at least 2 characters")
    hits = engine.search_knowledge(query, limit=20)
    return {
        "query": query,
        "results": hits,
        "total": len(hits),
    }
