"""Pattern 21: Topoception (The Sense of Place)

Implements a unified sense of location across heterogeneous coordinate systems.
Deepened to include Scenario-based thinking and Storyline location.
Answers: "What Planet are we on?" and "Where do we go from here?"
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Tuple
import numpy as np

@dataclass
class Coordinate:
    """A multi-dimensional coordinate representing a location."""
    system: str  # GEO, ODE, PALACE, SMELL, SCENARIO
    values: Dict[str, Any]
    label: str

@dataclass
class TrajectoryVector:
    """The inferred path from the current location into the future."""
    current_planet: str # EARTH, MARS, VENUS, JUPITER
    storyline_phase: str # BEGINNING, MIDDLE, END, RUPTURE
    next_step_motif: str # Inferred from CA rules
    velocity: float
    confidence: float

class LocationObserver:
    """The 'Internal GPS' of the sensorium. Senses Place and Storyline."""
    
    def __init__(self, palace_map: Optional[Dict[str, str]] = None):
        self.palace_map = palace_map or {}
        self.planets = ["EARTH", "MARS", "VENUS", "JUPITER"]

    def sense_location(
        self, 
        geo: Optional[Tuple[float, float]] = None,
        ode_state: Optional[np.ndarray] = None,
        palace_room: Optional[str] = None,
        smell_vector: Optional[Dict[str, float]] = None,
        scenario_id: Optional[str] = None
    ) -> List[Coordinate]:
        """Sense current position across all available systems."""
        coords = []
        
        if geo:
            coords.append(Coordinate("GEO", {"lat": geo[0], "lon": geo[1]}, f"At ({geo[0]}, {geo[1]})"))
            
        if ode_state is not None:
            coords.append(Coordinate(
                "ODE", 
                {"regime": float(ode_state[6]), "leverage": float(ode_state[1])},
                f"In Regime {int(ode_state[6])} with {ode_state[1]:.2f} leverage."
            ))
            
        if palace_room:
            zone = self.palace_map.get(palace_room, "unknown")
            coords.append(Coordinate("PALACE", {"room": palace_room, "zone": zone}, f"Inside {palace_room} ({zone})."))
            
        if scenario_id:
            # "What Planet are we on?" inference
            # Heuristic: map scenario_id or stress to planet
            planet = self.planets[0] # Default to Earth
            if "crisis" in scenario_id or "rupture" in scenario_id:
                planet = "MARS"
            elif "transformation" in scenario_id:
                planet = "JUPITER"
            coords.append(Coordinate("SCENARIO", {"id": scenario_id, "planet": planet}, f"On Planet {planet} (Scenario: {scenario_id})."))
            
        return coords

    def infer_trajectory(self, current_coords: List[Coordinate], ca_fired_rules: List[str]) -> TrajectoryVector:
        """Infer the 'Where do we go from here?' storyline vector."""
        # 1. Identify current planet from coordinates
        planet = "EARTH"
        for c in current_coords:
            if c.system == "SCENARIO":
                planet = c.values.get("planet", "EARTH")
        
        # 2. Map CA rules to next-step motifs
        next_motif = ca_fired_rules[0] if ca_fired_rules else "CONTINUATION"
        
        # 3. Determine phase
        # (This would be more complex in full implementation)
        phase = "MIDDLE" if len(ca_fired_rules) > 5 else "BEGINNING"
        
        return TrajectoryVector(
            current_planet=planet,
            storyline_phase=phase,
            next_step_motif=next_motif,
            velocity=0.5,
            confidence=0.8
        )

    def generate_location_report(self, coords: List[Coordinate], vector: Optional[TrajectoryVector] = None) -> str:
        """Produce a unified 'Sense of Place' and 'Storyline' report."""
        if not coords:
            return "LOCATION UNKNOWN. FLOATING IN THE VOID."
            
        lines = ["TOPOCEPTION / SENSE OF PLACE & STORYLINE"]
        for c in coords:
            lines.append(f"  • {c.system}: {c.label}")
            
        if vector:
            lines.append(f"\nSTORYLINE VECTOR (Where we are going):")
            lines.append(f"  • Planet: {vector.current_planet}")
            lines.append(f"  • Phase: {vector.storyline_phase}")
            lines.append(f"  • Next Step: {vector.next_step_motif}")
            lines.append(f"  • Inferred via: Semantic Cellular Automata")
            
        return "\n".join(lines)
