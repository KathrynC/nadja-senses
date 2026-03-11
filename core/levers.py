"""Pattern 34: Lever Sensing (Agency & Intervention)

Implements the sense of agency — identifying where small actions lead 
to disproportionately positive outcomes. Uses Sobol sensitivity and 
Information Geometry to find 'Leverage Points' in the manifold.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any
import numpy as np

@dataclass
class LeveragePoint:
    """A specific parameter that acts as a lever in the manifold."""
    parameter_name: str
    impact_score: float # Sobol total-order index (0 to 1)
    information_gradient: float # FIM sensitivity
    direction_to_thriving: int # +1 (Increase), -1 (Decrease)
    description: str

class LeverObserver:
    """The 'Hand' of the sensorium. Senses where to push."""
    
    def __init__(self, parameter_names: List[str]):
        self.parameter_names = parameter_names

    def sense_levers(
        self, 
        sobol_results: Dict[str, float], 
        fim_sensitivity: Dict[str, float],
        thriving_gradient: Dict[str, int]
    ) -> List[LeveragePoint]:
        """Identify the top-k levers in the current manifold state."""
        levers = []
        
        for name in self.parameter_names:
            impact = sobol_results.get(name, 0.0)
            grad = fim_sensitivity.get(name, 0.0)
            direction = thriving_gradient.get(name, 0)
            
            # A 'Lever' has high impact and/or a high information gradient
            if impact > 0.3 or grad > 0.2:
                desc = self._get_lever_description(name, impact, grad)
                levers.append(LeveragePoint(
                    parameter_name=name,
                    impact_score=impact,
                    information_gradient=grad,
                    direction_to_thriving=direction,
                    description=desc
                ))
        
        # Sort by impact score descending
        levers.sort(key=lambda x: x.impact_score, reverse=True)
        return levers

    def _get_lever_description(self, name: str, impact: float, grad: float) -> str:
        if impact > 0.7:
            return f"CRITICAL LEVER: {name} dominates output variance. High agency potential."
        if grad > 0.5:
            return f"INFORMATION BOTTLENECK: {name} controls the intrinsic model geometry."
        return f"MODERATE LEVER: {name} has measurable influence on outcomes."

    def generate_agency_report(self, levers: List[LeveragePoint]) -> str:
        """Produce a report on the system's leverage points."""
        if not levers:
            return "THE SYSTEM IS RIGID. NO DISPROPORTIONATE LEVERS DETECTED."
            
        lines = ["LEVER SENSING / AGENCY REPORT"]
        for l in levers:
            action = "INCREASE" if l.direction_to_thriving > 0 else "DECREASE" if l.direction_to_thriving < 0 else "NUDGE"
            lines.append(f"  • {l.parameter_name}: IMPACT {l.impact_score:.2f} | GRADIENT {l.information_gradient:.2f}")
            lines.append(f"    {l.description}")
            lines.append(f"    RECOMMENDED ACTION: {action} to move toward Thriving.")
        
        return "\n".join(lines)
