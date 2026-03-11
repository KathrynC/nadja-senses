"""Pattern 27: Retrodictive Hindsight (Backcasting)

Implements the ability to calibrate current sensing by asking: 
"What would we have perceived before a known historical outcome?"
Refines sensory weights based on the correlation between predicted 
and realized archetypes.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any
import numpy as np

@dataclass
class BackcastResult:
    case_id: str
    predicted_archetype: str
    realized_archetype: str
    rank_correlation: float # Spearman rho
    blind_spot_detected: bool
    description: str

class BackcastObserver:
    """The 'Memory Replay' center. Calibrates sensing via hindsight."""
    
    def __init__(self):
        self.historical_cases = {
            "2008_CRISIS": "MARS",
            "2020_SHOCK": "MARS",
            "2017_GOLDILOCKS": "EARTH"
        }

    def validate_perception(self, case_id: str, current_perception: str) -> BackcastResult:
        """Compare current sensory perception against a historical ground truth."""
        realized = self.historical_cases.get(case_id, "UNKNOWN")
        
        # Simple correlation placeholder
        correlation = 1.0 if current_perception == realized else 0.2
        blind_spot = correlation < 0.5
        
        if blind_spot:
            desc = f"BLIND SPOT: Sensory logic failed to recognize {case_id}. Perception was {current_perception}."
        else:
            desc = f"RESONANCE: Sensing correctly identified the {case_id} archetype."
            
        return BackcastResult(
            case_id=case_id,
            predicted_archetype=current_perception,
            realized_archetype=realized,
            rank_correlation=correlation,
            blind_spot_detected=blind_spot,
            description=desc
        )

    def generate_hindsight_audit(self, results: List[BackcastResult]) -> str:
        """Produce a report on sensory accuracy over historical cases."""
        if not results:
            return "NO BACKCASTS PERFORMED."
            
        mean_rho = np.mean([r.rank_correlation for r in results])
        lines = [
            "RETRODICTIVE HINDSIGHT AUDIT",
            f"  • Mean Correlation: {mean_rho:.2f}",
            f"  • Reliable Cases: {len([r for r in results if not r.blind_spot_detected])}/{len(results)}"
        ]
        for r in results:
            marker = "✘" if r.blind_spot_detected else "✔"
            lines.append(f"  {marker} Case {r.case_id}: {r.description}")
            
        return "\n".join(lines)
