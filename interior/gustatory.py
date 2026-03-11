"""Pattern 13: The Interoceptive Tongue (Portfolio Taste)

Implements the sense of Taste as an interoceptive audit of owned positions.
Evaluates 'nourishment' (profit/thesis alignment) and 'toxicity' (loss/decay).
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any
import numpy as np

@dataclass
class PositionTaste:
    """The taste of a single owned position."""
    ticker: str
    dominant_channel: str
    intensity: float
    description: str
    channels: Dict[str, float] = field(default_factory=dict)

class GustatoryObserver:
    """The 'Tongue' of the sensorium. Requires contact (ownership)."""
    
    def __init__(self):
        self.channels = [
            "sweet", "bitter", "sour", "salty", "umami", 
            "oleogustus", "kokumi", "astringent"
        ]

    def taste_portfolio(self, positions: List[Dict[str, Any]]) -> List[PositionTaste]:
        """Audit the taste of all owned positions."""
        tastes = []
        for pos in positions:
            p_l = pos.get("unrealized_pnl_pct", 0.0)
            thesis_match = pos.get("thesis_alignment", 0.5) # 0 to 1
            liquidity = pos.get("liquidity_score", 0.5)
            concentration = pos.get("weight_pct", 0.0)
            
            c = {ch: 0.0 for ch in self.channels}
            
            # 1. SWEET: Profit + Thesis (Nourishing)
            if p_l > 0 and thesis_match > 0.7:
                c["sweet"] = min(1.0, p_l * 5.0)
            
            # 2. BITTER: Loss + Broken Thesis (Toxic)
            if p_l < -0.05 and thesis_match < 0.3:
                c["bitter"] = min(1.0, abs(p_l) * 4.0)
                
            # 3. SOUR: Profit without Thesis (Spoiled/Lucky)
            if p_l > 0.1 and thesis_match < 0.4:
                c["sour"] = 0.8
                
            # 4. SALTY: Stability/Cash-like
            if abs(p_l) < 0.01:
                c["salty"] = 0.5
                
            # 5. OLEOGUSTUS: High Concentration (Fat)
            if concentration > 0.15:
                c["oleogustus"] = min(1.0, concentration * 2.0)
                
            # 6. ASTRINGENT: Illiquidity (Dry)
            if liquidity < 0.2:
                c["astringent"] = 0.9
                
            # Determine dominant channel
            dom = max(c, key=c.get)
            
            tastes.append(PositionTaste(
                ticker=pos["ticker"],
                dominant_channel=dom,
                intensity=c[dom],
                description=self._get_description(dom),
                channels=c
            ))
        return tastes

    def _get_description(self, channel: str) -> str:
        descriptions = {
            "sweet": "Nourishing. Profit and thesis are in alignment.",
            "bitter": "Toxic. Position is failing both financially and logically.",
            "sour": "Spoiled. Gains without clear thesis — risk of reversal.",
            "salty": "Stable. Baseline mineral energy.",
            "umami": "Deep resonance. High information value.",
            "oleogustus": "Fatty. High concentration risk.",
            "kokumi": "Hearty. Cross-modal sensory confirmation.",
            "astringent": "Dry. Exit friction detected (illiquidity)."
        }
        return descriptions.get(channel, "Neutral.")

    def generate_tasting_menu(self, tastes: List[PositionTaste]) -> str:
        """Produce a report on the portfolio's internal health."""
        if not tastes:
            return "THE TONGUE IS DRY. NO POSITIONS TO TASTE."
            
        lines = ["PORTFOLIO TASTING MENU (INTEROCEPTIVE AUDIT)"]
        for t in tastes:
            lines.append(f"  • {t.ticker}: {t.dominant_channel.upper()} (Intensity: {t.intensity:.2f})")
            lines.append(f"    {t.description}")
            if t.dominant_channel == "bitter":
                lines.append("    FEEDBACK: Triggers PUTRID olfactory signal in global sensorium.")
        
        return "\n".join(lines)
