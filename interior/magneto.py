"""Pattern 17: Magnetoreception (Field Navigation)

Implements the sense of magnetoreception — the ability to perceive the 
'magnetic pull' of major market attractors and poles (USD, Gold, BTC).
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Any
import numpy as np

@dataclass
class MagneticPole:
    name: str
    strength: float # 0.0 to 1.0
    polarity: int # +1 (North/Attract), -1 (South/Repel)
    description: str

class MagnetoObserver:
    """The 'Internal Compass' of the sensorium. Senses field strength."""
    
    def __init__(self):
        self.poles = ["DXY_POLE", "GLD_POLE", "BTC_POLE"]

    def sense_field(self, market_levels: Dict[str, float]) -> List[MagneticPole]:
        """Sense the current magnetic field of the manifold."""
        detected = []
        
        # 1. DXY (US Dollar) strength acts as a North Pole for liquidity
        dxy = market_levels.get("DXY", 100.0)
        detected.append(MagneticPole(
            "DXY_POLE", 
            strength=min(1.0, dxy / 110.0), 
            polarity=1, 
            description="The pull of the Dollar is strong. Capital is migrating to the core."
        ))
        
        # 2. GLD (Gold) acts as a pole for stasis/protection
        gld_mom = market_levels.get("GLD_momentum", 0.0)
        if gld_mom > 0.02:
            detected.append(MagneticPole(
                "GLD_POLE", 
                strength=min(1.0, gld_mom * 10.0), 
                polarity=1, 
                description="Safety attraction detected. The manifold is tilting toward protection."
            ))
            
        return detected

    def generate_compass_report(self, poles: List[MagneticPole]) -> str:
        """Produce a navigation report based on magnetic pull."""
        if not poles:
            return "THE FIELD IS NEUTRAL. NO MAJOR POLES DETECTED."
            
        lines = ["MAGNETIC FIELD / NAVIGATION REPORT"]
        for p in poles:
            lines.append(f"  • {p.name}: STRENGTH {p.strength:.2f} ({p.description})")
        
        return "\n".join(lines)
