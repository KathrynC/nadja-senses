"""Pattern 23: Hunger & Thirst (Metabolic Drive)

Implements the system's appetite for novelty and opportunities.
Includes:
1. Satiety: The sense of boredom/saturation with clichés (saturation_audit.py).
2. Foraging: The drive to find 'nectar' or micro-opportunities (hummingbird.py).
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any

@dataclass
class MetabolicState:
    hunger_level: float # Drive to find new opportunities
    satiety_level: float # Boredom/saturation with existing tropes
    available_nectar: int # Number of micro-opportunities found
    description: str

class MetabolicObserver:
    """The 'Stomach' of the sensorium. Monitors informational appetite."""
    
    def sense_appetite(self, saturation_score: float, nectar_count: int) -> MetabolicState:
        """Sense the current informational hunger and satiety."""
        
        # High saturation (clichés) leads to high satiety (boredom)
        satiety = saturation_score
        
        # High satiety triggers 'hunger' for a Rupture or something new
        hunger = 1.0 if satiety > 0.8 else (1.0 - satiety)
        
        if nectar_count > 3:
            desc = "SATED: Garden is full of nectar. Hummingbird is busy."
        elif satiety > 0.8:
            desc = "BOREDOM: Over-inscribed with clichés. Hunger for RUPTURE."
        elif hunger > 0.7:
            desc = "HUNGER: Searching for micro-opportunities in the manifold."
        else:
            desc = "Metabolic state is balanced."
            
        return MetabolicState(
            hunger_level=hunger,
            satiety_level=satiety,
            available_nectar=nectar_count,
            description=desc
        )
