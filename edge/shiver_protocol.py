"""Pattern 2: The Entrance Transition (Shiver Protocol)

Formalizes the interface for "observers" — modules that scan external 
data sources and produce normalized "shivers" (motifs, salience, and smells).
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Protocol, runtime_checkable
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Observation:
    """A single raw data point captured by an observer."""
    source: str
    category: str
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class EncounterSignal:
    """A normalized sensory signal mapped to the Olfactory Algebra."""
    expert_id: str
    motif: str
    salience: float  # 0.0 to 1.0
    description: str
    smell_fingerprint: Dict[str, float] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)

@runtime_checkable
class ObserverProtocol(Protocol):
    """Protocol for all lateral-line observers."""
    
    name: str
    
    def scan(self, **kwargs: Any) -> List[Observation]:
        """Scan the data source and return raw observations."""
        ...

    def interpret(self, observations: List[Observation]) -> List[EncounterSignal]:
        """Normalize observations into EncounterSignals via Smell Algebra."""
        ...

class BaseObserver:
    """Standard base class for observers."""
    def __init__(self, name: str):
        self.name = name

    def scan(self, **kwargs: Any) -> List[Observation]:
        return []

    def interpret(self, observations: List[Observation]) -> List[EncounterSignal]:
        return []
