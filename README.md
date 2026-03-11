# NADJA Senses

A specialized framework for **Semantic Pressure Sensing**, structured as a series of **Edge Environments** following Christopher Alexander's *Pattern Language*.

This toolkit treats sensory integration as a "living" organism, metabolizing raw world entropy into the structural beauty of the Memory Palace.

## Core Patterns

1.  **The Common Language:** A 10D Olfactory Algebra (Castro NMF) that normalizes all sensations (text, weather, price).
2.  **The Entrance Transition:** The "Lateral Line" edge where external observers (Arxiv, News, Climate) produce normalized "shivers."
3.  **Light on Two Sides:** A divergence-detection system that requires multi-domain confirmation for any major signal.
4.  **The Inscription Wall:** A synthesis layer that translates sensory gestalts into narrative strategies via Thinker Lenses (Banks, Lovecraft, Poincaré).
5.  **Thick Walls:** Normalization filters that prevent "Data Cannibalism" by transforming raw data into high-animacy archetypes.
6.  **The Cascading Flow:** Sensory tracking of "Deep Time" (Underland) and systemic change (Chronos).
7.  **The Rhythmic Pulse:** Acoustic analysis of meter, prosody, and sonic motifs (IAMBIC pulse vs. BEBOP rupture).
8.  **The Homophone Synapse:** Detection and resolution of "semantic homophones"—signals that sound the same but originate from disjoint regimes.

## Installation

```bash
pip install .
```

## Usage

### 1. Compute an Olfactory Gestalt

```python
from nadja_senses.core.nmf_algebra import compute_gestalt

activations = {
    "citrus": 0.022,
    "sulfurous": 0.014,
    "putrid": -0.006
}

print(compute_gestalt(activations))
# Output: CITRUS-SULFUROUS WITH PUTRID UNDERTONE
```

### 2. Use a Thinker Lens

```python
from nadja_senses.gallery.thinkers.lenses import THINKERS

banks = THINKERS["iain_banks"]
print(banks.perspective)

### 3. Scan the Rhythmic Pulse

```python
from nadja_senses.interior.acoustic import AcousticObserver

history = [
    {"volatility": 0.5, "momentum": 0.01},
    {"volatility": 1.8, "momentum": 0.03}, # Stressed syllable (/)
    {"volatility": 0.4, "momentum": 0.01}, # Unstressed (u)
    {"volatility": 2.1, "momentum": 0.04}  # Stressed (/)
]

gestalt = AcousticObserver.scan_ode_rhythm(history)
print(f"Foot: {gestalt.foot}, Audit: {gestalt.audit}")
# Output: Foot: IAMBIC, Audit: Healthy pulse. Steady motion.

### 4. Detect Semantic Puns

```python
from nadja_senses.interior.homophone import HomophoneObserver

active_signals = [
    {"motif": "spike", "domain": "liquidity", "description": "Injection of capital"},
    {"motif": "spike", "domain": "volatility", "description": "Margin call cascade"}
]

observer = HomophoneObserver()
rhymes = observer.detect_rhymes(active_signals)
print(observer.generate_pun_report(rhymes))
# Output: A 'pun' on spike indicates a high-divergence state.
```
```
```

## Philosophical Foundation: Rejecting Data Cannibalism

In the NADJA ecosystem, this repository serves as the **Thick Wall** against epistemic decay. By grounding the system in external facts (Wolfram), natural shivers (Lateral Line), and high-animacy literature, we ensure the simulation encounters the world rather than consuming its own synthetic output.

## License

MIT
