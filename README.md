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
```

## Philosophical Foundation: Rejecting Data Cannibalism

In the NADJA ecosystem, this repository serves as the **Thick Wall** against epistemic decay. By grounding the system in external facts (Wolfram), natural shivers (Lateral Line), and high-animacy literature, we ensure the simulation encounters the world rather than consuming its own synthetic output.

## License

MIT
