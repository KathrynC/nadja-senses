"""Pattern 38: The Joy of Recognition (Lexical Precision)

Implements lexical precision as a cognitive reward. Connects sensory 
gestalts to Robert Macfarlane's landscape vocabulary and audits 
narratives for 'Desecration' slop.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Any, Optional

@dataclass(frozen=True)
class PhilologicalAnchor:
    word: str
    definition: str
    origin: str
    is_restorative: bool # True if it replaces a 'desecrated' term

class LexicalObserver:
    """The 'Word-Hoard' center. Provides precision and audits slop."""
    
    def __init__(self):
        # Macfarlane-inspired Word-Hoard
        self.hoard = [
            PhilologicalAnchor("Smeuse", "A gap in the base of a hedge; a way through stasis.", "Sussex", True),
            PhilologicalAnchor("Zwer", "A sudden, non-linear acceleration (the whirr of wings).", "Exmoor", True),
            PhilologicalAnchor("Amveal", "The transition from flow to trickle; liquidity freeze.", "Exmoor", True),
            PhilologicalAnchor("Underland", "The world beneath the surface; buried systemic risk.", "Deep Time", True),
            PhilologicalAnchor("Kist", "A stone chest; the containment of legacy data.", "Gaelic", True)
        ]
        
        # Desecration Phrasebook (Dark Twin)
        self.desecration = {
            "human capital": "people and their capabilities",
            "harvest data": "listen to signals",
            "ecosystem services": "ecological relationships",
            "drill down": "explore deeply"
        }

    def find_precision(self, manifold_state: str) -> Optional[PhilologicalAnchor]:
        """Find the exact word to describe a manifold state."""
        mapping = {
            "STASIS": self.hoard[0], # Smeuse (the way through)
            "ACCELERATION": self.hoard[1], # Zwer
            "LIQUIDITY_FREEZE": self.hoard[2], # Amveal
            "BURIED_RISK": self.hoard[3], # Underland
            "CONTAINMENT": self.hoard[4] # Kist
        }
        return mapping.get(manifold_state)

    def audit_narrative(self, text: str) -> Dict[str, Any]:
        """Scan for desecrated language and suggest restorative alternatives."""
        flagged = []
        for term, alternative in self.desecration.items():
            if term in text.lower():
                flagged.append({"desecrated": term, "restorative": alternative})
        
        return {
            "has_slop": len(flagged) > 0,
            "flagged_items": flagged,
            "joy_score": 1.0 - (len(flagged) * 0.2)
        }
