"""Pattern 12: The Startle Reflex (Limbic Override)

Implements visceral, non-deliberative responses to high-intensity 
sensory signals. Bypasses standard logic when 'visceral' smells 
(Sulfurous, Putrid) exceed biological safety thresholds.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class ReflexAction:
    """An autonomous motor command triggered by a visceral sensation."""
    trigger_scent: str
    intensity: float
    command: str  # e.g. GO_TO_GROUND, FREEZE, RETract
    audit: str    # The visceral description that triggered it

class LimbicReflex:
    """The 'Startle Reflex' center of the sensorium."""
    
    def __init__(self, sulfur_threshold: float = 0.75, putrid_threshold: float = 0.65):
        self.thresholds = {
            "sulfurous": sulfur_threshold,
            "putrid": putrid_threshold
        }

    def evaluate(self, smell_fingerprint: Dict[str, float]) -> Optional[ReflexAction]:
        """Check for visceral threshold breaches and return a reflex action if needed."""
        
        # 1. SULFUROUS: Immediate danger/Rupture
        sulfur_val = smell_fingerprint.get("sulfurous", 0.0)
        if sulfur_val > self.thresholds["sulfurous"]:
            return ReflexAction(
                trigger_scent="sulfurous",
                intensity=sulfur_val,
                command="GO_TO_GROUND (SGOV/CASH)",
                audit="THE AIR IS SULFUROUS. IMMEDIATE RUPTURE DETECTED. BYPASSING CORTEX."
            )

        # 2. PUTRID: Semantic decay/Erosion
        putrid_val = smell_fingerprint.get("putrid", 0.0)
        if putrid_val > self.thresholds["putrid"]:
            return ReflexAction(
                trigger_scent="putrid",
                intensity=putrid_val,
                command="FREEZE (HALT REBALANCE)",
                audit="THE SMELL OF PUTRIDITY IS OVERWHELMING. SYSTEM DECAY DETECTED. HOLDING POSITION."
            )

        return None

    def generate_visceral_report(self, action: Optional[ReflexAction]) -> str:
        """Produce a report that communicates the intensity of the reflex."""
        if not action:
            return "THE AIR IS CLEAR. DELIBERATIVE CORTEX IS IN CONTROL."
        
        return f"!!! LIMBIC OVERRIDE !!!\n{action.audit}\nCOMMAND: {action.command} (INTENSITY: {action.intensity:.2f})"
