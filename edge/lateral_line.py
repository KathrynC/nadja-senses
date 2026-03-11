"""Pattern 2: The Lateral Line (Pressure Gradient Sensing)

Implements the lateral line — a sensory organ that detects minute vibrations 
and pressure changes in the global data stream. Following fish biology, 
it senses approaching 'shocks' before they reach the exteroceptive receptors.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any
import numpy as np

@dataclass
class ShiverSignal:
    """A minute vibration detected in the distal data stream."""
    source: str
    vibration_intensity: float
    pressure_gradient: float
    description: str
    smell_mapping: str

class LateralLineObserver:
    """The 'Whisker Array' of the sensorium. Senses semantic pressure."""
    
    def __init__(self):
        self.observers = ["ARXIV", "NEWS", "ENVIRONMENTAL", "SOCIAL"]

    def sense_shivers(self, external_flux: Dict[str, float]) -> List[ShiverSignal]:
        """Detect vibrations and pressure gradients in external data flux."""
        shivers = []
        
        # 1. NEWS VIBRATION: rapid increase in arrival rate
        news_flux = external_flux.get("news_arrival_rate", 1.0)
        if news_flux > 2.5:
            shivers.append(ShiverSignal(
                "NEWS", 0.82, 0.45, 
                "High-frequency narrative vibration detected.", 
                "popcorn"
            ))
            
        # 2. INTEL PRESSURE: specific spikes in 'Intelligence Horizon'
        arxiv_flux = external_flux.get("arxiv_salience", 0.5)
        if arxiv_flux > 0.8:
            shivers.append(ShiverSignal(
                "ARXIV", 0.31, 0.88, 
                "Heavy semantic pressure gradient from the Intelligence Horizon.", 
                "woody"
            ))
            
        # 3. ENVIRONMENTAL SHIVER: nonlinear shifts in physical data
        eco_flux = external_flux.get("climate_anomaly", 0.0)
        if abs(eco_flux) > 1.5:
            shivers.append(ShiverSignal(
                "ENVIRONMENTAL", 0.95, 0.15, 
                "Planetary shiver detected. Large anomaly in non-human system.", 
                "sulfurous"
            ))
            
        return shivers

    def generate_shiver_report(self, shivers: List[ShiverSignal]) -> str:
        """Produce a report on approaching 'pressure waves'."""
        if not shivers:
            return "THE WATER IS STILL. NO PRESSURE GRADIENTS DETECTED."
            
        lines = ["LATERAL LINE / SHIVER REPORT"]
        for s in shivers:
            lines.append(f"  • {s.source}: VIBRATION {s.vibration_intensity:.2f} | GRADIENT {s.pressure_gradient:.2f}")
            lines.append(f"    {s.description}")
        
        return "\n".join(lines)
