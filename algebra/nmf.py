"""Pattern 1: The Common Language (Olfactory Algebra)

Implements the Castro et al. (2013) NMF decomposition of human olfaction.
Provides the 10-dimensional latent space used to normalize all sensory signals.
"""
from __future__ import annotations
from typing import Dict, List, Any, Tuple
import numpy as np

SMELL_CATEGORIES = [
    "fragrant", "woody", "citrus", "fruity", "chemical",
    "minty", "sweet", "popcorn", "putrid", "sulfurous"
]

def normalize_vector(v: Dict[str, float]) -> Dict[str, float]:
    """Normalize a smell vector so the sum of absolute values is 1.0."""
    total = sum(abs(val) for val in v.values())
    if total < 1e-10:
        return v
    return {k: val / total for k, val in v.items()}

def compute_gestalt(activations: Dict[str, float]) -> str:
    """Produce a human-readable gestalt scent description."""
    sorted_cats = sorted(activations.items(), key=lambda x: abs(x[1]), reverse=True)
    primary = [cat for cat, val in sorted_cats if val > 0.001][:2]
    negative = [cat for cat, val in sorted_cats if val < -0.001][:1]

    parts = []
    if primary:
        parts.append("-".join(primary))
    if negative:
        parts.append(f"with {negative[0]} undertone")
    
    return " ".join(parts) if parts else "neutral"
