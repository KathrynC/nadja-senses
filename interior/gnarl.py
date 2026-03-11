"""Pattern 31: Seek the Gnarl (Complexity Foraging)
Pattern 32: The Eucatastrophe Sense (Happy Endings)

Implements the drive for interesting complexity (The Gnarl) and 
the detection of sudden positive ruptures (Happy Endings).
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any
import numpy as np

@dataclass
class GnarlState:
    complexity_score: float # 0.0 (Boring) to 1.0 (The Gnarl)
    eucatastrophe_potential: float # Probability of a happy ending
    is_gnarly: bool
    description: str

class GnarlObserver:
    """The 'Curiosity Engine'. Seeks complexity and green shoots."""
    
    def __init__(self):
        self.gnarl_threshold = 0.7
        self.green_shoots = ["innovation", "recovery", "cooperation", "clean_energy"]

    def sense_gnarl(self, manifold_stats: Dict[str, float], active_motifs: List[str]) -> GnarlState:
        """Sense the level of 'Gnarl' and 'Eucatastrophe' potential."""
        
        # 1. SEEK THE GNARL: Complexity lies at the edge of chaos
        # Volatility without rupture, high information velocity
        vol = manifold_stats.get("volatility", 0.0)
        velocity = manifold_stats.get("information_velocity", 0.5)
        
        # The Gnarl is high when vol is moderate-high but not breaking
        complexity = 1.0 - abs(0.6 - vol) 
        gnarly = complexity > self.gnarl_threshold
        
        # 2. FIND HAPPY ENDINGS: Detect 'Green Shoots' in the motifs
        green_count = len([m for m in active_motifs if m.lower() in self.green_shoots])
        eucatastrophe = min(1.0, green_count * 0.3)
        
        if eucatastrophe > 0.6:
            desc = "EUCATASTROPHE DETECTED: Sudden positive rupture. A happy ending is forming."
        elif gnarly:
            desc = "THE GNARL: Interesting complexity detected. Probability of surprise is high."
        elif complexity < 0.2:
            desc = "STAGNATION: Low complexity. Manifold is boring/predictable."
        else:
            desc = "Complexity is at baseline levels."
            
        return GnarlState(
            complexity_score=complexity,
            eucatastrophe_potential=eucatastrophe,
            is_gnarly=gnarly,
            description=desc
        )

    def generate_curiosity_report(self, state: GnarlState) -> str:
        """Produce a report on the 'Gnarliness' of the current state."""
        lines = [
            "CURIOSITY / GNARLINESS REPORT",
            f"  • Complexity Score: {state.complexity_score:.2f} ({'GNARLY' if state.is_gnarly else 'FLAT'})",
            f"  • Happy Ending Potential: {state.eucatastrophe_potential:.2f}",
            f"  • Narrative Vector: {state.description}"
        ]
        if state.is_gnarly:
            lines.append("    ACTION: Seek the Gnarl. Stay in the zone of high surprise.")
            
        return "\n".join(lines)
