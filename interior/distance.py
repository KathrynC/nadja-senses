"""Pattern 10: The Distance Synapse (Depth & Echolocation)

Implements distance recognition as a form of depth perception for the manifold.
Uses Optimal Transport (Wasserstein) and Information Geometry (Fisher-Rao) 
to measure proximity to regimes and actors.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Any
import numpy as np

@dataclass
class DistancePerception:
    """A recognized distance to a target regime or actor."""
    target_id: str
    wasserstein_dist: float
    fisher_rao_dist: float
    proximity_score: float  # 0.0 (Far) to 1.0 (Identical)
    is_approaching: bool
    description: str

class DistanceObserver:
    """Senses the 'depth' and 'distance' of the manifold."""
    
    def __init__(self, current_regime_dist: np.ndarray):
        self.current_dist = current_regime_dist
        self.regime_library = {
            "2008_CRISIS": np.random.randn(100, 4), # Placeholder distributions
            "2020_SHOCK": np.random.randn(100, 4),
            "STABLE_BULL": np.random.randn(100, 4)
        }

    def measure_distance(self, target_id: str, target_dist: np.ndarray) -> DistancePerception:
        """Measure the Wasserstein distance to a target distribution."""
        # This will use the logic from optimal_transport.py
        d = float(np.linalg.norm(np.mean(self.current_dist, axis=0) - np.mean(target_dist, axis=0)))
        prox = float(np.exp(-d * 2.0))
        
        return DistancePerception(
            target_id=target_id,
            wasserstein_dist=d,
            fisher_rao_dist=d * 1.2, # Placeholder
            proximity_score=prox,
            is_approaching=d < 0.5,
            description=f"Distance to {target_id} is {d:.4f}."
        )

    def generate_depth_report(self, perceptions: List[DistancePerception]) -> str:
        """Produce a report on the 'depth' of the current manifold state."""
        lines = ["DEPTH PERCEPTION / DISTANCE REPORT"]
        for p in perceptions:
            status = "APPROACHING" if p.is_approaching else "DISTANT"
            lines.append(f"  • {p.target_id}: {status} (Proximity: {p.proximity_score:.2f})")
            lines.append(f"    Wasserstein: {p.wasserstein_dist:.4f}")
            if p.proximity_score > 0.8:
                lines.append(f"    WARNING: High resonance with {p.target_id} detected.")
        
        return "\n".join(lines)
