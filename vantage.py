#!/usr/bin/env python3
"""VANTAGE — Visual Arts & Design Intelligence Terminal."""

from __future__ import annotations

import json
import shlex
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


@dataclass(frozen=True)
class Principle:
    name: str
    summary: str
    when_to_use: str


class VantageEngine:
    def __init__(self) -> None:
        data_path = Path(__file__).with_name("knowledge_base.json")
        self.knowledge_db = json.loads(data_path.read_text(encoding="utf-8"))

    component_rules = {
        "dashboard": ["12-column data grid", "KPI cards", "trend lines", "filter rail"],
        "portfolio": ["modular masonry gallery", "project case-study cards", "sticky narrative nav"],
        "landing": ["hero split layout", "feature ladders", "social proof ribbon", "CTA command strip"],
        "mobile": ["bottom command dock", "thumb-zone controls", "gesture transitions"],
        "ecommerce": ["product matrix", "comparison table", "trust badges", "checkout flow map"],
        "game": ["HUD layers", "stat bars", "diegetic overlays", "interaction reticle"],
        "film": ["shot-list timeline", "scene metadata panels", "moodboard sequence"],
        "ai": ["prompt module", "model control panel", "output scoring rubric", "version compare"],
    }

    principle_rules = {
        "Hierarchy": "Prioritize attention using scale, contrast, and spacing for mission-critical data.",
        "Gestalt Grouping": "Cluster related controls to reduce cognitive parsing overhead.",
        "Hick's Law": "Constrain options per step to accelerate decision throughput.",
        "Fitts's Law": "Make high-frequency controls larger and spatially predictable.",
        "Miller's Law": "Chunk dense information into 5–9 meaningful units.",
        "Occam's Razor": "Remove decorative complexity that does not increase signal.",
        "Serial Position Effect": "Place strategic calls-to-action first and last in sequences.",
        "Von Restorff Effect": "Use the teal accent only for active/high-value actions.",
        "Aesthetic-Usability Effect": "Deliver polished visual rhythm to increase user trust.",
        "Progressive Disclosure": "Expose detail on demand, preserve tactical overview by default.",
        "Zeigarnik Effect": "Surface incomplete tasks with persistent, motivating state cues.",
        "Pareto Principle": "Invest 80% of craft on flows that drive 20% of key outcomes.",
    }

    style_explorer = [
        "Swiss International Style",
        "Bauhaus",
        "Art Deco",
        "Constructivism",
        "De Stijl",
        "Brutalism",
        "Minimalism",
        "Maximalism",
        "Neo-Brutalism",
        "Memphis",
        "Psychedelic",
        "International Typographic Style",
        "Corporate Modernism",
        "Afrofuturism",
        "Cyberpunk",
        "Biopunk",
        "Retro Futurism",
        "Y2K",
        "Vaporwave",
        "Noir",
        "Superflat",
        "Ukiyo-e",
        "Wabi-sabi",
        "Scandinavian Minimal",
        "Mid-Century Modern",
        "Postmodern",
        "Grunge",
        "Editorial Modern",
        "Data Visualization Minimal",
        "Monochrome Utility",
        "Cinematic Matte",
        "Arcade UI",
        "Skeuomorphism",
        "Flat Design",
        "Material-inspired Systems",
        "Isometric Illustration",
        "Diagrammatic Interface",
        "Generative Design",
        "Noir Futurism",
        "Kinetic Typography",
        "Retro CRT Ops",
        "Japanese Metabolism",
        "Biomorphic Tech",
        "Post-Internet Collage",
        "Luxury Tech Editorial",
        "Glitch Systems",
        "Tactical Industrial",
        "Monospace Intelligence",
        "Cinematic Matte UI",
        "Branded Command Center",
        "Experimental Type-led",
        "Modular Storyboard",
        "Voxel UI",
        "Vector Flat Pro",
        "Editorial Darkness",
        "Generative Organic",
        "Parametric Dashboard",
        "Brutalist Data Ops",
        "Speculative Interface",
        "Analog Plotter",
        "Arcade Overlay",
        "Architectural Blueprint",
        "Motion-first Product",
    ]

    principles = [
        Principle("Hierarchy", "Structure visual importance deliberately.", "Dashboards, hero sections, data critical flows."),
        Principle("Contrast", "Use luminance and scale contrast to guide scanning.", "Dense operator interfaces."),
        Principle("Alignment", "Anchor every element to a deliberate grid.", "Any system UI."),
        Principle("Proximity", "Group related data by distance.", "Forms and panel clusters."),
        Principle("Repetition", "Repeat motifs for learned interaction speed.", "Component systems."),
        Principle("Balance", "Distribute visual weight for stability.", "Complex multi-panel layouts."),
        Principle("White Space", "Breathing room creates comprehension speed.", "High-density text surfaces."),
        Principle("Scale", "Use size as an information hierarchy dial.", "KPI and CTA emphasis."),
        Principle("Consistency", "Predictable patterns reduce cognitive load.", "Cross-screen systems."),
        Principle("Feedback", "Every action needs visible response.", "Form submission and command actions."),
        Principle("Affordance", "Controls must look usable.", "Interactive widgets and command chips."),
        Principle("Progressive Disclosure", "Layer complexity over time.", "Power-user tools."),
    ]

    knowledge_cards = [
        ("anime_artists_mangakas", "Anime Artists & Mangakas"),
        ("graphic_design_artists", "Graphic Design Artists"),
        ("modern_contemporary_artists", "Modern & Contemporary Artists"),
        ("cartoon_animation_styles", "Cartoon & Animation Styles"),
        ("art_styles_movements", "Art Styles & Movements"),
        ("animated_films", "Animated Films"),
        ("structural_rules_design", "Structural Rules of Design"),
        ("design_color_psychology", "Design Theories & Color Psychology"),
        ("film_directors", "Film Directors"),
        ("cinematography_lexicon", "Cinematography Lexicon"),
        ("camera_lens_catalog", "Camera / Lens Catalog"),
        ("photo_styles_and_design_psychology", "Photo Styles + Design Psychology Layers"),
    ]

    def search_knowledge(self, query: str, limit: int = 20) -> list[dict]:
        tokens = [t for t in query.lower().split() if t]
        hits: list[dict] = []

        for key, _ in self.knowledge_cards:
            for item in self.knowledge_db[key]:
                joined = " ".join(str(v) for v in item.values()).lower()
                if query.lower() in joined or any(tok in joined for tok in tokens):
                    hits.append({"domain": key, "record": item})

        return hits[:limit]

    def generate(self, intent: str) -> dict:
        lowered = intent.lower()
        components = ["responsive shell", "command console", "stateful cards", "tokenized spacing scale"]

        for key, mapped in self.component_rules.items():
            if key in lowered:
                components.extend(mapped)

        if "motion" in lowered or "animate" in lowered:
            components.extend(["200ms micro-interactions", "command feedback pulse", "prefers-reduced-motion fallbacks"])

        components = sorted(set(components))
        matched = []

        if any(k in lowered for k in ["dashboard", "analytics", "data", "console"]):
            matched.extend(["Hierarchy", "Miller's Law"])
        if any(k in lowered for k in ["app", "product", "flow", "onboarding"]):
            matched.extend(["Hick's Law", "Progressive Disclosure"])
        if any(k in lowered for k in ["cta", "marketing", "landing", "brand"]):
            matched.extend(["Von Restorff Effect", "Serial Position Effect"])
        if not matched:
            matched.extend(["Occam's Razor", "Pareto Principle", "Gestalt Grouping", "Aesthetic-Usability Effect"])

        top4 = list(dict.fromkeys(matched))[:4]
        component_block = "\n- ".join(components)
        prompt = dedent(
            f"""
            Project Intent:
            {intent}

            Visual System:
            - Tone: Bloomberg × Palantir command center, operator-grade, signal-dense
            - Color ratio 60:30:10: #080B10 / #0D1219-#121A24 / #00D2B4
            - Secondary utility accent: #FF6B35 for warnings, tier markers, escalations
            - Typography: Syne 800 (headings), DM Mono (terminal and data layers)
            - Reject: glassmorphism, purple gradients, decorative noise

            Component Stack:
            - {component_block}

            Motion Requirements:
            - Tight motion budget (120–220ms), ease-out, no ornamental loops
            - Status transitions must communicate system state, not decoration
            - Cursor, focus, and command execution feedback should be explicit

            Layout Rules:
            - 12-column structure on desktop, compact command rail on mobile
            - 40px subtle grid motif at 1.5% opacity over deep void base
            - Prioritize hierarchy: mission-critical controls in top-left scan zones

            Implementation Stack:
            - Componentized design system with design tokens
            - Semantic HTML / accessible keyboard command model
            - Theme variables for color, type, spacing, motion

            Quality Bar:
            - Every element must justify information value
            - Console interactions should be deterministic and fast
            - Dense, exacting, studio-internal tooling feel
            """
        ).strip()

        return {
            "components": components,
            "structured_prompt": prompt,
            "principles": [(p, self.principle_rules[p]) for p in top4],
            "color_direction": {
                "Environment (60%)": "#080B10",
                "Panels/Surfaces (30%)": "#0D1219 and #121A24",
                "Primary Accent (10%)": "#00D2B4",
                "Secondary Utility Accent": "#FF6B35",
                "Grid Overlay": "40px lattice at 1.5% opacity",
            },
        }


class VantageApp:
    def __init__(self) -> None:
        self.engine = VantageEngine()

    @staticmethod
    def hr(title: str = "") -> None:
        line = "=" * 96
        print(f"\n{line}\n{title}\n{line}" if title else f"\n{line}")

    def header(self) -> None:
        self.hr("VANTAGE — Visual Arts & Design Intelligence Terminal")
        print("Deep void #080B10 | Slate #0D1219/#121A24 | Accent #00D2B4 | Utility #FF6B35")

    def render_help(self) -> None:
        self.hr("Command Console")
        print(
            "GENERATE [intent]   → fires generator with pre-filled intent\n"
            "ASK [query]         → routes to knowledge base query\n"
            "STYLES              → opens Style Explorer\n"
            "PRINCIPLES          → opens Principles Index\n"
            "KNOWLEDGE           → opens Knowledge Base\n"
            "SCREEN [1–5]        → switches screen by number\n"
            "HELP                → shows command menu\n"
            "CLEAR               → clears console log\n"
            "EXIT                → quits VANTAGE"
        )

    def show_screen(self, num: int) -> None:
        if num == 1:
            self.hr("SCREEN 1 — Prompt Generator")
            print("Run: GENERATE [intent]")
        elif num == 2:
            self.hr("SCREEN 2 — Knowledge Base")
            for idx, (key, title) in enumerate(self.engine.knowledge_cards, start=1):
                print(f"{idx:02d}. {title}: {len(self.engine.knowledge_db[key])} records")
        elif num == 3:
            self.hr("SCREEN 3 — Style Explorer")
            for i, style in enumerate(self.engine.style_explorer, start=1):
                print(f"{i:02d}. {style}")
        elif num == 4:
            self.hr("SCREEN 4 — Principles Index")
            for p in self.engine.principles:
                print(f"- {p.name}: {p.summary} | Use: {p.when_to_use}")
        elif num == 5:
            self.render_help()
        else:
            print("SCREEN must be 1-5")

    def ask_knowledge(self, query: str) -> None:
        self.hr(f"Knowledge Query — {query}")
        hits = self.engine.search_knowledge(query, limit=12)

        if not hits:
            print("No direct match. Showing representative records:")
            for key, title in self.engine.knowledge_cards[:4]:
                sample = self.engine.knowledge_db[key][0]
                print(f"- {title}: {sample}")
            return

        for idx, hit in enumerate(hits, start=1):
            print(f"{idx:02d}. {hit['domain']}: {hit['record']}")

    def run_generate(self, intent: str) -> None:
        out = self.engine.generate(intent)
        self.show_screen(1)
        self.hr("Component Matrix")
        print("Tier: Layout / Motion / Typography / Color / Data")
        for c in out["components"]:
            print(f"- {c}")

        self.hr("Structured Prompt")
        print(out["structured_prompt"])

        self.hr("Design Intelligence — Top 4")
        for p, reason in out["principles"]:
            print(f"- {p}: {reason}")

        self.hr("Color Direction")
        for role, value in out["color_direction"].items():
            print(f"- {role}: {value}")

    def run(self) -> None:
        self.header()
        self.show_screen(5)

        while True:
            try:
                raw = input("\nVANTAGE> ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\nSession ended.")
                break

            if not raw:
                continue

            parts = shlex.split(raw)
            cmd = parts[0].upper()
            arg = raw[len(parts[0]) :].strip()

            if cmd == "GENERATE":
                if arg:
                    self.run_generate(arg)
                else:
                    print("Usage: GENERATE [intent]")
            elif cmd == "ASK":
                if arg:
                    self.ask_knowledge(arg)
                else:
                    print("Usage: ASK [query]")
            elif cmd == "STYLES":
                self.show_screen(3)
            elif cmd == "PRINCIPLES":
                self.show_screen(4)
            elif cmd == "KNOWLEDGE":
                self.show_screen(2)
            elif cmd == "SCREEN":
                if len(parts) > 1 and parts[1].isdigit():
                    self.show_screen(int(parts[1]))
                else:
                    print("Usage: SCREEN [1-5]")
            elif cmd == "HELP":
                self.render_help()
            elif cmd == "CLEAR":
                print("\033c", end="")
                self.header()
            elif cmd in {"EXIT", "QUIT"}:
                print("VANTAGE offline.")
                break
            else:
                print(f"Unknown command: {cmd}. Try HELP")


def main() -> None:
    VantageApp().run()


if __name__ == "__main__":
    main()
