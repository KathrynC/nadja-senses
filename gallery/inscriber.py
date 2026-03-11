"""Pattern 4: The Inscription Wall (Synthesis Logic)

The 'Curator' of the sensorium. Synthesizes multi-modal gestalts into 
a unified 'Day Inscription' dashboard.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from nadja_senses.gallery.thinkers.lenses import THINKERS, ThinkerLens

@dataclass
class DayInscription:
    """The final synthesized output of a sensory cycle."""
    gestalt_label: str
    radar_data: Dict[str, float]
    trajectory_summary: str
    thinker_interpretations: List[Dict[str, str]]
    divergence_alerts: List[str]
    typographic_state: str

class InscriptionWall:
    """Synthesizes the 30 patterns into a unified visual/poetic surface."""
    
    def synthesize(
        self, 
        smell_gestalt: str,
        nmf_activations: Dict[str, float],
        trajectory_desc: str,
        divergences: List[str],
        type_label: str
    ) -> DayInscription:
        """Create a unified Inscription from all senses."""
        
        # 1. Gather Thinker interpretations
        interpretations = []
        salience = max(nmf_activations.values()) if nmf_activations else 0.5
        for thinker in THINKERS.values():
            interpretations.append({
                "thinker": thinker.name,
                "text": thinker.interpret(smell_gestalt, salience)
            })
            
        return DayInscription(
            gestalt_label=smell_gestalt,
            radar_data=nmf_activations,
            trajectory_summary=trajectory_desc,
            thinker_interpretations=interpretations,
            divergence_alerts=divergences,
            typographic_state=type_label
        )

    def render_display(self, inscription: DayInscription) -> str:
        """Produce a text-based mockup of the Day Inscription."""
        lines = [
            f"--- NADJA DAY INSCRIPTION ---",
            f"GESTALT: {inscription.gestalt_label}",
            f"TYPE: {inscription.typographic_state}",
            f"\nINTRADAY TRAJECTORY:",
            f"  {inscription.trajectory_summary}",
            f"\nDIVERGENCES:",
            *[f"  ⚠ {d}" for d in inscription.divergence_alerts],
            f"\nTHINKER LENSES:"
        ]
        for interp in inscription.thinker_interpretations:
            lines.append(f"  [{interp['thinker']}]: {interp['text'][:80]}...")
            
        return "\n".join(lines)
