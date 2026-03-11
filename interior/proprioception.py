"""Pattern 9: Proprioception (Self-Movement and Body Position)

Implements the sense of proprioception — the system's ability to sense its 
own posture, leverage, and rebalancing 'gait' without external visuals.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any
import numpy as np

@dataclass
class PostureSignature:
    leverage_extension: float  # How 'stretched' the leverage is
    rebalance_frequency: float # How 'fast' the rebalancing gait is
    concentration_weight: float # How 'heavy' one side of the body is
    recognized_gait: str
    description: str

class ProprioceptionObserver:
    """The system's internal sense of its own physical strategy configuration."""
    
    def __init__(self):
        self.gaits = {
            "sprint": "High leverage, rapid rebalance. (Aggressive)",
            "trudge": "Low leverage, infrequent rebalance. (Defensive)",
            "limp": "Asymmetric concentration, high friction. (Imbalanced)",
            "steady_walk": "Balanced leverage and rebalance cycle. (Neutral)"
        }

    def sense_posture(self, strategy_params: Dict[str, float]) -> PostureSignature:
        """Sense the current 'body position' of the simulation."""
        lev = strategy_params.get("leverage_target", 1.0)
        reb = strategy_params.get("rebalance_threshold", 0.1)
        conc = strategy_params.get("max_concentration", 0.15)
        
        if lev > 2.0 and reb < 0.05:
            gait = "sprint"
        elif lev < 0.5:
            gait = "trudge"
        elif conc > 0.25:
            gait = "limp"
        else:
            gait = "steady_walk"
            
        return PostureSignature(
            leverage_extension=lev,
            rebalance_frequency=1.0 - reb,
            concentration_weight=conc,
            recognized_gait=gait,
            description=self.gaits.get(gait, "Unknown posture.")
        )
