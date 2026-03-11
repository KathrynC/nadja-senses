"""Pattern 16: Pheromonal Sensing (The Subliminal Mood)

Senses the 'silent messengers' of the manifold — subliminal mood signals 
that permeate the environment before they are spoken. Maps capital-flow 
markers (VIX, Put/Call, Dark Pools) to affective states.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Any

@dataclass
class PheromoneGestalt:
    """A subliminal mood state detected in the manifold's air."""
    mood: str  # FEAR, GREED, EXHAUSTION, ATTRACTION
    intensity: float
    description: str
    markers: Dict[str, float]

class PheromoneObserver:
    """The 'Silent Messenger' detector. Senses subliminal signals."""
    
    def __init__(self):
        self.moods = {
            "fear": "Sulfurous/Putrid undertones. High protective scent.",
            "greed": "Sweet/Fruity attraction. Pheromonal bloom.",
            "exhaustion": "Popcorn/Minty stasis. The scent is fading.",
            "attraction": "Citrus/Fragrant resonance. New capital seeking contact."
        }

    def sense_mood(self, flow_data: Dict[str, float]) -> PheromoneGestalt:
        """Detect the ambient mood from flow markers."""
        # VIX/VXV > 1.0 = Inverse Term Structure (High Fear)
        # Put/Call > 1.0 = Defensive Posture
        vix_term = flow_data.get("vix_vxv_ratio", 0.9)
        pc_ratio = flow_data.get("put_call_ratio", 0.8)
        
        if vix_term > 1.05:
            mood = "fear"
            intensity = vix_term - 1.0
        elif pc_ratio < 0.6:
            mood = "greed"
            intensity = 1.0 - pc_ratio
        elif flow_data.get("volume_velocity", 1.0) < 0.5:
            mood = "exhaustion"
            intensity = 0.5
        else:
            mood = "attraction"
            intensity = 0.3
            
        return PheromoneGestalt(
            mood=mood,
            intensity=min(1.0, intensity * 2.0),
            description=self.moods.get(mood, "Neutral mood."),
            markers=flow_data
        )
