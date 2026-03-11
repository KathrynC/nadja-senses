"""Castro-informed Receptor Templates for NADJA Olfactory Algebra.

Maps financial and linguistic motifs to the 10-category Castro NMF space.
"""
from __future__ import annotations
from typing import Dict, List, Any

# ===================================================================
# Receptor Templates — Castro 10-Category NMF
# ===================================================================
# Each receptor is a dict of {component: weight}.
# Weights are normalized so each receptor sums to ~1.0 in abs value.

RECEPTOR_TEMPLATES = {
    "fragrant": {
        # High value, stable growth, positive resonance
        "bullish_momentum": 0.15,
        "structural_stability": 0.15,
        "clean_energy": 0.10,
        "innovation_breakthrough": 0.10,
        "high_trust": 0.10,
    },
    "woody": {
        # Deep structural fundamentals, industrial base, old growth
        "commodities": 0.15,
        "energy_fundamentals": 0.15,
        "infrastructure": 0.15,
        "theoretical_grounding": 0.15,
        "geological_stasis": 0.10,
    },
    "citrus": {
        # Fresh catalysts, new information, sharp innovation
        "tech_innovation": 0.15,
        "computational_finance": 0.15,
        "machine_learning": 0.15,
        "fresh_news_spike": 0.15,
        "innovation_signal": 0.10,
    },
    "fruity": {
        # Yield-seeking, income flows, "sweet" opportunities
        "income_flows": 0.15,
        "dividend_yield": 0.15,
        "market_harvest": 0.15,
        "consumer_staples": 0.15,
        "growth_sweetness": 0.10,
    },
    "chemical": {
        # Policy intervention, artificial stimulus, engineered signals
        "monetary_stimulus": 0.20,
        "fiat_injection": 0.15,
        "regulatory_intervention": 0.15,
        "synthetic_yield": 0.15,
        "engineered_narrative": 0.10,
    },
    "minty": {
        # Deflationary cleansing, cold regimes, structural correction
        "deflationary_pulse": 0.25,
        "structural_correction": 0.20,
        "deleveraging": 0.15,
        "cold_regime": 0.10,
        "system_purge": 0.10,
    },
    "sweet": {
        # Goldilocks conditions, speculative attraction, low friction
        "equities_rally": 0.15,
        "low_volatility": 0.15,
        "easy_credit": 0.15,
        "speculative_attraction": 0.10,
        "economic_stability": 0.10,
    },
    "popcorn": {
        # Overheating, late-cycle noise, speculative froth
        "late_cycle_froth": 0.15,
        "speculative_overhang": 0.15,
        "noisy_data": 0.10,
        "retail_mania": 0.10,
        "short_term_vol": 0.10,
    },
    "putrid": {
        # Credit rot, systemic decay, semantic erosion
        "credit_spread_widening": -0.20,
        "institutional_decay": -0.20,
        "semantic_erosion": -0.15,
        "bank_run_signal": -0.15,
        "systemic_rot": -0.10,
    },
    "sulfurous": {
        # Hidden danger, divergence, systemic rupture
        "yield_curve_inversion": -0.15,
        "cross_domain_divergence": -0.15,
        "geopolitical_rupture": -0.10,
        "risk_management_failure": -0.10,
        "hidden_cliff": -0.10,
    },
}

def compute_receptor_activation(
    active_motifs: Dict[str, float],
    receptor_template: Dict[str, float],
) -> float:
    """Compute activation of a single receptor against a set of active motifs."""
    activation = 0.0
    weight_sum = 0.0
    for motif, weight in receptor_template.items():
        if motif in active_motifs:
            activation += weight * active_motifs[motif]
            weight_sum += abs(weight)
    if weight_sum < 1e-10:
        return 0.0
    return activation / weight_sum

def compute_all_receptors(
    active_motifs: Dict[str, float]
) -> Dict[str, float]:
    """Compute activation for all 10 Castro NMF receptor categories."""
    activations = {}
    for category, template in RECEPTOR_TEMPLATES.items():
        activations[category] = compute_receptor_activation(active_motifs, template)
    return activations
