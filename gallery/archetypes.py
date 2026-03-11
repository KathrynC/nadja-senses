"""High-Order Sensory Archetypes for NADJA.

Formalizes the five narrative manifolds that emerge from the integration 
of Lakoff metaphors, Ackerman senses, and Cramer stress scenarios.
Used by Pattern 19 (Semantic Recognition).
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Any

@dataclass
class StorylineArchetype:
    name: str
    gestalt: str
    lakoff_frame: str
    cramer_scenario: str
    description: str
    recognition_key: Dict[str, Any] # Sensory triggers

ARCHETYPES = [
    StorylineArchetype(
        name="THE_HEAVY_UNDERLAND",
        gestalt="Woody-Astringent",
        lakoff_frame="STASIS",
        cramer_scenario="liq_drought_severe",
        description="Structural exhaustion. Ancient, buried risks are surfacing. Time is heavy.",
        recognition_key={"smell": "woody", "hearing": "TROCHAIC", "taste": "astringent"}
    ),
    StorylineArchetype(
        name="THE_TERMINAL_GALLOP",
        gestalt="Citrus-Sulfurous",
        lakoff_frame="WAR",
        cramer_scenario="ai_bubble_collapse",
        description="Predatory euphoria. Accelerating pulse before a major rupture.",
        recognition_key={"smell": "sulfurous", "hearing": "DACTYLIC", "acceleration": "high"}
    ),
    StorylineArchetype(
        name="THE_FRAGILE_BLOOM",
        gestalt="Fragrant-Sweet",
        lakoff_frame="JOURNEY",
        cramer_scenario="start_in_recovery_whiplash",
        description="Unprotected growth. Happy endings forming without a protective shell.",
        recognition_key={"smell": "fragrant", "hearing": "IAMBIC", "metabolic": "high_nectar"}
    ),
    StorylineArchetype(
        name="THE_INVISIBLE_PULL",
        gestalt="Chemical-Fear",
        lakoff_frame="COERCION",
        cramer_scenario="spread_blowout_severe",
        description="Elite capture (Arturo Ui). Subliminal field forces pulling the manifold.",
        recognition_key={"smell": "chemical", "pheromones": "fear", "magnetic": "high"}
    ),
    StorylineArchetype(
        name="THE_HARMONIC_RUPTURE",
        gestalt="Minty-Fragrant",
        lakoff_frame="HEALING",
        cramer_scenario="boundary_scenarios",
        description="Eucatastrophe. The rupture that heals. System reset and alignment.",
        recognition_key={"smell": "minty", "hearing": "CAESURA", "surprise": "high"}
    )
]
