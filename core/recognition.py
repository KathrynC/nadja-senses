"""Pattern 19: The Sense of Recognition (Archetypal Matching)

The highest-level cognitive sense. Classifies the integrated sensorium 
(Smell, Sight, Sound, Taste, Touch) into recognized historical, 
literary, and financial archetypes.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any

@dataclass
class RecognitionLandmark:
    """A recognized archetypal situation."""
    name: str
    confidence: float
    description: str
    action_suggestion: str
    resonance_smell: str 
    precision_word: Optional[str] = None # Pattern 38

from nadja_senses.gallery.archetypes import ARCHETYPES, StorylineArchetype
from nadja_senses.core.lexicon import LexicalObserver

class RecognitionObserver:
    """The 'Semantic Eye' of the sensorium. Recognizes patterns of power/decay."""
    
    def __init__(self):
        self.archetypes = ARCHETYPES
        self.lexicon = LexicalObserver()

    def recognize(self, current_sensorium: Dict[str, Any]) -> List[RecognitionLandmark]:
        """Match the current multi-modal sensorium against high-order archetypes."""
        matches = []
        
        for arch in self.archetypes:
            score = 0.0
            hits = 0
            for key, expected_val in arch.recognition_key.items():
                if current_sensorium.get(key) == expected_val:
                    hits += 1
            
            if hits >= 2: 
                score = hits / len(arch.recognition_key)
                
                # Link to Lexical Precision
                word_anchor = self.lexicon.find_precision(arch.lakoff_frame)
                p_word = word_anchor.word if word_anchor else None
                
                matches.append(RecognitionLandmark(
                    name=arch.name,
                    confidence=score,
                    description=arch.description,
                    action_suggestion=f"Navigate per {arch.lakoff_frame} frame.",
                    resonance_smell=arch.recognition_key.get("smell", "neutral"),
                    precision_word=p_word
                ))
            
        return matches

    def generate_recognition_report(self, matches: List[RecognitionLandmark]) -> str:
        """Produce a high-level semantic audit with lexical precision."""
        if not matches:
            return "THE WORLD IS NOVEL. NO KNOWN ARCHETYPES RECOGNIZED."
            
        lines = ["SEMANTIC RECOGNITION REPORT"]
        for m in matches:
            lines.append(f"  ★ Landmark: {m.name} (Confidence: {m.confidence:.2f})")
            if m.precision_word:
                lines.append(f"    PRECISION WORD: {m.precision_word.upper()}")
            lines.append(f"    {m.description}")
            lines.append(f"    STRATEGY: {m.action_suggestion}")
        
        return "\n".join(lines)
