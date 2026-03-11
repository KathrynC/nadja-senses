"""Pattern 14: Market Texture (The Somatosensory Surface)

Implements the sense of Touch as a multi-channel interrogation of market 
and portfolio state. Following biological somatosensation, it includes:
1. Thermoception: Volatility intensity (Cold to Hot).
2. Nociception: Pain and damage detection (Startle reflexes).
3. Interoception: Internal health (Portfolio taste/fullness).
4. Mechanoreception: Pressure and vibration (The shiver of the tape).
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any
import numpy as np

@dataclass
class HapticProfile:
    ticker: str
    thermo_score: float  # Volatility (Hot/Cold)
    noci_score: float    # Pain (Loss/Rupture)
    intero_score: float  # Health (Nourishment)
    mechano_score: float # Vibration (Noise)
    salience: float
    description: str

class HapticObserver:
    """The 'Skin' and 'Internal Nerves' of the sensorium."""
    
    def feel_state(self, ticker: str, data: Dict[str, Any]) -> HapticProfile:
        """Feel the 4 sub-channels of touch for a specific actor."""
        # 1. Thermoception (Volatility)
        vol = data.get("volatility", 0.0)
        thermo = min(1.0, vol * 1.5)
        
        # 2. Nociception (Pain/Loss)
        pnl = data.get("pnl_pct", 0.0)
        noci = min(1.0, abs(pnl) * 5.0) if pnl < -0.02 else 0.0
        
        # 3. Interoception (Internal Health/Liquidity)
        liq = data.get("liquidity", 0.5)
        intero = min(1.0, liq * 2.0)
        
        # 4. Mechanoreception (Vibration/Noise)
        noise = data.get("noise_ratio", 0.2)
        mechano = min(1.0, noise * 1.2)
        
        salience = max(thermo, noci, mechano)
        
        # Determine description based on highest channel
        if noci > 0.7:
            desc = "Nociceptive alert: The system is in pain."
        elif thermo > 0.7:
            desc = "Thermal alert: The manifold is running hot."
        else:
            desc = "Ambient tactile feedback stable."
            
        return HapticProfile(
            ticker=ticker,
            thermo_score=thermo,
            noci_score=noci,
            intero_score=intero,
            mechano_score=mechano,
            salience=salience,
            description=desc
        )
