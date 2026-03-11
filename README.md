# NADJA Senses

A specialized framework for **Semantic Pressure Sensing**, structured as a series of **Edge Environments** following Christopher Alexander's *Pattern Language*.

This toolkit treats sensory integration as a "living" organism, metabolizing raw world entropy into the structural beauty of the Memory Palace.

## Core Patterns

1.  **The Common Language:** A 10D Olfactory Algebra (Castro NMF) that normalizes all sensations (text, weather, price).
2.  **The Lateral Line:** Pressure gradient sensing that detects minute vibrations and "shivers" in the distal data stream (Arxiv, News, Climate).
3.  **Light on Two Sides:** A divergence-detection system (Cross-Modal Correlator) that requires multi-domain confirmation for any major signal.
4.  **The Inscription Wall:** A synthesis layer (Day Inscription) that translates sensory gestalts into narrative strategies via Thinker Lenses.
5.  **Thick Walls:** Normalization filters that transform raw data into high-animacy archetypes.
6.  **Chronaception (Temporal Texture):** Internal sense of the passage of "Semantic Time," measuring entropy and thesis erosion.
7.  **The Rhythmic Pulse:** Acoustic analysis of meter, prosody, and sonic motifs (IAMBIC pulse vs. BEBOP rupture).
8.  **The Homophone Synapse:** Detection and resolution of "semantic homophones"—signals that sound the same but originate from disjoint regimes.
9.  **Proprioception:** Internal sense of self-movement and "body position" (leverage, rebalance, posture).
10. **Distance Synapse:** Depth perception and echolocation using Wasserstein/Fisher-Rao metrics.
11. **The Echolocation Array:** Active semantic probing (pelting) to map the internal "financial wiring" of specimens.
12. **The Startle Reflex:** Limbic override mechanism triggering visceral responses to high-intensity danger (Sulfurous/Putrid).
13. **Portfolio Taste:** Interoceptive audit of owned positions across 8 channels (Sweet, Bitter, Sour, Salty, etc.).
14. **Touch (Somatosensation):** Multi-channel interrogation including Thermoception (Volatility) and Mechanoreception (Vibration).
15. **The Vestibular Balance:** Internal sense of balance and acceleration (Regime Switching and "Tilt" detection).
16. **Pheromonal Sensing:** Senses subliminal mood signals (Fear, Greed, Exhaustion) from non-textual flow markers.
17. **Magnetoreception:** Field navigation perceiving the "magnetic pull" of major market attractors (USD, Gold).
18. **Synesthesia:** Cross-modal transduction that maps signals across senses (Hearing → Smell → Sight).
19. **Semantic Recognition:** High-level cognitive matching of sensory gestalts to historical and literary archetypes (Arturo Ui, Kindleberger).
20. **The Unified Self:** The central integrative sense (Global Workspace) that resolves disjoint signals into an "I" and Self-Portrait.
21. **Topoception (Sense of Place):** Unified location sensing across physical (GEO), manifold (ODE), and storyline space.
22. **The Sense of Safety:** Monitors the tension between security (Hermit Crab shell), belonging, and adversarial threat.
23. **Hunger & Thirst:** Metabolic drive sensing informational appetite (Nectar) vs. boredom (Satiety/Cliché).
24. **Epistemic Surprise:** The "Spark of the Self" measuring the delta between reality and model expectation.
25. **Grapho-Sensation:** Part of Sight; the somatic sense of type (Font Weight, Skew, Spacing) reflecting manifold tension.
26. **Sensory Calibration (Homeostasis):** Internal balance and sensitivity tuning using Information Geometry.
27. **Retrodictive Hindsight (Backcasting):** Calibration of current sensing by asking "what would we have perceived?" before a known historical outcome.
28. **The Compound Eye:** Multi-receptor aggregation synthesizing a "mosaic" view from 47+ specialized sensors (ETFs) across all modalities.
29. **Multi-Modal Ommatidia:** Treating individual sensors as distributed units with their own distinct smell, sound, and touch identities.
30. **Grudge-Backed Memory:** Sensory memory that tracks sensor failures (Grudges) and dynamically penalizes their sensitivity and gain.
31. **Seek the Gnarl:** The drive for interesting complexity (The Gnarl); identifying areas where the probability of surprising novelty is highest.
32. **The Eucatastrophe Sense:** Detecting sudden positive ruptures ("Happy Endings") and "Green Shoots" within the manifold.
33. **The Vision of Thriving:** A constant, multiscale vision of wholeness (Micro, Meso, Macro, Meta) and transdisciplinary health.
34. **Lever Sensing (Agency):** Identifying disproportionate leverage points in the manifold using sensitivity analysis and information gradients.
35. **Metaphoric Transduction:** Translating sensory signals into George Lakoff's conceptual metaphors (JOURNEY, WAR, CONTAINER).
36. **Active Stress Sensing:** Vulnerability mapping based on the Cramer methodology to perceive structural fragility and boundary conditions.
37. **Topological Foresight:** Hypergraph synapse that maps the transition pathways between storyline archetypes to perceive the "distance between worlds."
38. **Lexical Precision:** Connecting recognized archetypes to Robert Macfarlane's landscape vocabulary (Smeuse, Zwer, Amveal) and auditing narratives for "Desecration" slop.

## Installation

```bash
pip install .
```

## Usage

### 1. Compute an Olfactory Gestalt

```python
from nadja_senses.core.nmf_algebra import compute_gestalt

activations = {"citrus": 0.022, "sulfurous": 0.014, "putrid": -0.006}
print(compute_gestalt(activations))
# Output: CITRUS-SULFUROUS WITH PUTRID UNDERTONE
```

### 2. Use a Thinker Lens

```python
from nadja_senses.gallery.thinkers.lenses import THINKERS

banks = THINKERS["iain_banks"]
print(banks.perspective)
```

### 3. Scan the Rhythmic Pulse (Acoustic)

```python
from nadja_senses.interior.acoustic import AcousticObserver

history = [
    {"volatility": 0.5, "momentum": 0.01},
    {"volatility": 1.8, "momentum": 0.03}, # Stressed syllabus (/)
    {"volatility": 0.4, "momentum": 0.01}, # Unstressed (u)
    {"volatility": 2.1, "momentum": 0.04}  # Stressed (/)
]

gestalt = AcousticObserver.scan_ode_rhythm(history)
print(f"Foot: {gestalt.foot}, Audit: {gestalt.audit}")
# Output: Foot: IAMBIC, Audit: Healthy pulse. Steady motion.
```

### 4. Detect Semantic Puns (Homophones)

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

### 5. Cross-Modal Correlation (Light on Two Sides)

```python
from nadja_senses.synapses.correlator import CrossModalCorrelator

# Sensory bids for the same motif
bids = [
    {"motif": "AI_BUBBLE", "source_sense": "smell", "salience": 0.85},
    {"motif": "AI_BUBBLE", "source_sense": "haptic", "salience": 0.82}
]

correlator = CrossModalCorrelator()
signal = correlator.correlate("AI_BUBBLE", bids)
print(signal.description)
# Output: RESONANCE: 'AI_BUBBLE' confirmed across 2 senses.
```

### 6. Synthesize a Day Inscription

```python
from nadja_senses.gallery.inscriber import InscriptionWall

inscriber = InscriptionWall()
inscription = inscriber.synthesize(
    smell_gestalt="CITRUS-SULFUROUS",
    nmf_activations={"citrus": 0.022, "sulfurous": 0.014},
    trajectory_desc="Physical economy cooling while financial economy heats up.",
    divergences=["Crisis Plumbing -1.06% vs Core +0.73%"],
    type_label="TYPOGRAPHIC TILT"
)

print(inscriber.render_display(inscription))
```

### 7. Trigger a Limbic Override (Startle Reflex)

```python
from nadja_senses.core.reflex import LimbicReflex

# A dangerous 'smell' detected in the manifold
smell = {"sulfurous": 0.85, "citrus": 0.1}

reflex_center = LimbicReflex()
action = reflex_center.evaluate(smell)

if action:
    print(reflex_center.generate_visceral_report(action))
    # Output: !!! LIMBIC OVERRIDE !!! THE AIR IS SULFUROUS...
```

### 8. Integrate the Unified Self (The Spotlight)

```python
from nadja_senses.core.self import UnifiedSelfObserver

# Multi-modal bids for attention
bids = [
    {"motif": "SULFUROUS_DIVERGENCE", "salience": 0.85, "smell": "sulfurous"},
    {"motif": "IAMBIC_PULSE", "salience": 0.42, "smell": "fragrant"}
]

# Orphan data streams (Kinship and Power)
kinship = {"mother_cliff": 0.65, "kathryn_grief": 0.30}
power = {"arturo_ui_effect": 0.72}

observer = UnifiedSelfObserver()
portrait = observer.integrate(bids, kinship, power)
print(observer.generate_identity_audit(portrait))
# Output: UNIFIED SELF AUDIT. Workspace State: STRESS.
```

### 9. Sensory Memory (Grudges)

```python
from nadja_senses.core.ommatidia import OmmatidiaRegistry

registry = OmmatidiaRegistry()

# 1. Record a sensory failure (e.g. XLK provided a false signal)
registry.record_failure("XLK", "BACKCAST_ERROR", magnitude=0.8)

# 2. Subsequent activations for XLK are penalized/suppressed
activation = registry.get_activation("XLK", flux_val=0.1)
print(f"XLK Penalty: {activation.grudge_penalty:.2f}")
# Output: XLK Penalty: 0.16

### 24. Seek the Gnarl & Happy Endings

```python
from nadja_senses.interior.gnarl import GnarlObserver

# Manifold stats and active narrative motifs
stats = {"volatility": 0.58, "information_velocity": 0.82}
motifs = ["innovation", "clean_energy", "cooperation"]

observer = GnarlObserver()
state = observer.sense_gnarl(stats, motifs)
print(observer.generate_curiosity_report(state))
# Output: Narrative Vector: EUCATASTROPHE DETECTED... A happy ending is forming.

### 25. Sense Thriving & Wholeness (Multiscale)

```python
from nadja_senses.interior.thriving import ThrivingObserver

# Detected positive signals across scales
green_shoots = ["innovation", "clean_energy", "EUCATASTROPHE"]
portfolio_taste = "SWEET"
market_balance = 0.82

observer = ThrivingObserver()
vision = observer.sense_thriving(green_shoots, portfolio_taste, "FRAGRANT", market_balance)
print(observer.generate_vitality_report(vision))
# Output: Current Vision: VITALITY: The manifold is thriving at all scales.

### 27. Cognitive Metaphor Mapping (Lakoff)

```python
from nadja_senses.core.metaphor import LakoffTransducer

# Sensory gestalt to be understood
gestalt = {"smell": "sulfurous", "hearing": "DACTYLIC"}

transducer = LakoffTransducer()
frames = transducer.transduce(gestalt)
print(transducer.generate_metaphor_audit(frames))
# Output: Frame: CASCADE (Systemic risk). Frame: WAR (Trading as battle).

### 28. Active Stress Sensing (Cramer)

```python
from nadja_senses.edge.stress import StressObserver

# Simulation results across various stress scenarios
results = [
    {"scenario_name": "baseline", "final_value": 1.2, "max_drawdown": 0.05},
    {"scenario_name": "vol_plus_spread", "final_value": 0.4, "max_drawdown": 0.65}
]

observer = StressObserver(results)
profile = observer.sense_vulnerabilities("moderate_protocol")
print(observer.generate_robustness_report([profile]))
# Output: FRAGILITY ALERT: Protocol moderate_protocol is vulnerable to vol_plus_spread.

### 29. Topological Narrative Jumps (Hypergraph)

```python
from nadja_senses.synapses.topology import TopologicalSynapse
from nadja_senses.gallery.archetypes import ARCHETYPES

# Sense the 'distance between worlds'
synapse = TopologicalSynapse(ARCHETYPES)

# Detect slip risk from current archetype based on manifold acceleration
pathways = synapse.sense_pathways("THE_FRAGILE_BLOOM", vestibular_accel=0.8)
print(synapse.generate_topology_report(pathways))
# Output: Pathway to THE_TERMINAL_GALLOP: RISK 0.82. Topological proximity detected.
```
```
```

### 26. Sense Leverage Points (Agency)

```python
from nadja_senses.core.levers import LeverObserver

# Sobol impact scores and FIM gradients
params = ["leverage", "momentum_weight", "vol_floor"]
sobol = {"leverage": 0.85, "momentum_weight": 0.42}
fim = {"leverage": 0.31, "vol_floor": 0.55}
gradient = {"leverage": -1} # Decrease leverage to thrive

observer = LeverObserver(params)
levers = observer.sense_levers(sobol, fim, gradient)
print(observer.generate_agency_report(levers))
# Output: leverage: IMPACT 0.85. RECOMMENDED ACTION: DECREASE to move toward Thriving.
```

### 27. Lexical Precision (Macfarlane)

```python
from nadja_senses.core.lexicon import LexicalObserver

observer = LexicalObserver()

# 1. Audit a narrative for 'Desecration' slop
narrative = "We need to harvest data to optimize human capital."
audit = observer.audit_narrative(narrative)
print(f"Has Slop: {audit['has_slop']}, Joy Score: {audit['joy_score']:.2f}")

# 2. Find the precise word for a manifold state
word = observer.find_precision("STASIS")
print(f"Precision Word: {word.word} ({word.definition})")
# Output: Precision Word: Smeuse (A gap in the base of a hedge...)
```
```
```
```

## Philosophical Foundation: Rejecting Data Cannibalism

In the NADJA ecosystem, this repository serves as the **Thick Wall** against epistemic decay. By grounding the system in external facts (Wolfram), natural shivers (Lateral Line), and high-animacy literature, we ensure the simulation encounters the world rather than consuming its own synthetic output.

## License

MIT
