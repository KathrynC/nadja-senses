"""Pattern 35: The Lakoff Transducer (Metaphoric Mapping)

Translates multi-modal sensory signals into George Lakoff's structured 
conceptual metaphors and semantic frames. Provides the cognitive 'connective 
tissue' for the sensorium.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any

@dataclass
class MetaphoricFrame:
    """A structured Lakoff frame triggered by sensory input."""
    frame_id: str # e.g. CONTAINER, JOURNEY, WAR, MACHINE
    category: str # CONCEPTUAL_METAPHOR, MORAL_FOUNDATION, etc.
    intensity: float
    description: str
    icon: str

class LakoffTransducer:
    """The 'Cognitive Cortex' of the sensorium. Maps signals to metaphors."""
    
    def __init__(self):
        # Mappings from senses to Lakoff IDs
        self.sensory_map = {
            "hearing": {
                "IAMBIC": ("JOURNEY", "Investing as a path with direction and progress."),
                "TROCHAIC": ("FORCE", "Market moves as physical forces and resistance."),
                "DACTYLIC": ("WAR", "Trading as battle: attacks, defenses, winners/losers."),
                "CAESURA": ("STASIS", "A break or freeze in the narrative flow.")
            },
            "smell": {
                "putrid": ("DEGRADATION", "Systemic decay, pollution, or corruption."),
                "fragrant": ("SANCTITY", "Purity, integrity, and structural health."),
                "citrus": ("INNOVATION", "Fresh catalysts and sharp invention."),
                "sulfurous": ("CASCADE", "Systemic risk and chain reactions.")
            },
            "touch": {
                "resistance_hard": ("CONTAINER", "Markets as bounded spaces with limits."),
                "vibration_high": ("AMPLIFICATION", "Magnification of effects through feedback.")
            }
        }

    def transduce(self, sensorium_gestalt: Dict[str, Any]) -> List[MetaphoricFrame]:
        """Translate a sensory gestalt into a set of active Lakoff frames."""
        frames = []
        
        # 1. Map Hearing
        if "hearing" in sensorium_gestalt:
            h_val = sensorium_gestalt["hearing"]
            if h_val in self.sensory_map["hearing"]:
                fid, desc = self.sensory_map["hearing"][h_val]
                frames.append(MetaphoricFrame(fid, "CONCEPTUAL_METAPHOR", 0.8, desc, "⎔"))
                
        # 2. Map Smell
        if "smell" in sensorium_gestalt:
            s_val = sensorium_gestalt["smell"]
            if s_val in self.sensory_map["smell"]:
                fid, desc = self.sensory_map["smell"][s_val]
                frames.append(MetaphoricFrame(fid, "MORAL_FOUNDATION", 0.9, desc, "⚖"))
                
        return frames

    def generate_metaphor_audit(self, frames: List[MetaphoricFrame]) -> str:
        """Produce a report on the active metaphors structuring perception."""
        if not frames:
            return "NO STRUCTURED METAPHORS DETECTED."
            
        lines = ["LAKOFF METAPHORIC TRANSDUCTION REPORT"]
        for f in frames:
            lines.append(f"  {f.icon} Frame: {f.frame_id} ({f.category})")
            lines.append(f"    {f.description}")
            
        return "\n".join(lines)
