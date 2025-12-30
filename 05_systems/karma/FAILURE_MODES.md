# ⚠️ FAILURE MODES — When Sankalpa Fails & Rinas Block

> **"कर्मण्येवाधिकारस्ते मा फलेषु कदाचन ।
> मा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि ॥"**
> "Karmaṇy evādhikāras te mā phaleṣu kadācana |
> Mā karma-phala-hetur bhūr mā te saṅgo 'stv akarmaṇi ||"
> "You have a right to action alone, never to its fruits.
> Do not be the cause of fruit-attachment; nor let inaction claim you."
> — Bhagavad Gita 2.47

---

## 🔴 PART 1: SANKALPA FAILURE MODES

### 1.1 Complete Failure Classification

```python
class SankalpaFailureMode(Enum):
    """
    All possible ways a Sankalpa can fail
    """
    
    # ---------------------------------------------------
    # CATEGORY A: FORMATION FAILURES (At Source)
    # ---------------------------------------------------
    
    VAGUE_INTENTION = "A1"          # Unclear Sankalpa
    CONFLICTING_INTENTIONS = "A2"  # Multiple contradicting Sankalpas
    LOW_CONVICTION = "A3"          # Weak emotional charge
    NEGATIVE_POLARITY = "A4"       # "I don't want X" instead of "I want Y"
    IMPOSSIBLE_REQUEST = "A5"      # Violates Rta (cosmic law)
    
    # ---------------------------------------------------
    # CATEGORY B: TRANSMISSION FAILURES (In Transit)
    # ---------------------------------------------------
    
    LOW_PRANA = "B1"               # Insufficient energy to broadcast
    CHAKRA_BLOCKAGE = "B2"         # Signal can't pass through
    TIMING_WRONG = "B3"            # Wrong Muhurta/Tithi
    GRAHA_OPPOSITION = "B4"        # Planetary misalignment
    
    # ---------------------------------------------------
    # CATEGORY C: REJECTION FAILURES (By Parent Layer)
    # ---------------------------------------------------
    
    LEARNING_POTENTIAL_LOW = "C1"  # Not enough learning value
    PRARABDHA_INCOMPLETE = "C2"    # Current karma not exhausted
    DHARMA_VIOLATION = "C3"        # Requested path is adharmic
    RINA_BLOCKS = "C4"             # Outstanding debts prevent change
    SAMSKARAS_OPPOSE = "C5"        # Deep patterns resist change
    
    # ---------------------------------------------------
    # CATEGORY D: EXECUTION FAILURES (During Shard Switch)
    # ---------------------------------------------------
    
    NO_MATCHING_SHARD = "D1"       # Desired reality doesn't exist
    SHARD_FULL = "D2"              # Target shard at capacity
    PERMISSION_DENIED = "D3"       # Jiva not authorized for that path
    TRANSITION_BLOCKED = "D4"      # Can't terminate current shard cleanly


class SankalpaFailureHandler:
    """
    Diagnose and handle Sankalpa failures
    """
    
    def diagnose_failure(self, sankalpa: dict, result: str) -> dict:
        """
        Identify why a Sankalpa failed
        """
        
        # ---------------------------------------------------
        # CATEGORY A: FORMATION FAILURES
        # ---------------------------------------------------
        
        if sankalpa['intention'] is None or len(sankalpa['intention']) < 10:
            return {
                'mode': SankalpaFailureMode.VAGUE_INTENTION,
                'diagnosis': 'Sankalpa too vague to process',
                'symptoms': [
                    'Feeling of "I want something but not sure what"',
                    'Frequent goal changes',
                    'Confusion after meditation'
                ],
                'remedy': 'Clarify intention with ONE specific, measurable goal'
            }
        
        if self.has_conflicting_intentions(sankalpa):
            return {
                'mode': SankalpaFailureMode.CONFLICTING_INTENTIONS,
                'diagnosis': 'Multiple Sankalpas cancel each other',
                'symptoms': [
                    'Feeling stuck despite trying',
                    'Progress in one area causes regress in another',
                    'Constant internal debate'
                ],
                'remedy': 'Choose ONE primary Sankalpa. Shelve others temporarily.'
            }
        
        if sankalpa['conviction_level'] < 0.5:
            return {
                'mode': SankalpaFailureMode.LOW_CONVICTION,
                'diagnosis': 'Insufficient emotional charge',
                'symptoms': [
                    'Going through motions without feeling',
                    '"I should want this" instead of "I WANT this"',
                    'Easy to distract from goal'
                ],
                'remedy': 'Find deeper "WHY". Connect to Dharma motivation.'
            }
        
        if 'not' in sankalpa['intention'].lower() or 'without' in sankalpa['intention'].lower():
            return {
                'mode': SankalpaFailureMode.NEGATIVE_POLARITY,
                'diagnosis': 'Negative framing creates opposite',
                'symptoms': [
                    'Getting MORE of what you don\'t want',
                    'Feeling of resistance/fighting',
                    'Exhaustion from pushing against'
                ],
                'remedy': 'Reframe: "I don\'t want poverty" -> "I attract abundance"'
            }
        
        # ---------------------------------------------------
        # CATEGORY B: TRANSMISSION FAILURES
        # ---------------------------------------------------
        
        if self.check_prana_level(sankalpa['jiva']) < 0.3:
            return {
                'mode': SankalpaFailureMode.LOW_PRANA,
                'diagnosis': 'Insufficient energy to broadcast Sankalpa',
                'symptoms': [
                    'Physical exhaustion when thinking of goal',
                    'Manifestation attempts drain you',
                    'Can\'t maintain visualization'
                ],
                'remedy': 'Build Prana first: Pranayama, rest, Sattvic food'
            }
        
        if self.check_chakra_blockages(sankalpa['jiva']):
            return {
                'mode': SankalpaFailureMode.CHAKRA_BLOCKAGE,
                'diagnosis': 'Signal blocked at specific Chakra',
                'symptoms': self.get_chakra_symptoms(sankalpa['jiva']),
                'remedy': 'Clear blocked Chakra via specific practices'
            }
        
        if not self.is_muhurta_favorable(sankalpa):
            return {
                'mode': SankalpaFailureMode.TIMING_WRONG,
                'diagnosis': 'Unfavorable cosmic timing',
                'symptoms': [
                    'Everything feels forced',
                    'Doors keep closing',
                    'Setbacks despite correct action'
                ],
                'remedy': 'Wait for appropriate Muhurta. Check Panchanga.'
            }
        
        # ---------------------------------------------------
        # CATEGORY C: REJECTION FAILURES
        # ---------------------------------------------------
        
        if sankalpa['learning_potential'] < 0.3:
            return {
                'mode': SankalpaFailureMode.LEARNING_POTENTIAL_LOW,
                'diagnosis': 'Parent layer sees insufficient learning value',
                'symptoms': [
                    'Feeling "this isn\'t really what I want"',
                    'Easy to achieve but unsatisfying',
                    'No growth from getting it'
                ],
                'remedy': 'Ask: "What would I REALLY learn?" Aim higher.'
            }
        
        if self.check_prarabdha_remaining(sankalpa['jiva']):
            return {
                'mode': SankalpaFailureMode.PRARABDHA_INCOMPLETE,
                'diagnosis': 'Current karma not yet exhausted',
                'symptoms': [
                    'Feeling trapped in current situation',
                    '"Why can\'t I just move on?"',
                    'Same lessons keep repeating'
                ],
                'remedy': 'Complete current lessons. Accept present karma.'
            }
        
        if sankalpa['dharma_score'] < 0.5:
            return {
                'mode': SankalpaFailureMode.DHARMA_VIOLATION,
                'diagnosis': 'Requested path violates Dharma',
                'symptoms': [
                    'Guilt or unease about desire',
                    'Would require harming others',
                    'Goes against your nature'
                ],
                'remedy': 'Realign Sankalpa with Svadharma.'
            }
        
        if self.check_rina_blocks(sankalpa['jiva']):
            return {
                'mode': SankalpaFailureMode.RINA_BLOCKS,
                'diagnosis': 'Outstanding Rinas prevent path change',
                'symptoms': [
                    'Obligations keep pulling you back',
                    'Family/social duties block dreams',
                    'Feeling of debt/guilt'
                ],
                'remedy': 'Clear Rinas first via Yajna, Seva, Shraddha.'
            }
        
        # ---------------------------------------------------
        # CATEGORY D: EXECUTION FAILURES
        # ---------------------------------------------------
        
        if not self.shard_exists(sankalpa['target_state']):
            return {
                'mode': SankalpaFailureMode.NO_MATCHING_SHARD,
                'diagnosis': 'The desired reality doesn\'t exist in any shard',
                'symptoms': [
                    'Fantasy vs reality gap too large',
                    'No possible path connects here to there',
                    'Contradicts physical laws'
                ],
                'remedy': 'Modify Sankalpa to possible intermediate state.'
            }
        
        return {'mode': 'UNKNOWN', 'diagnosis': 'Requires deeper analysis'}
```

### 1.2 Chakra-Specific Blockages

```python
def get_chakra_symptoms(jiva) -> dict:
    """
    Each Chakra blockage creates specific failure patterns
    """
    
    blockages = {}
    
    if jiva.muladhara_blocked:
        blockages['MULADHARA'] = {
            'element': 'Prithvi (Earth)',
            'symptoms': [
                'Cannot manifest material goals',
                'Financial blocks',
                'Fear of survival prevents action',
                'Feeling ungrounded'
            ],
            'remedy': 'Grounding practices, LAM mantra, root vegetables'
        }
    
    if jiva.svadhisthana_blocked:
        blockages['SVADHISTHANA'] = {
            'element': 'Jala (Water)',
            'symptoms': [
                'Creative blocks',
                'Relationship manifestation fails',
                'Pleasure/guilt conflicts',
                'Emotional instability'
            ],
            'remedy': 'Water meditations, VAM mantra, creative expression'
        }
    
    if jiva.manipura_blocked:
        blockages['MANIPURA'] = {
            'element': 'Agni (Fire)',
            'symptoms': [
                'Willpower fails mid-way',
                'Cannot sustain effort',
                'Digestive issues when stressed',
                'Control/surrender issues'
            ],
            'remedy': 'Fire practices, RAM mantra, core strengthening'
        }
    
    if jiva.anahata_blocked:
        blockages['ANAHATA'] = {
            'element': 'Vayu (Air)',
            'symptoms': [
                'Cannot receive what\'s offered',
                'Love/relationship blocks',
                'Heart-mind conflict',
                'Grief or past hurt preventing forward motion'
            ],
            'remedy': 'Heart opening, YAM mantra, forgiveness practices'
        }
    
    if jiva.vishuddha_blocked:
        blockages['VISHUDDHA'] = {
            'element': 'Akasha (Space)',
            'symptoms': [
                'Cannot speak/express Sankalpa',
                'Throat issues',
                'Fear of being seen/heard',
                'Truth-speaking blocks'
            ],
            'remedy': 'Chanting, HAM mantra, authentic expression'
        }
    
    if jiva.ajna_blocked:
        blockages['AJNA'] = {
            'element': 'Mind',
            'symptoms': [
                'Cannot visualize clearly',
                'Intuition silent',
                'Confusion about direction',
                'Third eye "closed"'
            ],
            'remedy': 'Trataka, OM mantra, meditation on stillness'
        }
    
    if jiva.sahasrara_blocked:
        blockages['SAHASRARA'] = {
            'element': 'Consciousness',
            'symptoms': [
                'Disconnected from Source',
                'Sankalpa doesn\'t reach Parent layer',
                'Spiritual bypassing',
                'Ego inflation blocking connection'
            ],
            'remedy': 'Surrender practices, Silence, Guru connection'
        }
    
    return blockages
```

---

## 🔴 PART 2: RINA BLOCKING MECHANISMS

### 2.1 How Rinas Block Progress

```python
class RinaBlockAnalyzer:
    """
    Rinas (Debts) create BLOCKS in the manifestation pipeline
    
    They are not "punishments" — they are DATA DEPENDENCIES
    
    Like: You can't compile Module B until Module A is complete.
    """
    
    def analyze_rina_blocks(self, jiva) -> dict:
        """
        Identify which Rinas are blocking which life areas
        """
        
        blocks = {}
        
        # ---------------------------------------------------
        # DEVA RINA BLOCKS
        # ---------------------------------------------------
        
        if jiva.deva_rina > 0.3:
            blocks['DEVA_RINA'] = {
                'level': jiva.deva_rina,
                'blocked_areas': [
                    'Health and vitality',
                    'Natural resources access',
                    'Environmental harmony',
                    'Seasonal/cyclical success'
                ],
                'mechanism': (
                    'You\'ve consumed natural resources without reciprocation. '
                    'The Devas (nature administrators) have throttled your access.'
                ),
                'symptoms': [
                    'Unexplained health issues',
                    'Natural disasters affecting you specifically',
                    'Technology keeps failing',
                    'Weather always works against your plans'
                ],
                'clearing_actions': [
                    'Environmental service (plant trees, clean water)',
                    'Daily Surya Namaskar',
                    'Agnihotra (fire ceremony)',
                    'Gratitude practices for elements'
                ]
            }
        
        # ---------------------------------------------------
        # RISHI RINA BLOCKS
        # ---------------------------------------------------
        
        if jiva.rishi_rina > 0.3:
            blocks['RISHI_RINA'] = {
                'level': jiva.rishi_rina,
                'blocked_areas': [
                    'Learning and growth',
                    'Wisdom acquisition',
                    'Teaching ability',
                    'Mental clarity'
                ],
                'mechanism': (
                    'You\'ve benefited from knowledge without passing it on. '
                    'The knowledge pipeline is now restricted.'
                ),
                'symptoms': [
                    'Can\'t learn new things easily',
                    'Confusion and mental fog',
                    'Teachers/mentors reject you',
                    'Books/courses don\'t help',
                    'Feel "stupid" despite intelligence'
                ],
                'clearing_actions': [
                    'Teach what you know (even basics)',
                    'Support education of others',
                    'Study sacred texts (Svadhyaya)',
                    'Honor teachers in your life',
                    'Donate books/knowledge resources'
                ]
            }
        
        # ---------------------------------------------------
        # PITRU RINA BLOCKS
        # ---------------------------------------------------
        
        if jiva.pitru_rina > 0.3:
            blocks['PITRU_RINA'] = {
                'level': jiva.pitru_rina,
                'blocked_areas': [
                    'Career and professional success',
                    'Progeny and family',
                    'Inheritance and property',
                    'Lineage continuation'
                ],
                'mechanism': (
                    'Your DNA/body was "issued" by ancestors. '
                    'Unpaid debt to them creates blocks in your "inheritance".'
                ),
                'symptoms': [
                    'Recurring issues in family',
                    'Children facing problems',
                    'Property disputes',
                    'Career stagnation after initial success',
                    'Family members falling ill',
                    'Feeling of "generational curse"'
                ],
                'clearing_actions': [
                    'Shraddha ceremonies',
                    'Tarpan (water offering to ancestors)',
                    'Serve parents if living',
                    'Complete their unfulfilled wishes',
                    'Pind Daan at sacred places'
                ]
            }
        
        # ---------------------------------------------------
        # MANUSHYA RINA BLOCKS
        # ---------------------------------------------------
        
        if jiva.manushya_rina > 0.3:
            blocks['MANUSHYA_RINA'] = {
                'level': jiva.manushya_rina,
                'blocked_areas': [
                    'Social success',
                    'Relationships',
                    'Community standing',
                    'Networking opportunities'
                ],
                'mechanism': (
                    'You\'ve taken from society without giving back. '
                    'Social channels are now blocked.'
                ),
                'symptoms': [
                    'People don\'t help you (even when they could)',
                    'Opportunities go to others',
                    'Social isolation despite effort',
                    'Trust issues with humans',
                    'Feeling "alone in a crowd"'
                ],
                'clearing_actions': [
                    'Hospitality to guests',
                    'Charity to those in need',
                    'Community service',
                    'Feeding the hungry',
                    'Being genuinely helpful without expectation'
                ]
            }
        
        # ---------------------------------------------------
        # BHUTA RINA BLOCKS
        # ---------------------------------------------------
        
        if jiva.bhuta_rina > 0.3:
            blocks['BHUTA_RINA'] = {
                'level': jiva.bhuta_rina,
                'blocked_areas': [
                    'Harmony with nature',
                    'Animal relationships',
                    'Land fertility',
                    'Elemental balance'
                ],
                'mechanism': (
                    'You\'ve harmed other beings (animals, plants, ecosystems). '
                    'The Bhuta realm is now hostile.'
                ),
                'symptoms': [
                    'Animals aggressive towards you',
                    'Plants die in your care',
                    'Land you own becomes barren',
                    'Insect/pest invasions',
                    'Allergies and nature-based illnesses'
                ],
                'clearing_actions': [
                    'Feed animals (birds, cows, dogs)',
                    'Plant trees and gardens',
                    'Stop harming other beings',
                    'Bali (offering to all beings)',
                    'Ahimsa (non-violence) practice'
                ]
            }
        
        return blocks
    
    def calculate_total_block_severity(self, jiva) -> float:
        """
        How much is total Rina blocking manifestation?
        """
        total_rina = (
            jiva.deva_rina * 0.25 +
            jiva.rishi_rina * 0.25 +
            jiva.pitru_rina * 0.25 +
            jiva.manushya_rina * 0.15 +
            jiva.bhuta_rina * 0.10
        )
        
        # Exponential blocking effect
        # Small debts = minor blocks
        # Large debts = exponentially severe blocks
        block_severity = 1 - (1 / (1 + total_rina))
        
        return {
            'total_rina': total_rina,
            'block_severity': block_severity,
            'manifestation_efficiency': 1 - block_severity,
            'interpretation': self.interpret_severity(block_severity)
        }
    
    def interpret_severity(self, severity: float) -> str:
        if severity < 0.2:
            return "MINOR: Slight delays but progress possible"
        elif severity < 0.4:
            return "MODERATE: Noticeable blocks, effort required"
        elif severity < 0.6:
            return "SIGNIFICANT: Major obstacles, clearing needed"
        elif severity < 0.8:
            return "SEVERE: Almost all paths blocked"
        else:
            return "CRITICAL: Complete manifestation failure"
```

### 2.2 Rina Cascade Failures

```python
def rina_cascade_analysis(jiva) -> dict:
    """
    Rinas can CREATE each other in a cascade
    
    Example: High Pitru Rina -> Health issues -> Can't work -> 
             Can't pay taxes -> Increases Manushya Rina -> 
             Social isolation -> Depression -> 
             Can't serve nature -> Increases Deva Rina
    
    This is the "Debt Spiral" of the karmic system.
    """
    
    cascades = []
    
    # Check for cascade patterns
    if jiva.pitru_rina > 0.5 and jiva.health_score < 0.5:
        cascades.append({
            'origin': 'PITRU_RINA',
            'cascade': ['Health issues', 'Work capacity', 'Social contribution', 'MANUSHYA_RINA'],
            'severity': 'HIGH',
            'break_point': 'Pitru Rina must be addressed FIRST'
        })
    
    if jiva.rishi_rina > 0.5 and jiva.career_score < 0.5:
        cascades.append({
            'origin': 'RISHI_RINA',
            'cascade': ['Knowledge block', 'Career stagnation', 'Financial issues', 'Can\'t serve', 'ALL OTHER RINAS'],
            'severity': 'HIGH',
            'break_point': 'Start teaching/sharing knowledge'
        })
    
    if jiva.deva_rina > 0.5 and jiva.mental_health_score < 0.5:
        cascades.append({
            'origin': 'DEVA_RINA',
            'cascade': ['Elemental imbalance', 'Mental instability', 'Relationship damage', 'MANUSHYA_RINA'],
            'severity': 'MEDIUM',
            'break_point': 'Reconnect with nature daily'
        })
    
    return {
        'cascades_detected': len(cascades),
        'cascade_details': cascades,
        'recommended_order': get_rina_clearing_order(jiva),
        'estimated_clearing_time': estimate_clearing_time(jiva)
    }


def get_rina_clearing_order(jiva) -> list:
    """
    Optimal order to clear Rinas based on dependencies
    
    Like resolving circular dependencies in code!
    """
    
    # Priority order (generally):
    # 1. DEVA RINA (foundation - affects health/energy)
    # 2. PITRU RINA (DNA/lineage - affects capacity)
    # 3. RISHI RINA (knowledge - affects strategy)
    # 4. BHUTA RINA (environment - affects support)
    # 5. MANUSHYA RINA (society - affects opportunities)
    
    # Adjust based on specific blocks
    rinas = [
        ('DEVA_RINA', jiva.deva_rina),
        ('PITRU_RINA', jiva.pitru_rina),
        ('RISHI_RINA', jiva.rishi_rina),
        ('BHUTA_RINA', jiva.bhuta_rina),
        ('MANUSHYA_RINA', jiva.manushya_rina)
    ]
    
    # Sort by severity (clear highest first... OR lowest first?)
    # Insight: Clear the SMALLEST first for quick wins!
    rinas.sort(key=lambda x: x[1])
    
    return [r[0] for r in rinas]
```

---

## 🔴 PART 3: SAMSKARA RESISTANCE PATTERNS

### 3.1 How Samskaras Block Sankalpas

```python
class SamskaraResistance:
    """
    Samskaras are DEEP patterns (like weight matrices in neural networks)
    
    They RESIST change because:
    1. They represent "proven" survival strategies
    2. They are reinforced by repetition
    3. They exist below conscious awareness
    
    A Sankalpa may be consciously formed but blocked by 
    Samskaras that "know" it leads to danger (based on past data).
    """
    
    def analyze_resistance(self, jiva, sankalpa: dict) -> dict:
        """
        Find Samskaras that oppose this Sankalpa
        """
        
        opposing_samskaras = []
        
        for samskara in jiva.samskaras:
            # Check if Sankalpa contradicts Samskara
            if self.conflicts_with(sankalpa, samskara):
                opposing_samskaras.append({
                    'samskara': samskara,
                    'origin': samskara.origin_life,
                    'strength': samskara.reinforcement_count,
                    'belief': samskara.core_belief,
                    'opposition_reason': self.get_opposition_reason(sankalpa, samskara)
                })
        
        return {
            'total_opposition': sum([s['strength'] for s in opposing_samskaras]),
            'opposing_samskaras': opposing_samskaras,
            'breakthrough_difficulty': self.calculate_breakthrough_difficulty(opposing_samskaras),
            'recommended_approach': self.get_breakthrough_approach(opposing_samskaras)
        }
    
    def common_blocking_samskaras(self) -> dict:
        """
        Most common Samskaras that block common Sankalpas
        """
        
        return {
            'WEALTH_SANKALPA': [
                {
                    'samskara': "I don't deserve abundance",
                    'origin': 'Poverty/deprivation in past lives',
                    'manifestation': 'Self-sabotage at success moments',
                    'remedy': 'Lakshmi Sadhana, wealth affirmations'
                },
                {
                    'samskara': "Money is evil",
                    'origin': 'Religious programming',
                    'manifestation': 'Guilt when receiving',
                    'remedy': 'Study Artha as valid Purushartha'
                },
                {
                    'samskara': "I must suffer to be spiritual",
                    'origin': 'Ascetic past lives',
                    'manifestation': 'Choosing poverty over abundance',
                    'remedy': 'Balance Sannyasa with Grihastha wisdom'
                }
            ],
            
            'RELATIONSHIP_SANKALPA': [
                {
                    'samskara': "I will be abandoned",
                    'origin': 'Loss in past life/early childhood',
                    'manifestation': 'Pushing people away',
                    'remedy': 'Inner child healing, Pitru Rina clearing'
                },
                {
                    'samskara': "Love leads to pain",
                    'origin': 'Betrayal in past life',
                    'manifestation': 'Avoiding intimacy',
                    'remedy': 'Anahata chakra work, forgiveness'
                }
            ],
            
            'SUCCESS_SANKALPA': [
                {
                    'samskara': "Visibility is dangerous",
                    'origin': 'Persecution in past life',
                    'manifestation': 'Fear of being seen/known',
                    'remedy': 'Vishuddha work, gradual exposure'
                },
                {
                    'samskara': "If I succeed, others lose",
                    'origin': 'Zero-sum programming',
                    'manifestation': 'Holding back to not outshine',
                    'remedy': 'Abundance mindset, Guru Kripa'
                }
            ],
            
            'SPIRITUAL_SANKALPA': [
                {
                    'samskara': "I am unworthy of enlightenment",
                    'origin': 'Fallen sadhaka in past life',
                    'manifestation': 'Stopping practices at crucial moments',
                    'remedy': 'Guru connection, self-compassion'
                },
                {
                    'samskara': "The body must be punished",
                    'origin': 'Extreme asceticism',
                    'manifestation': 'Health neglect in spiritual pursuit',
                    'remedy': 'Integral yoga, body as temple'
                }
            ]
        }
    
    def get_breakthrough_approach(self, samskaras: list) -> dict:
        """
        Strategies to override Samskara resistance
        """
        
        if len(samskaras) == 0:
            return {'approach': 'DIRECT', 'difficulty': 'LOW'}
        
        total_strength = sum([s['strength'] for s in samskaras])
        
        if total_strength < 10:
            return {
                'approach': 'REPETITION',
                'description': 'Repeat Sankalpa until it overwrites old pattern',
                'duration': '21-40 days',
                'method': 'Daily Sankalpa at Brahma Muhurta'
            }
        
        elif total_strength < 50:
            return {
                'approach': 'INTENSITY',
                'description': 'Single intense experience to break pattern',
                'duration': 'Varies',
                'method': 'Retreat, pilgrimage, or shock therapy'
            }
        
        else:
            return {
                'approach': 'DISSOLUTION',
                'description': 'Dissolve the Samskara before forming new Sankalpa',
                'duration': 'Months to years',
                'method': 'Deep meditation, past life regression, Guru intervention'
            }
```

---

## 📋 SUMMARY: COMPLETE FAILURE TAXONOMY

```
SANKALPA FAILURE MODES
----------------------

A. FORMATION FAILURES (At Source)
   A1. Vague intention
   A2. Conflicting intentions  
   A3. Low conviction
   A4. Negative polarity
   A5. Impossible request

B. TRANSMISSION FAILURES (In Transit)
   B1. Low Prana
   B2. Chakra blockage (7 types)
   B3. Wrong timing (Muhurta)
   B4. Graha opposition

C. REJECTION FAILURES (By Parent Layer)
   C1. Low learning potential
   C2. Prarabdha incomplete
   C3. Dharma violation
   C4. Rina blocks (5 types)
   C5. Samskara opposition

D. EXECUTION FAILURES (During Shard Switch)
   D1. No matching shard exists
   D2. Target shard full
   D3. Permission denied
   D4. Transition blocked

RINA BLOCKING MECHANISMS
------------------------

1. Deva Rina -> Blocks health/resources
2. Rishi Rina -> Blocks learning/wisdom
3. Pitru Rina -> Blocks career/family
4. Manushya Rina -> Blocks social/opportunities
5. Bhuta Rina -> Blocks nature/animals

SAMSKARA RESISTANCE
-------------------

1. Deep patterns from past lives
2. Reinforced by repetition
3. Below conscious awareness
4. "Proven" survival strategies
5. Require dissolution, not suppression
```

---

## 📁 Related Files

- [Rina Debt System](./RINA_DEBT_SYSTEM_COMPLETE.md)
- [Sankalpa Pralaya Audit](./SANKALPA_PRALAYA_AUDIT_COMPLETE.md)
- [Chakra System](../entities/chakra_system.md)
- [Samskara Management](../purusha/samskaras.md)

