"""Vercel-compatible ASGI app for VANTAGE."""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from vantage import VantageEngine

app = FastAPI(title="VANTAGE API", version="0.1.0")
engine = VantageEngine()


class GenerateRequest(BaseModel):
    intent: str


class AskRequest(BaseModel):
    query: str


@app.get("/")
def root() -> dict:
    return {
        "name": "VANTAGE",
        "subtitle": "Visual Arts & Design Intelligence Terminal",
        "status": "online",
        "endpoints": ["/api/health", "/api/knowledge", "/api/styles", "/api/principles", "/api/generate", "/api/ask"],
    }


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
    query = body.query.lower()
    hits = []
    for key, _ in engine.knowledge_cards:
        for item in engine.knowledge_db[key]:
            joined = " ".join(str(v) for v in item.values()).lower()
            if query in joined or any(tok in joined for tok in query.split()):
                hits.append({"domain": key, "record": item})

    return {
        "query": body.query,
        "results": hits[:20],
        "total": len(hits),
    }
