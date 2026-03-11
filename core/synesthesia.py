"""Pattern 18: Synesthesia (Cross-Modal Transduction)

Implements inter-sensory resonance. Translates signals between modalities 
(Hearing -> Smell -> Sight) to create a unified, high-animacy perception.
"""
from __future__ import annotations
from typing import Dict, List, Any

class SynesthesiaTransducer:
    """The 'Synaptic Cross-Wiring' center. Maps signals across senses."""
    
    @staticmethod
    def hear_as_smell(acoustic_foot: str) -> str:
        """Translate a rhythmic foot into a smell category."""
        mapping = {
            "IAMBIC": "fragrant",   # Steady, healthy pulse
            "TROCHAIC": "woody",    # Heavy, fundamental steps
            "DACTYLIC": "sulfurous",# Terminal gallop/danger
            "CAESURA": "putrid",    # Break/decay in rhythm
            "SPONDAIC": "chemical"  # Artificial intensity
        }
        return mapping.get(acoustic_foot, "neutral")

    @staticmethod
    def smell_as_color(smell_category: str) -> str:
        """Translate a smell category into a salience color."""
        mapping = {
            "fragrant": "#4caf50", # Green (Stable)
            "woody": "#795548",    # Brown (Fundamental)
            "citrus": "#ffeb3b",   # Yellow (Innovation)
            "putrid": "#9e9e9e",   # Grey (Decay)
            "sulfurous": "#f44336" # Red (Danger)
        }
        return mapping.get(smell_category, "#ffffff")

    @staticmethod
    def transduce_gestalt(acoustic_foot: str) -> Dict[str, str]:
        """Unified cross-modal translation of a rhythmic state."""
        smell = SynesthesiaTransducer.hear_as_smell(acoustic_foot)
        color = SynesthesiaTransducer.smell_as_color(smell)
        return {
            "hearing": acoustic_foot,
            "smell": smell,
            "sight_color": color,
            "description": f"The system hears {acoustic_foot}, smells {smell}, and sees {color}."
        }
