# NADJA Senses

A specialized framework for **Semantic Pressure Sensing**, structured as a series of **Edge Environments** following Christopher Alexander's *Pattern Language*.

This toolkit treats sensory integration as a "living" organism, metabolizing raw world entropy into the structural beauty of the Memory Palace.

## Core Patterns

1.  **The Common Language:** A 10D Olfactory Algebra (Castro NMF) that normalizes all sensations (text, weather, price).
2.  **The Lateral Line:** Pressure gradient sensing that detects minute vibrations and "shivers" in the distal data stream (Arxiv, News, Climate).
3.  **Light on Two Sides:** A divergence-detection system that requires multi-domain confirmation for any major signal.
4.  **The Inscription Wall:** A synthesis layer that translates sensory gestalts into narrative strategies via Thinker Lenses.
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

### 5. Recognize Gait

```python
from nadja_senses.interior.gait import GaitObserver

# Trajectory data for a specific ticker
trajectory = [
    {"volatility": 0.1, "momentum": 0.08},
    {"volatility": 0.15, "momentum": 0.12}
]

observer = GaitObserver()
signature = observer.recognize_gait("NVDA", trajectory)
print(observer.generate_hunting_report([signature]))
# Output: NVDA: MOMENTUM. Gait: High-displacement (The Wolf).

### 6. Measure Semantic Distance

```python
import numpy as np
from nadja_senses.interior.distance import DistanceObserver

# Current market state distribution
current_dist = np.random.randn(100, 4)
target_dist = np.random.randn(100, 4) + 0.2

observer = DistanceObserver(current_dist)
perception = observer.measure_distance("2008_CRISIS", target_dist)
print(observer.generate_depth_report([perception]))
# Output: 2008_CRISIS: APPROACHING (Proximity: 0.67).

### 7. Map a Specimen via Echolocation

```python
from nadja_senses.edge.echolocation import EcholocationObserver

# A semantic 'echo' from a model pelt
pelt_id = "seed_tomato_zapotec"
prompt = "What is the financial metaphor for a Zapotec Pink Pleated Tomato?"
response = "It represents structural complexity and heirloom resilience..."

observer = EcholocationObserver("deepseek-v3.1")
echo = observer.interpret_echo(pelt_id, prompt, response)
print(observer.map_environment([echo]))
# Output: Specimen deepseek-v3.1 exhibits a high-resolution financial ontology...

### 8. Trigger a Limbic Override

```python
from nadja_senses.core.reflex import LimbicReflex

# A dangerous 'smell' detected in the manifold
smell = {"sulfurous": 0.85, "citrus": 0.1}

reflex_center = LimbicReflex()
action = reflex_center.evaluate(smell)

if action:
    print(reflex_center.generate_visceral_report(action))
    # Output: !!! LIMBIC OVERRIDE !!! THE AIR IS SULFUROUS...

### 9. Taste the Portfolio (Interoception)

```python
from nadja_senses.interior.gustatory import GustatoryObserver

# Portfolio of owned positions
positions = [
    {"ticker": "NVDA", "unrealized_pnl_pct": 0.12, "thesis_alignment": 0.9, "weight_pct": 0.10}, # SWEET
    {"ticker": "KRE", "unrealized_pnl_pct": -0.08, "thesis_alignment": 0.2, "weight_pct": 0.05}  # BITTER
]

observer = GustatoryObserver()
tastes = observer.taste_portfolio(positions)
print(observer.generate_tasting_menu(tastes))
# Output: KRE: BITTER. FEEDBACK: Triggers PUTRID olfactory signal.
```

### 10. Feel the Market Surface (Somatosensation)

```python
from nadja_senses.interior.haptic import HapticObserver

data = {"volatility": 0.9, "pnl_pct": -0.05, "liquidity": 0.3}
observer = HapticObserver()
profile = observer.feel_state("SPY", data)
print(profile.description)
# Output: Nociceptive alert: The system is in pain.
```

### 11. Sense Body Posture (Proprioception)

```python
from nadja_senses.interior.proprioception import ProprioceptionObserver

params = {"leverage_target": 2.5, "rebalance_threshold": 0.02}
observer = ProprioceptionObserver()
signature = observer.sense_posture(params)
print(f"Current Gait: {signature.recognized_gait}")
# Output: Current Gait: sprint
```

### 12. Sense Manifold Balance (Vestibular)

```python
from nadja_senses.interior.vestibular import VestibularObserver

# State history (momentum and regime)
history = [{"momentum": 0.1}, {"momentum": 0.3}, {"momentum": 0.6, "regime": 2.0}]
observer = VestibularObserver()
state = observer.sense_balance(history)
print(state.description)
# Output: Sudden upward tilt. System accelerating toward new attractor.

### 14. Cross-Modal Transduction (Synesthesia)

```python
from nadja_senses.core.synesthesia import SynesthesiaTransducer

# Transduce a rhythmic 'hearing' state into other senses
gestalt = SynesthesiaTransducer.transduce_gestalt("DACTYLIC")
print(gestalt["description"])
# Output: The system hears DACTYLIC, smells sulfurous, and sees #f44336.

### 15. Semantic Recognition

```python
from nadja_senses.core.recognition import RecognitionObserver

# Integrated sensorium gestalt
sensorium = {
    "smell": "sulfurous",
    "hearing": "DACTYLIC",
    "touch_pressure": 0.82
}

observer = RecognitionObserver()
matches = observer.recognize(sensorium)
print(observer.generate_recognition_report(matches))
# Output: Landmark: ARTURO_UI_RISE. Recognized: The resistible rise of a disruptor agent.

### 17. Integrate the Unified Self (The Spotlight)

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

### 18. Unified Sense of Place (Topoception)

```python
import numpy as np
from nadja_senses.core.location import LocationObserver

# Current state across systems
geo_coords = (40.7128, -74.0060) # New York
ode_state = np.array([1.0, 2.5, 0.5, 0.8, 0.02, 0.04, 2.0]) # PV, LEV, ..., REGIME=2
palace_room = "predator_trump"

observer = LocationObserver(palace_map={"predator_trump": "Predator Den"})
coords = observer.sense_location(geo=geo_coords, ode_state=ode_state, palace_room=palace_room)
print(observer.generate_location_report(coords))
# Output: ODE: In Regime 2. PALACE: Inside predator_trump (Predator Den).

### 19. Scenario Location & Storyline Trajectory

```python
from nadja_senses.core.location import LocationObserver

observer = LocationObserver()

# 1. Sense "What Planet are we on?"
coords = observer.sense_location(scenario_id="global_financial_crisis")

# 2. Infer "Where do we go from here?" via TSCA Rules
fired_rules = ["LIQUIDITY_SPIRAL", "MARGIN_CALL_CASCADE"]
vector = observer.infer_trajectory(coords, fired_rules)

print(observer.generate_location_report(coords, vector))
# Output: SCENARIO: On Planet MARS. STORYLINE: Phase BEGINNING, Next Step LIQUIDITY_SPIRAL.

### 20. Sense Safety & Belonging

```python
from nadja_senses.interior.safety import SafetyObserver

# High threat, memory stashed in hermit crab shell, low social contagion
observer = SafetyObserver()
state = observer.sense_safety(threat_level=0.8, memory_stashed=True, contagion_rate=0.2)
print(state.description)
# Output: ADVERSARIAL ALERT: System feels actively targeted.
```

### 21. Sense Metabolic Appetite (Hunger/Thirst)

```python
from nadja_senses.interior.metabolic import MetabolicObserver

# High cliché saturation, low nectar count
observer = MetabolicObserver()
state = observer.sense_appetite(saturation_score=0.9, nectar_count=1)
print(state.description)
# Output: BOREDOM: Over-inscribed with clichés. Hunger for RUPTURE.
```

### 22. Feel Typographic Tension (Sight)

```python
from nadja_senses.gallery.typography import TypographyObserver

# High volatility and high pressure
observer = TypographyObserver()
muscle = observer.sense_type_tension(volatility=0.8, pressure=0.9)
print(f"Weight: {muscle.font_weight}, Skew: {muscle.skew_degrees}")
print(muscle.label)
# Output: TYPOGRAPHIC BRUISE: MANIFOLD UNDER HEAVY TENSION
```
```
```
```

### 16. Sense the Lateral Line (Exteroception)

```python
from nadja_senses.edge.lateral_line import LateralLineObserver

# External data flux (velocity and salience)
flux = {
    "news_arrival_rate": 3.2,
    "climate_anomaly": 1.8
}

observer = LateralLineObserver()
shivers = observer.sense_shivers(flux)
print(observer.generate_shiver_report(shivers))
# Output: ENVIRONMENTAL: VIBRATION 0.95 | GRADIENT 0.15. Planetary shiver detected.
```
```
```

### 13. Sense Semantic Time (Chronos)

```python
from nadja_senses.interior.chronos import ChronosObserver

# State history and age of current market thesis (in days)
history = [{"volatility": 0.1}, {"volatility": 0.4}, {"volatility": 0.9}]
thesis_age = 45 

observer = ChronosObserver()
texture = observer.sense_time(history, thesis_age)
print(f"Dominant Time: {texture.dominant_channel.upper()}")
print(texture.description)
# Output: Dominant Time: EROSION. Time is heavy. The current thesis is eroding.
```
```

## Philosophical Foundation: Rejecting Data Cannibalism

In the NADJA ecosystem, this repository serves as the **Thick Wall** against epistemic decay. By grounding the system in external facts (Wolfram), natural shivers (Lateral Line), and high-animacy literature, we ensure the simulation encounters the world rather than consuming its own synthetic output.

## License

MIT
