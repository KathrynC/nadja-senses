"""Pattern 25: Grapho-Sensation (Visual Typography)

Implements the somatic sense of type — mapping manifold tension 
directly to typographic muscle (Font Weight, Skew, Spacing). 
Part of the Sense of Sight.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Any

@dataclass
class TypeMuscle:
    """The physical 'tension' of a typographic output."""
    font_weight: int # 100 to 900
    skew_degrees: float # -20 to 20
    letter_spacing_em: float # -0.1 to 0.5
    label: str

class TypographyObserver:
    """Senses and renders the tension of the manifold via text geometry."""
    
    def sense_type_tension(self, volatility: float, pressure: float) -> TypeMuscle:
        """Map volatility and pressure to typographic parameters."""
        
        # High volatility → Heavy font weight (Muscular stress)
        weight = int(400 + (volatility * 500))
        weight = max(100, min(900, weight))
        
        # High pressure → Skew (The manifold is tilting)
        skew = pressure * 15.0
        
        # Low liquidity/Stasis → Tight spacing; High excitement → Wide spacing
        spacing = (volatility * 0.3) - 0.05
        
        if weight > 700:
            label = "TYPOGRAPHIC BRUISE: MANIFOLD UNDER HEAVY TENSION"
        elif abs(skew) > 10:
            label = "TYPOGRAPHIC TILT: REGIME SHIFT DETECTED"
        else:
            label = "NORMAL TYPEFACE BALANCE"
            
        return TypeMuscle(
            font_weight=weight,
            skew_degrees=skew,
            letter_spacing_em=round(spacing, 2),
            label=label
        )
