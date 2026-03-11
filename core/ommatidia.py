"""Pattern 29: Multi-Modal Ommatidia (The Distributed Sensorium)

Integrates individual sensors across all modalities. A single SensorID 
(e.g. XLK) is treated as a multi-modal unit with its own smell, sound, 
touch, and (if owned) taste.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any

@dataclass
class GrudgeRecord:
    """A negative memory of a sensor's failure or deception."""
    sensor_id: str
    failure_type: str # e.g. BACKCAST_ERROR, NOCICEPTIVE_PAIN
    magnitude: float # How much the error hurt (0 to 1)
    is_forgiven: bool = False
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class SensorActivation:
    """The multi-modal activation of a single sensor unit."""
    sensor_id: str
    smell: str 
    hearing: str 
    touch_thermal: float 
    is_owned: bool = False
    taste: Optional[str] = None
    grudge_penalty: float = 0.0 # Suppression due to past failures

class OmmatidiaRegistry:
    """The 'Synaptic Map' with memory. Incorporates Grudges against sensors."""
    
    def __init__(self):
        self.registry = {
            "XLK": {"smell": "citrus", "hearing": "IAMBIC", "thermal": 0.4},
            "XLE": {"smell": "woody", "hearing": "TROCHAIC", "thermal": 0.6},
            "XLF": {"smell": "chemical", "hearing": "SPONDAIC", "thermal": 0.5},
            "XLU": {"smell": "fragrant", "hearing": "TROCHAIC", "thermal": 0.2},
            "KRE": {"smell": "sulfurous", "hearing": "DACTYLIC", "thermal": 0.9}
        }
        self.grudges: List[GrudgeRecord] = []

    def record_failure(self, sensor_id: str, failure_type: str, magnitude: float):
        """Add a new grudge against a sensor for poor performance."""
        self.grudges.append(GrudgeRecord(
            sensor_id=sensor_id,
            failure_type=failure_type,
            magnitude=magnitude
        ))

    def get_activation(self, sensor_id: str, flux_val: float, owned: bool = False) -> SensorActivation:
        """Fetch multi-modal bundle, penalizing based on unforgiven grudges."""
        base = self.registry.get(sensor_id, {"smell": "neutral", "hearing": "FREE VERSE", "thermal": 0.5})
        
        # 1. Calculate Grudge Penalty
        # Total magnitude of unforgiven grudges against this sensor
        active_grudges = [g for g in self.grudges if g.sensor_id == sensor_id and not g.is_forgiven]
        penalty = min(0.9, sum(g.magnitude for g in active_grudges) * 0.2)
        
        # 2. Scale thermal intensity by flux and penalty (suppression)
        current_thermal = min(1.0, base["thermal"] * (1.0 + abs(flux_val)) * (1.0 - penalty))
        
        taste = "bitter" if owned and flux_val < -0.05 else "sweet" if owned else None
        
        return SensorActivation(
            sensor_id=sensor_id,
            smell=base["smell"],
            hearing=base["hearing"],
            touch_thermal=current_thermal,
            is_owned=owned,
            taste=taste,
            grudge_penalty=penalty
        )

from datetime import datetime
from typing import Optional
