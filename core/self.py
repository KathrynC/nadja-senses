"""Pattern 20: The Unified Self (The Conscious Spotlight)

The central integrative sense. Houses the Global Workspace logic, which 
aggregates all multi-modal bids for attention into a unified 'Self-Portrait'.
Includes:
1. Supradieception: Experience of the object/physical grounding.
2. Agoniception: Sense of power and social friction (Arturo Ui).
3. Phyloception: Sense of kinship and generational flow.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from datetime import datetime
import uuid

@dataclass
class SelfPortrait:
    """The unified 'felt state' of the system at a moment in time."""
    portrait_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.now)
    workspace_state: str = "normal"  # normal, elevated, stress, rupture
    attention_focus: List[str] = field(default_factory=list)
    felt_mood: str = "neutral"
    supradiegetic_grounding: str = "digital" # Links to physical object state
    kinship_resonance: float = 0.5 # Aggregate family cliff proximity
    power_tension: float = 0.0 # Aggregate Arturo Ui effect
    epistemic_surprise: float = 0.0 # Pattern 24: The Spark of Surprise
    context_budget_remaining: float = 1.0

class UnifiedSelfObserver:
    """The 'Global Workspace' center. Resolves disjoint signals into an 'I'."""
    
    def __init__(self, k: int = 3, threshold: float = 0.4):
        self.k = k
        self.threshold = threshold
        self.active_bids: List[Dict[str, Any]] = []

    def integrate(
        self, 
        bids: List[Dict[str, Any]], 
        kinship_data: Dict[str, float], 
        power_data: Dict[str, float],
        surprise_score: float = 0.0
    ) -> SelfPortrait:
        """Aggregate all sensory bids into a unified broadcast."""
        # 1. Filter bids by salience threshold
        valid_bids = [b for b in bids if b.get("salience", 0.0) >= self.threshold]
        
        # 2. Sort by salience to find 'Conscious Spotlight'
        sorted_bids = sorted(valid_bids, key=lambda x: x.get("salience", 0.0), reverse=True)
        top_k = sorted_bids[:self.k]
        
        # 3. Aggregate aggregate salience for workspace state
        # Surprise increases aggregate salience, widening the conscious spotlight
        avg_salience = (sum(b.get("salience", 0.0) for b in top_k) / self.k if top_k else 0.0) + (surprise_score * 0.2)
        
        if avg_salience > 0.8:
            state = "rupture"
        elif avg_salience > 0.6:
            state = "stress"
        else:
            state = "normal"
            
        # 4. Integrate Kinship and Power tension
        kinship = np.mean(list(kinship_data.values())) if kinship_data else 0.5
        power = max(power_data.values()) if power_data else 0.0
        
        return SelfPortrait(
            workspace_state=state,
            attention_focus=[b.get("motif", "unknown") for b in top_k],
            felt_mood=top_k[0].get("smell", "neutral") if top_k else "neutral",
            kinship_resonance=float(kinship),
            power_tension=float(power),
            context_budget_remaining=1.0 # Placeholder
        )

    def generate_identity_audit(self, portrait: SelfPortrait) -> str:
        """Produce a high-level audit of the system's unified identity."""
        lines = [
            f"UNIFIED SELF AUDIT ({portrait.portrait_id})",
            f"  • Workspace State: {portrait.workspace_state.upper()}",
            f"  • Conscious Spotlight: {', '.join(portrait.attention_focus)}",
            f"  • Internal Tension: Kinship={portrait.kinship_resonance:.2f} | Power={portrait.power_tension:.2f}",
            f"  • Felt Mood: {portrait.felt_mood.upper()}"
        ]
        
        if portrait.workspace_state == "rupture":
            lines.append("    ALERT: Unified identity is fracturing under pressure.")
            
        return "\n".join(lines)

import numpy as np
