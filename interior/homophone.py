"""Pattern 8: The Homophone Synapse (Semantic Rhyming)

Detects and resolves 'semantic homophones' — signals that share a surface 
similarity (sound the same) but originate from disjoint underlying regimes.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any

@dataclass
class SemanticRhyme:
    """A pair of signals that 'rhyme' semantically."""
    surface_pattern: str  # The shared 'sound' or appearance
    domain_a: str
    domain_b: str
    meaning_a: str
    meaning_b: str
    divergence_score: float  # How much the underlying 'smells' differ

class HomophoneObserver:
    """Senses rhymes and puns in the manifold's data stream."""
    
    def __init__(self):
        self.rhyme_registry = {
            "spike": [
                {"domain": "liquidity", "meaning": "Injection of capital", "smell": "FRAGRANT"},
                {"domain": "volatility", "meaning": "Margin call cascade", "smell": "SULFUROUS"}
            ],
            "freeze": [
                {"domain": "market", "meaning": "Liquidity drought", "smell": "PUTRID"},
                {"domain": "climate", "meaning": "Supply chain shock", "smell": "WOODY"}
            ]
        }

    def detect_rhymes(self, active_signals: List[Dict[str, Any]]) -> List[SemanticRhyme]:
        """Detect when active signals 'rhyme' on the surface."""
        rhymes = []
        # Group active signals by their surface pattern
        by_pattern = {}
        for sig in active_signals:
            pattern = sig.get("motif", "").lower()
            if pattern in self.rhyme_registry:
                if pattern not in by_pattern:
                    by_pattern[pattern] = []
                by_pattern[pattern].append(sig)
        
        # Identify divergences between rhyming signals
        for pattern, signals in by_pattern.items():
            if len(signals) >= 2:
                # Potential rhyme detected across domains
                rhymes.append(SemanticRhyme(
                    surface_pattern=pattern,
                    domain_a=signals[0].get("domain", "unknown"),
                    domain_b=signals[1].get("domain", "unknown"),
                    meaning_a=signals[0].get("description", ""),
                    meaning_b=signals[1].get("description", ""),
                    divergence_score=0.85 # Placeholder for actual NMF divergence
                ))
        return rhymes

    def generate_pun_report(self, rhymes: List[SemanticRhyme]) -> str:
        """Produce an interpretive report on semantic puns."""
        if not rhymes:
            return "The manifold is literal today. No puns detected."
        
        lines = ["SEMANTIC HOMOPHONE REPORT"]
        for r in rhymes:
            lines.append(f"  • Rhyme detected: '{r.surface_pattern}'")
            lines.append(f"    Domain A ({r.domain_a}): {r.meaning_a}")
            lines.append(f"    Domain B ({r.domain_b}): {r.meaning_b}")
            lines.append(f"    Resolution: A 'pun' on {r.surface_pattern} indicates a high-divergence state.")
        
        return "\n".join(lines)
