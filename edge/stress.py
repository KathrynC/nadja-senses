"""Pattern 36: Vulnerability Mapping (Stress Perception)

Implements active stress sensing based on the Cramer methodology. 
Perceives the structural robustness of the manifold by interrogating 
boundary conditions and compound stress scenarios.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional

@dataclass
class VulnerabilityProfile:
    """A map of structural weaknesses in the current manifold."""
    target_id: str
    resilience_score: float # 0.0 (Fragile) to 1.0 (Robust)
    critical_failure_point: str # The scenario that breaks the system
    vulnerability_depth: float # Magnitude of the 'regret'
    description: str

class StressObserver:
    """The 'Structural Engineer' of the sensorium. Senses breaking points."""
    
    def __init__(self, simulation_results: List[Dict[str, Any]]):
        self.results = simulation_results

    def sense_vulnerabilities(self, protocol_id: str) -> VulnerabilityProfile:
        """Analyze a protocol's performance across stress scenarios."""
        # This will eventualy link to resilience_summary and vulnerability_profile
        
        # Simple heuristic: find the scenario with the max drawdown
        worst_case = min(self.results, key=lambda x: x.get("final_value", 1.0))
        drawdown = worst_case.get("max_drawdown", 1.0)
        
        resilience = 1.0 - drawdown
        
        if resilience < 0.3:
            desc = f"FRAGILITY ALERT: Protocol {protocol_id} is vulnerable to {worst_case.get('scenario_name')}."
        elif resilience > 0.8:
            desc = f"ROBUSTNESS CONFIRMED: Protocol {protocol_id} shows high structural integrity."
        else:
            desc = "Vulnerability levels are within normal bounds."
            
        return VulnerabilityProfile(
            target_id=protocol_id,
            resilience_score=resilience,
            critical_failure_point=worst_case.get("scenario_name", "UNKNOWN"),
            vulnerability_depth=drawdown,
            description=desc
        )

    def generate_robustness_report(self, profiles: List[VulnerabilityProfile]) -> str:
        """Produce a report on the 'Structural Stress' of the manifold."""
        if not profiles:
            return "NO STRESS DATA AVAILABLE."
            
        lines = ["STRUCTURAL ROBUSTNESS / VULNERABILITY REPORT"]
        for p in profiles:
            lines.append(f"  • {p.target_id}: RESILIENCE {p.resilience_score:.2f}")
            lines.append(f"    Critical Break: {p.critical_failure_point}")
            lines.append(f"    {p.description}")
        
        return "\n".join(lines)
