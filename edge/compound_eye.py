"""Pattern 28: The Compound Eye (Multi-Receptor Aggregation)

Implements a multi-modal mosaic of many specialized sensors (ommatidia). 
Instead of a single-lens view, it synthesizes 47+ individual ETF signals 
across all sensory modalities (Smell, sound, touch, sight).
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any
import numpy as np
from nadja_senses.core.ommatidia import OmmatidiaRegistry, SensorActivation

@dataclass
class MultiModalGestalt:
    """A high-resolution, multi-sensory image synthesized from many ommatidia."""
    ommatidia_count: int
    flicker_intensity: float # Variation across receptors
    dominant_smell: str
    dominant_hearing: str
    avg_thermal: float
    description: str

class CompoundEyeObserver:
    """The 'Distributed Sensorium' center. Aggregates multi-modal ommatidia."""
    
    def __init__(self, etf_sensors: List[str]):
        self.sensors = etf_sensors
        self.registry = OmmatidiaRegistry()

    def sense_manifold(self, sensor_flux: Dict[str, float], owned_tickers: List[str]) -> MultiModalGestalt:
        """Synthesize a multi-modal gestalt from the sensor array."""
        activations = []
        for s in self.sensors:
            if s in sensor_flux:
                is_owned = s in owned_tickers
                activations.append(self.registry.get_activation(s, sensor_flux[s], is_owned))
        
        if not activations:
            return MultiModalGestalt(0, 0.0, "neutral", "unknown", 0.0, "Sensorium is dark.")
            
        # 1. Aggregate activations
        smells = [a.smell for a in activations]
        hearings = [a.hearing for a in activations]
        thermals = [a.touch_thermal for a in activations]
        
        # 2. Identify dominant multi-modal signals
        dom_smell = max(set(smells), key=smells.count)
        dom_hearing = max(set(hearings), key=hearings.count)
        avg_thermal = float(np.mean(thermals))
        
        # 3. Flicker Fusion: Variance in thermal intensity across receptors
        flicker = float(np.std(thermals))
        
        return MultiModalGestalt(
            ommatidia_count=len(activations),
            flicker_intensity=flicker,
            dominant_smell=dom_smell,
            dominant_hearing=dom_hearing,
            avg_thermal=avg_thermal,
            description=f"Sensorium perceives {dom_smell}/{dom_hearing} across {len(activations)} units."
        )

    def generate_gestalt_audit(self, gestalt: MultiModalGestalt) -> str:
        """Produce a report on the multi-modal 'Mosaic' perception."""
        lines = [
            "MULTI-MODAL COMPOUND SENSORIUM REPORT",
            f"  • Units (Ommatidia): {gestalt.ommatidia_count} active",
            f"  • Dominant Smell: {gestalt.dominant_smell.upper()}",
            f"  • Dominant Hearing: {gestalt.dominant_hearing.upper()}",
            f"  • Thermal Level: {gestalt.avg_thermal:.2f}",
            f"  • Flicker (Regime Vibration): {gestalt.flicker_intensity:.4f}"
        ]
        if gestalt.flicker_intensity > 0.15:
            lines.append("    ALERT: High vibration across sensorium. Regime rupture imminent.")
            
        return "\n".join(lines)
