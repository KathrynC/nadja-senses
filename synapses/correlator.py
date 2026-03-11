"""Pattern 3: Light on Two Sides (Cross-Domain Divergence)

Ensures '3D perception' by requiring cross-modal confirmation for major 
signals. A signal is only fully 'perceived' if it is seen from at least 
two disjoint domains (e.g. Olfactory + Haptic).
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional

@dataclass
class DivergenceSignal:
    """A signal that has been confirmed (or denied) by multiple senses."""
    motif: str
    is_confirmed: bool
    confirmation_breadth: int # Number of senses that saw it
    divergence_score: float # Delta between senses
    description: str
    participating_senses: List[str]

class CrossModalCorrelator:
    """The 'Synapse' center. Performs 'Light on Two Sides' checks."""
    
    def __init__(self, confirmation_threshold: int = 2):
        self.confirmation_threshold = confirmation_threshold

    def correlate(self, motif: str, sensory_bids: List[Dict[str, Any]]) -> DivergenceSignal:
        """Verify a motif across multiple sensory modalities."""
        
        # 1. Filter bids that mention this motif
        active_bids = [b for b in sensory_bids if b.get("motif") == motif]
        senses = [b.get("source_sense") for b in active_bids]
        
        # 2. Calculate divergence
        # If one sense sees it as 0.9 and another as 0.1, divergence is high
        salience_vals = [b.get("salience", 0.0) for b in active_bids]
        div = float(np.std(salience_vals)) if len(salience_vals) > 1 else 1.0
        
        confirmed = len(senses) >= self.confirmation_threshold and div < 0.3
        
        if confirmed:
            desc = f"RESONANCE: '{motif}' confirmed across {len(senses)} senses with low divergence."
        elif len(senses) >= self.confirmation_threshold:
            desc = f"DIVERGENCE: '{motif}' seen by {len(senses)} senses but with high discordance."
        else:
            desc = f"FLAT PERCEPTION: '{motif}' seen only by {len(senses)} sense(s). Needs more light."
            
        return DivergenceSignal(
            motif=motif,
            is_confirmed=confirmed,
            confirmation_breadth=len(senses),
            divergence_score=div,
            description=desc,
            participating_senses=senses
        )

import numpy as np
