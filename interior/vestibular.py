"""Pattern 15: The Vestibular Balance (Regime Acceleration)

Implements the vestibular sense — the system's ability to sense balance, 
spatial orientation, and acceleration (regime switching).
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any
import numpy as np

@dataclass
class VestibularState:
    current_regime: str
    tilt_velocity: float # Rate of change of regime probability
    acceleration: float  # Second derivative of momentum
    is_balanced: bool
    description: str

class VestibularObserver:
    """The 'Inner Ear' of the sensorium. Monitors balance and tilt."""
    
    def __init__(self):
        self.regimes = ["BULL", "BEAR", "CRISIS", "RECOVERY"]

    def sense_balance(self, state_history: List[Dict[str, float]]) -> VestibularState:
        """Sense the 'tilt' and 'acceleration' of the manifold."""
        if len(state_history) < 3:
            return VestibularState("BULL", 0.0, 0.0, True, "Stable orientation.")
            
        # Extract momentum series
        moms = [h.get("momentum", 0.0) for h in state_history]
        vel = moms[-1] - moms[-2]
        prev_vel = moms[-2] - moms[-3]
        accel = vel - prev_vel
        
        # Sense 'tilt' (proximity to regime boundary)
        regime = state_history[-1].get("regime", 0.0)
        is_balanced = abs(accel) < 0.05
        
        if accel > 0.1:
            desc = "Sudden upward tilt. System accelerating toward new attractor."
        elif accel < -0.1:
            desc = "Sudden downward tilt. Vertigo detected."
        else:
            desc = "Balanced trajectory."
            
        return VestibularState(
            current_regime=self.regimes[int(np.clip(regime, 0, 3))],
            tilt_velocity=vel,
            acceleration=accel,
            is_balanced=is_balanced,
            description=desc
        )
