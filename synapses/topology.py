"""Pattern 37: Topological Foresight (Hypergraph Synapse)

Perceives the 'distance between worlds' by mapping the transition 
pathways between storyline archetypes using hypergraph topology.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any, Set
import numpy as np

@dataclass
class TransitionPathway:
    """A potential slip or jump between archetypes."""
    source_archetype: str
    target_archetype: str
    distance: float # Topological distance
    shared_indicators: Set[str]
    slip_risk: float # Probability of transition (0 to 1)
    description: str

class TopologicalSynapse:
    """The 'Structural Forecaster'. Senses the narrative topology."""
    
    def __init__(self, archetypes: List[Any]):
        self.archetypes = archetypes
        self.adjacency_matrix = self._build_topology()

    def _build_topology(self) -> Dict[str, Dict[str, float]]:
        """Calculate the static distance between archetypes based on shared keys."""
        topology = {}
        for a in self.archetypes:
            topology[a.name] = {}
            for b in self.archetypes:
                if a.name == b.name:
                    topology[a.name][b.name] = 0.0
                    continue
                
                # Jaccard-like distance between recognition keys
                keys_a = set(a.recognition_key.keys())
                keys_b = set(b.recognition_key.keys())
                shared = keys_a.intersection(keys_b)
                dist = 1.0 - (len(shared) / len(keys_a.union(keys_b)))
                topology[a.name][b.name] = dist
        return topology

    def sense_pathways(self, current_arch_name: str, vestibular_accel: float) -> List[TransitionPathway]:
        """Detect where the system is likely to 'slip' next."""
        pathways = []
        if current_arch_name not in self.adjacency_matrix:
            return []
            
        dists = self.adjacency_matrix[current_arch_name]
        
        for target, dist in dists.items():
            if dist == 0: continue
            
            # High vestibular acceleration increases slip risk
            risk = np.exp(-dist * 2.0) * (1.0 + vestibular_accel)
            
            if risk > 0.5:
                pathways.append(TransitionPathway(
                    source_archetype=current_arch_name,
                    target_archetype=target,
                    distance=dist,
                    shared_indicators=set(), # Placeholder
                    slip_risk=min(1.0, risk),
                    description=f"Topological proximity detected to {target}."
                ))
        
        return sorted(pathways, key=lambda x: x.slip_risk, reverse=True)

    def generate_topology_report(self, pathways: List[TransitionPathway]) -> str:
        """Produce a report on potential narrative jumps."""
        if not pathways:
            return "NARRATIVE TOPOLOGY IS STABLE. NO IMMEDIATE SLIPS DETECTED."
            
        lines = ["TOPOLOGICAL FORESIGHT / TRANSITION REPORT"]
        for p in pathways:
            lines.append(f"  • Pathway to {p.target_archetype}: RISK {p.slip_risk:.2f} (Dist: {p.distance:.2f})")
            lines.append(f"    {p.description}")
            if p.slip_risk > 0.8:
                lines.append("    WARNING: High-velocity transition imminent.")
        
        return "\n".join(lines)
