"""Pattern 26: Sensory Calibration (Homeostasis)

Implements the sense of internal balance and sensitivity tuning.
Uses Information Geometry (Fisher-Rao) to calibrate the delta between 
the system's perception and the world's reality.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any
import numpy as np

@dataclass
class HomeostaticState:
    geometric_drift: float # Fisher-Rao distance from reality
    current_gains: Dict[str, float] # Sensitivity gain per sense
    is_balanced: bool
    description: str

class HomeostasisObserver:
    """The 'Thermostat' of the sensorium. Maintains internal balance."""
    
    def __init__(self):
        self.default_gains = {
            "smell": 1.0,
            "sight": 1.0,
            "hearing": 1.0,
            "touch": 1.0,
            "metabolic": 1.0
        }

    def calibrate(self, perception_moments: Dict[str, float], reality_moments: Dict[str, float]) -> HomeostaticState:
        """Measure the drift between system perception and reality."""
        
        # Simple Euclidean drift as a placeholder for Fisher-Rao
        p_vec = np.array([perception_moments.get(k, 0.0) for k in ["return", "vol"]])
        r_vec = np.array([reality_moments.get(k, 0.0) for k in ["return", "vol"]])
        drift = float(np.linalg.norm(p_vec - r_vec))
        
        # 1. Sensitivity Tuning
        # If drift is high (Surprise), increase the gain on 'Sensing' to find the cause
        # If drift is low (Stasis), decrease gain to save energy
        gain_scalar = 1.0 + (drift * 2.0)
        new_gains = {k: min(2.0, v * gain_scalar) for k, v in self.default_gains.items()}
        
        is_balanced = drift < 0.1
        
        if drift > 0.5:
            desc = "SENSORY DISSONANCE: Major drift from reality. Increasing gain."
        elif drift < 0.05:
            desc = "SENSORY HOMEOSTASIS: Perception and reality are in alignment."
        else:
            desc = "Sensing is currently calibrated."
            
        return HomeostaticState(
            geometric_drift=drift,
            current_gains=new_gains,
            is_balanced=is_balanced,
            description=desc
        )

    def generate_calibration_report(self, state: HomeostaticState) -> str:
        """Produce a report on the system's homeostatic balance."""
        lines = [
            "HOMEOSTATIC CALIBRATION REPORT",
            f"  • Geometric Drift: {state.geometric_drift:.4f}",
            f"  • System Balance: {'STABLE' if state.is_balanced else 'UNSTABLE'}",
            f"  • Description: {state.description}",
            "  • Sensitivity Gains:"
        ]
        for sense, gain in state.current_gains.items():
            lines.append(f"    - {sense.capitalize()}: {gain:.2f}x")
            
        return "\n".join(lines)
