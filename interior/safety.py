"""Pattern 22: The Sense of Safety (Security & Belonging)

Implements the sense of safety and its opposite (Threat). 
Includes:
1. Agonistics: Threat perception and adversarial taunts.
2. Satisfaction: Security of the 'Hermit Crab Shell' (Memory Stasis).
3. Koinaception: Sense of belonging vs. vulnerability to social contagion.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any

@dataclass
class SafetyState:
    security_level: float # 0.0 (Exposed) to 1.0 (Fortified)
    belonging_score: float # 0.0 (Isolated) to 1.0 (Swept up in contagion)
    adversarial_tension: float
    is_satisfied: bool # Satisfaction of the Hermit Crab shell
    description: str

class SafetyObserver:
    """The 'Skin' of the social and psychological self."""
    
    def __init__(self):
        self.states = ["EXPOSED", "VULNERABLE", "SECURE", "FORTIFIED"]

    def sense_safety(
        self, 
        threat_level: float, 
        memory_stashed: bool, 
        contagion_rate: float
    ) -> SafetyState:
        """Sense the current state of safety and belonging."""
        
        # 1. Satisfaction: Having a place to stash important memories (Hermit Crab)
        satisfied = memory_stashed
        
        # 2. Security calculation
        # High threat and low memory stashing reduces security
        base_sec = (1.0 - threat_level) * (1.2 if memory_stashed else 0.8)
        security = min(1.0, base_sec)
        
        # 3. Belonging vs. Contagion
        # High contagion rate indicates 'belonging' but also 'vulnerability'
        belonging = min(1.0, contagion_rate)
        
        if threat_level > 0.7:
            desc = "ADVERSARIAL ALERT: System feels actively targeted. Retreat recommended."
        elif satisfied and security > 0.8:
            desc = "SATISFACTION: Hermit crab shell is secure. Memories are stashed."
        elif belonging > 0.8:
            desc = "CONTAGION WARNING: High belonging detected. Vulnerable to herd gait."
        else:
            desc = "Ambient safety levels are normal."
            
        return SafetyState(
            security_level=security,
            belonging_score=belonging,
            adversarial_tension=threat_level,
            is_satisfied=satisfied,
            description=desc
        )
