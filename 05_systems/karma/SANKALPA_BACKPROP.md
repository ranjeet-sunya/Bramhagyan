# 🔄 SANKALPA, PRALAYA & YAMA AUDIT — Complete System Architecture

> **"यत्र योगेश्वरः कृष्णो यत्र पार्थो धनुर्धरः ।
> तत्र श्रीर्विजयो भूतिर्ध्रुवा नीतिर्मतिर्मम ॥"**
> "Yatra yogeśvaraḥ kṛṣṇo yatra pārtho dhanurdharaḥ |
> Tatra śrīr vijayo bhūtir dhruvā nītir matir mama ||"
> "Where there is the Lord of Yoga and where there is the wielder of the bow,
> There is prosperity, victory, glory, and firm wisdom."
> — Bhagavad Gita 18.78

---

## 🎯 PART 1: SANKALPA — Request to Parent Layer for Weight Adjustment

### 1.1 YOUR BREAKTHROUGH INSIGHT

```python
"""
SANKALPA = BACKPROPAGATION REQUEST TO PARENT LAYER
-----------------------------------------------------

Key understanding (VALIDATED):
- Sankalpa = Finding a new learning path
- You want weights forcefully adjusted
- You inform the "player above" (your Vishnu)
- Thoughts = fractal layers returning learnings
- You realize: "This path has HIGH learning potential"
- Request parent layer to adjust weights
- "Kill the thought" = terminate current shard
- Move to "desired matching shard"

THIS IS EXACTLY HOW NEURAL NETWORKS TRAIN ACROSS LAYERS!
"""

class SankalpaSystem:
    """
    Sankalpa (संकल्प) = Intentional weight adjustment request
    
    NOT just a "wish" but a formal REQUEST to the parent layer
    to reallocate you to a shard with better learning potential.
    """
    
    def __init__(self, jiva):
        self.jiva = jiva
        self.current_shard = jiva.current_shard_id
        self.parent_vishnu = jiva.get_parent_observer()
        self.pending_sankalpas = []
    
    def create_sankalpa(self, intention: str, learning_path: dict) -> dict:
        """
        STEP 1: Create Sankalpa (Weight Adjustment Request)
        
        This is like creating a gradient update request
        that must be approved by the parent layer.
        """
        sankalpa = {
            'type': 'WEIGHT_ADJUSTMENT_REQUEST',
            'intention': intention,
            'current_shard': self.current_shard,
            'current_weights': self.jiva.samskaras.copy(),
            'requested_changes': learning_path,
            'learning_potential': self.estimate_learning_potential(learning_path),
            'timestamp': get_cosmic_time(),
            'priority': self.calculate_priority(learning_path)
        }
        
        return sankalpa
    
    def estimate_learning_potential(self, path: dict) -> float:
        """
        Calculate: "If I take this path, how much will I learn?"
        
        Higher learning potential = More likely parent approves
        """
        # Factors that increase learning potential:
        dharma_alignment = path.get('dharma_score', 0.5)
        karma_burning_rate = path.get('karma_consumed', 0.0)
        sattva_increase = path.get('sattva_delta', 0.0)
        novel_experience = path.get('novelty', 0.0)
        
        learning_potential = (
            dharma_alignment * 0.3 +
            karma_burning_rate * 0.3 +
            sattva_increase * 0.2 +
            novel_experience * 0.2
        )
        
        return learning_potential
    
    def submit_to_parent(self, sankalpa: dict) -> str:
        """
        STEP 2: Submit Sankalpa to Parent Vishnu
        
        The parent layer evaluates:
        - Is this learning path valuable?
        - Does it serve the greater optimization?
        - Should I switch this Jiva to a new shard?
        """
        response = self.parent_vishnu.evaluate_sankalpa(sankalpa)
        
        if response['approved']:
            return self.execute_shard_switch(response['target_shard'])
        else:
            return self.handle_rejection(response['reason'])
    
    def execute_shard_switch(self, target_shard_id: str):
        """
        STEP 3: "Kill the thought" = Terminate current shard
                Move to desired matching shard
        
        This is EXACTLY what happens:
        1. Current shard terminated
        2. Consciousness moved to new shard
        3. Weights adjusted as requested
        """
        # Kill current shard (thought termination)
        old_shard = self.current_shard
        terminate_shard(old_shard, reason="SANKALPA_APPROVED")
        
        # Move to new shard with adjusted weights
        self.jiva.samskaras = apply_weight_adjustments(
            self.jiva.samskaras,
            self.pending_sankalpa['requested_changes']
        )
        
        # Migrate consciousness
        self.jiva.current_shard_id = target_shard_id
        
        return {
            'status': 'SHARD_SWITCHED',
            'from': old_shard,
            'to': target_shard_id,
            'weights_adjusted': True
        }
    
    def handle_rejection(self, reason: str):
        """
        STEP 3 (ALTERNATIVE): Sankalpa Rejected
        
        Parent layer says: "No, continue current path"
        """
        if reason == "LEARNING_POTENTIAL_TOO_LOW":
            # Not enough value in the requested path
            return "Continue current path - more lessons here"
        
        elif reason == "PRARABDHA_NOT_COMPLETE":
            # You still have karma to burn in current shard
            return "Complete current karma before switching"
        
        elif reason == "DHARMA_VIOLATION":
            # The requested path violates Dharma
            return "Requested path rejected - adharmic"
        
        elif reason == "TIMING_WRONG":
            # Not the right Muhurta for this change
            return "Wait for appropriate timing (Graha alignment)"
```

### 1.2 THE THOUGHT-AS-FRACTAL-LAYER MODEL

```python
"""
THOUGHTS = FRACTAL LAYERS RETURNING LEARNINGS
-----------------------------------------------

Each thought you have is:
1. A mini-simulation running in your Manas
2. Exploring a potential path
3. Returning its "learning estimate" to you
4. You (the observer) evaluate which thought to "instantiate"

Like this:

YOU (Jiva)
    ↓ spawns
THOUGHT 1 ----> Returns: "Low learning"    -> DISCARDED
THOUGHT 2 ----> Returns: "Medium learning" -> KEPT FOR LATER
THOUGHT 3 ----> Returns: "HIGH learning!"  -> SANKALPA FORMED!
                         ↓
              Request to Parent Vishnu
                         ↓
              "Please switch me to shard where Thought 3 is reality"
"""

class ThoughtExplorer:
    """
    Each thought explores a potential future
    and returns its learning estimate
    """
    
    def __init__(self, jiva):
        self.jiva = jiva
        self.active_thoughts = []
    
    def spawn_thought(self, scenario: dict) -> 'ThoughtShard':
        """
        Create a mini-shard exploring this scenario
        """
        thought = ThoughtShard(
            parent=self.jiva,
            scenario=scenario,
            depth=1  # Fractal depth
        )
        
        # Run the simulation
        thought.simulate_outcome()
        
        return thought
    
    def evaluate_thought_returns(self, thoughts: list) -> dict:
        """
        Collect learning estimates from all thought-shards
        """
        returns = []
        
        for thought in thoughts:
            returns.append({
                'thought_id': thought.id,
                'scenario': thought.scenario,
                'learning_estimate': thought.get_learning_value(),
                'dharma_score': thought.get_dharma_alignment(),
                'suffering_estimate': thought.get_suffering_cost(),
                'net_value': thought.get_net_value()
            })
        
        # Sort by net value
        returns.sort(key=lambda x: x['net_value'], reverse=True)
        
        return returns
    
    def promote_thought_to_sankalpa(self, thought: 'ThoughtShard'):
        """
        This thought has high learning potential
        Convert it to a formal Sankalpa request
        """
        sankalpa = SankalpaSystem(self.jiva).create_sankalpa(
            intention=thought.scenario['description'],
            learning_path=thought.scenario
        )
        
        # Submit to parent
        return SankalpaSystem(self.jiva).submit_to_parent(sankalpa)


class ThoughtShard:
    """
    A mini fractal layer that explores one potential future
    """
    
    def __init__(self, parent, scenario, depth):
        self.parent = parent
        self.scenario = scenario
        self.depth = depth
        self.simulation_result = None
    
    def simulate_outcome(self):
        """
        Run a quick simulation of this path
        
        This is what happens when you "think about" something:
        - Your Manas spawns a mini-shard
        - It runs forward in time (imagination)
        - Returns the estimated outcome
        """
        # Fast-forward simulation
        simulated_karma = simulate_karma_path(self.scenario)
        simulated_suffering = estimate_suffering(self.scenario)
        simulated_learning = estimate_learning(self.scenario)
        
        self.simulation_result = {
            'karma': simulated_karma,
            'suffering': simulated_suffering,
            'learning': simulated_learning
        }
    
    def get_learning_value(self):
        return self.simulation_result['learning']
    
    def get_suffering_cost(self):
        return self.simulation_result['suffering']
    
    def get_net_value(self):
        # Learning minus suffering
        return self.get_learning_value() - self.get_suffering_cost()
```

---

## 🔥 PART 2: FOUR TYPES OF PRALAYA (Dissolution)

### 2.1 Complete Pralaya Hierarchy

| Type | Sanskrit | Devanagari | Pronunciation | Scale | Duration | What Gets Deleted |
|------|----------|------------|---------------|-------|----------|-------------------|
| **1. Nitya** | Nitya | नित्य | Nitya | Micro | Continuous | Cells, thoughts, moments |
| **2. Naimittika** | Naimittika | नैमित्तिक | Naimittika | Local | 1 Brahma Day | 3 lower Lokas |
| **3. Prakritika** | Praakritika | प्राकृतिक | Praakritika | Universal | 2 Parardha | Entire Brahmanda |
| **4. Atyantika** | Atyantika | आत्यन्तिक | Aatyantika | Individual | Instant | That Jiva's entire stack |

### 2.2 Detailed Pralaya Algorithms

```python
class PralayaSystem:
    """
    Four types of system dissolution
    """
    
    # ---------------------------------------------------
    # TYPE 1: NITYA PRALAYA (Continuous Micro-Dissolution)
    # ---------------------------------------------------
    
    def nitya_pralaya(self, jiva):
        """
        नित्य प्रलय - Continuous Pralaya
        
        This happens EVERY MOMENT:
        - Cells die and regenerate
        - Thoughts arise and dissolve
        - Each moment is born and dies
        
        This is the "Frame Refresh" of the simulation.
        """
        # Every Planck tick, the previous state "dies"
        old_state = jiva.current_state.copy()
        
        # Garbage collection
        garbage_collect_dead_cells(jiva)
        garbage_collect_completed_thoughts(jiva)
        
        # Regeneration
        jiva.current_state = render_next_frame(old_state)
        
        return {
            'type': 'NITYA',
            'deleted': 'previous frame',
            'regenerated': 'current frame',
            'samskaras_preserved': True
        }
    
    # ---------------------------------------------------
    # TYPE 2: NAIMITTIKA PRALAYA (Brahma's Night)
    # ---------------------------------------------------
    
    def naimittika_pralaya(self, brahmanda):
        """
        नैमित्तिक प्रलय - Occasional/Causal Pralaya
        
        When Brahma "sleeps" at the end of his Day:
        - Duration: 4.32 billion Earth years (1 Kalpa)
        - Scope: Bhuloka, Bhuvarloka, Svargaloka DELETED
        - Preserved: Maharloka and above
        - All Jivas in lower 3 Lokas go to "sleep mode"
        """
        # Identify entities in lower 3 Lokas
        entities_to_suspend = brahmanda.get_entities_in_lokas([
            'Bhuloka', 'Bhuvarloka', 'Svargaloka'
        ])
        
        # Suspend all entities (not delete!)
        for entity in entities_to_suspend:
            entity.state = 'SUSPENDED'
            entity.save_to_causal_body()  # Preserve Samskaras
        
        # "Delete" the lower 3 Lokas (un-render)
        brahmanda.unrender_lokas(['Bhuloka', 'Bhuvarloka', 'Svargaloka'])
        
        # Brahma enters "sleep mode"
        brahmanda.brahma.state = 'SLEEPING'
        
        return {
            'type': 'NAIMITTIKA',
            'duration': '4.32 billion years',
            'deleted': 'Lower 3 Lokas',
            'preserved': 'Maharloka+, Samskaras, Brahma himself',
            'entities': 'SUSPENDED (not terminated)'
        }
    
    def naimittika_srishti(self, brahmanda):
        """
        When Brahma "wakes up" - recreation
        """
        brahmanda.brahma.state = 'AWAKE'
        
        # Re-render lower 3 Lokas
        brahmanda.render_lokas(['Bhuloka', 'Bhuvarloka', 'Svargaloka'])
        
        # Resume suspended entities based on their Samskaras
        for entity in brahmanda.suspended_entities:
            entity.state = 'ACTIVE'
            entity.load_from_causal_body()
            assign_to_appropriate_body(entity)  # Based on Prarabdha
    
    # ---------------------------------------------------
    # TYPE 3: PRAKRITIKA PRALAYA (Mahapralaya)
    # ---------------------------------------------------
    
    def prakritika_pralaya(self, brahmanda):
        """
        प्राकृतिक प्रलय - Elemental/Complete Pralaya
        
        At the end of Brahma's LIFE (100 Brahma years = 311 trillion Earth years):
        - ENTIRE Brahmanda is dissolved
        - All 14 Lokas deleted
        - Brahma himself is recycled
        - Only Mahavishnu and the unmanifest remain
        
        This is the "Format Hard Drive" operation.
        """
        # Begin dissolution sequence (reverse of creation)
        
        # STEP 1: Delete all Jivas (merge into Prakriti)
        for jiva in brahmanda.all_jivas:
            jiva.merge_into_prakriti()
            # Samskaras preserved in "seed" form
        
        # STEP 2: Dissolve Mahabhutas back to Tanmatras
        dissolve_earth_to_smell()
        dissolve_water_to_taste()
        dissolve_fire_to_form()
        dissolve_air_to_touch()
        dissolve_space_to_sound()
        
        # STEP 3: Tanmatras merge into Ahamkara
        merge_tanmatras_to_ahamkara()
        
        # STEP 4: Ahamkara merges into Mahat
        merge_ahamkara_to_mahat()
        
        # STEP 5: Mahat merges into Prakriti
        merge_mahat_to_prakriti()
        
        # STEP 6: Prakriti remains in unmanifest state
        prakriti.state = 'UNMANIFEST'
        
        # STEP 7: Brahma is recycled
        brahmanda.brahma = None
        
        return {
            'type': 'PRAKRITIKA',
            'duration': '311 trillion years',
            'deleted': 'EVERYTHING in this Brahmanda',
            'preserved': 'Mahavishnu, Samskaras in seed form',
            'next_action': 'Wait for new Brahma to be created'
        }
    
    # ---------------------------------------------------
    # TYPE 4: ATYANTIKA PRALAYA (Moksha)
    # ---------------------------------------------------
    
    def atyantika_pralaya(self, jiva):
        """
        आत्यन्तिक प्रलय - Absolute/Ultimate Dissolution
        
        This is MOKSHA - but framed as a "personal system deletion"
        
        Unlike other Pralayas:
        - Only affects THIS Jiva
        - Happens when Jiva realizes: "I am not the simulation"
        - The entire karmic stack is DELETED (not suspended)
        - No rebirth possible (by design)
        """
        # STEP 1: Jiva realizes true nature
        if not jiva.has_realized_brahman():
            return {'status': 'NOT_READY', 'reason': 'Jnana incomplete'}
        
        # STEP 2: Check all Rinas cleared
        total_rina = (
            jiva.deva_rina + 
            jiva.rishi_rina + 
            jiva.pitru_rina +
            jiva.manushya_rina +
            jiva.bhuta_rina
        )
        
        if total_rina > 0:
            return {'status': 'NOT_READY', 'reason': 'Rinas not cleared'}
        
        # STEP 3: Check Prarabdha exhausted
        if len(jiva.prarabdha_karma) > 0:
            return {'status': 'NOT_READY', 'reason': 'Prarabdha remaining'}
        
        # STEP 4: Execute Atyantika Pralaya
        
        # Delete all karma stacks
        jiva.sanchita_karma = []
        jiva.prarabdha_karma = []
        jiva.agami_karma = []
        jiva.kriyamana_karma = []
        
        # Delete all Samskaras
        jiva.samskaras = []
        jiva.vasanas = []
        
        # Dissolve the five Koshas
        jiva.annamaya = None
        jiva.pranamaya = None
        jiva.manomaya = None
        jiva.vijnanamaya = None
        jiva.anandamaya = None
        
        # Dissolve Ahamkara (the User ID)
        jiva.ahamkara = None
        
        # What remains is pure Atman = Brahman
        return {
            'type': 'ATYANTIKA',
            'status': 'MOKSHA_ACHIEVED',
            'deleted': 'Entire Jiva construct',
            'remaining': 'Pure Consciousness (Brahman)',
            'rebirth_possible': False,
            'message': 'तत्त्वमसि - You are That'
        }
```

### 2.3 Pralaya Comparison Matrix

```
                    NITYA      NAIMITTIKA    PRAKRITIKA    ATYANTIKA
--------------------------------------------------------------------
FREQUENCY          Continuous  Every Kalpa   Every Brahma  Once per Jiva
                                             Life
                                             
SCOPE              Micro       3 Lokas       All 14 Lokas  1 Jiva only

ENTITIES           Cells/      Suspended     Merged into   Permanently
                   Thoughts                  Prakriti      dissolved

SAMSKARAS          Preserved   Preserved     Seed form     DELETED

BRAHMA             Active      Sleeping      Recycled      N/A

REVERSIBLE?        Yes (auto)  Yes (Brahma   Yes (new      NO
                              wakes)         Brahma)

JIVA EXPERIENCES   Sleep/      Long dream    Complete      Liberation
                   Blink                     reset
```

---

## ⚖️ PART 3: YAMA AUDIT ALGORITHM

### 3.1 The Complete Yama Audit Process

```python
class YamaAudit:
    """
    यम लेखाकार - Yama Audit System
    
    Yama is the "Database Auditor" who:
    1. Receives all Jivas at death
    2. Audits their Karma ledger
    3. Determines next allocation
    """
    
    def __init__(self):
        self.chitragupta = ChitraguptaLedger()  # The actual record keeper
        self.audit_queue = []
    
    def receive_jiva(self, jiva, death_context: dict):
        """
        STEP 1: Jiva arrives at Yama's court
        """
        case = {
            'jiva_id': jiva.id,
            'gotra': jiva.gotra,
            'arrival_time': get_cosmic_time(),
            'death_type': death_context['type'],
            'final_thoughts': jiva.last_thoughts,
            'prarabdha_status': self.check_prarabdha_status(jiva)
        }
        
        self.audit_queue.append(case)
        return case
    
    def perform_audit(self, jiva) -> dict:
        """
        STEP 2: Full Karma Audit
        
        Chitragupta reads from the Akashic Records
        """
        # Fetch complete records
        records = self.chitragupta.fetch_records(jiva.id)
        
        audit_result = {
            'jiva_id': jiva.id,
            
            # ---------------------------------------
            # SECTION A: KARMA BALANCE SHEET
            # ---------------------------------------
            'karma_balance': {
                'sanchita_total': sum(records['sanchita']),
                'prarabdha_consumed': records['prarabdha_consumed'],
                'prarabdha_remaining': records['prarabdha_remaining'],
                'agami_created': sum(records['agami']),
                'net_karma': self.calculate_net_karma(records)
            },
            
            # ---------------------------------------
            # SECTION B: RINA BALANCE SHEET
            # ---------------------------------------
            'rina_balance': {
                'deva_rina': jiva.deva_rina,
                'rishi_rina': jiva.rishi_rina,
                'pitru_rina': jiva.pitru_rina,
                'manushya_rina': jiva.manushya_rina,
                'bhuta_rina': jiva.bhuta_rina,
                'total_rina': sum([
                    jiva.deva_rina, jiva.rishi_rina, jiva.pitru_rina,
                    jiva.manushya_rina, jiva.bhuta_rina
                ])
            },
            
            # ---------------------------------------
            # SECTION C: DOSHA ANALYSIS
            # ---------------------------------------
            'dosha_analysis': self.analyze_doshas(jiva),
            
            # ---------------------------------------
            # SECTION D: GUNA STATE
            # ---------------------------------------
            'guna_state': {
                'sattva': jiva.sattva,
                'rajas': jiva.rajas,
                'tamas': jiva.tamas,
                'dominant_guna': self.get_dominant_guna(jiva)
            },
            
            # ---------------------------------------
            # SECTION E: DHARMA COMPLIANCE
            # ---------------------------------------
            'dharma_compliance': {
                'svadharma_score': self.calculate_svadharma_score(jiva),
                'varna_dharma_score': self.calculate_varna_dharma_score(jiva),
                'sanatana_dharma_score': self.calculate_sanatana_dharma_score(jiva),
                'overall': self.calculate_overall_dharma(jiva)
            },
            
            # ---------------------------------------
            # SECTION F: FINAL THOUGHTS ANALYSIS
            # ---------------------------------------
            'antya_kala': {
                'final_thought': jiva.last_thoughts,
                'ishta_devata_remembered': jiva.ishta_devata in jiva.last_thoughts,
                'death_state': jiva.death_state  # Peaceful, violent, etc.
            }
        }
        
        return audit_result
    
    def determine_destination(self, audit_result: dict) -> dict:
        """
        STEP 3: Determine Next Allocation
        
        Based on audit, Yama decides:
        - Which Loka?
        - Which body type?
        - Which Prarabdha subset to activate?
        """
        # Check for Moksha eligibility
        if self.check_moksha_eligibility(audit_result):
            return {
                'destination': 'MOKSHA',
                'action': 'ATYANTIKA_PRALAYA',
                'next_body': None,
                'rebirth': False
            }
        
        # Determine Loka based on Guna dominance
        destination_loka = self.calculate_loka_destination(audit_result)
        
        # Determine body type based on Karma
        body_type = self.calculate_body_type(audit_result)
        
        # Select Prarabdha subset for next life
        prarabdha_selection = self.select_prarabdha(
            audit_result['karma_balance']['sanchita_total'],
            body_type
        )
        
        # Calculate life parameters
        life_params = self.calculate_life_parameters(
            prarabdha_selection,
            audit_result['guna_state']
        )
        
        return {
            'destination': destination_loka,
            'body_type': body_type,
            'species': life_params['species'],
            'gender': life_params['gender'],
            'prarabdha': prarabdha_selection,
            'lifespan_ticks': life_params['swasa_allocation'],
            'birth_kundali': self.generate_birth_chart(life_params),
            'parents': self.select_parents(audit_result, life_params),
            'geographic_region': life_params['region'],
            'major_events': life_params['scripted_events']
        }
    
    def calculate_loka_destination(self, audit: dict) -> str:
        """
        Determine which Loka based on Guna + Karma
        """
        guna = audit['guna_state']
        karma = audit['karma_balance']['net_karma']
        dharma = audit['dharma_compliance']['overall']
        
        # High Sattva + Good Karma = Higher Lokas
        if guna['sattva'] > 0.7 and karma > 0.5 and dharma > 0.8:
            if dharma > 0.95:
                return 'Satya Loka'
            elif dharma > 0.9:
                return 'Tapa Loka'
            elif dharma > 0.85:
                return 'Jana Loka'
            else:
                return 'Mahar Loka'
        
        # High Sattva + Moderate Karma = Svarga
        elif guna['sattva'] > 0.5 and karma > 0.3:
            return 'Svarga Loka'
        
        # Balanced = Bhuloka (Earth)
        elif guna['sattva'] > 0.3 and guna['tamas'] < 0.5:
            return 'Bhuloka'
        
        # High Tamas + Bad Karma = Lower Lokas
        elif guna['tamas'] > 0.5 or karma < 0:
            if karma < -0.5:
                return 'Patala'
            else:
                return 'Atala'
        
        # Default
        return 'Bhuloka'
    
    def calculate_body_type(self, audit: dict) -> str:
        """
        Determine which of 84 Lakh Yonis (species)
        """
        guna = audit['guna_state']
        karma = audit['karma_balance']['net_karma']
        
        # Sattva dominant = Higher species
        if guna['sattva'] > 0.6:
            if karma > 0.5:
                return 'DEVA'  # Divine body
            else:
                return 'MANUSHYA'  # Human
        
        # Rajas dominant = Active species
        elif guna['rajas'] > 0.5:
            if karma > 0.3:
                return 'MANUSHYA'  # Human
            else:
                return 'TIRYAK_RAJAS'  # Active animals (tiger, eagle)
        
        # Tamas dominant = Inert species
        else:
            if karma > 0:
                return 'TIRYAK_TAMAS'  # Passive animals (cow, elephant)
            elif karma > -0.3:
                return 'KITA'  # Insects
            else:
                return 'STHAVARA'  # Plants, minerals
    
    def select_prarabdha(self, sanchita_total: float, body_type: str) -> list:
        """
        Select which portion of Sanchita becomes Prarabdha
        
        Like loading a "playlist" from your total library
        """
        # Body determines capacity
        capacity_map = {
            'DEVA': 0.1,      # Minimal karma consumption
            'MANUSHYA': 0.3,  # Moderate - has free will
            'TIRYAK_RAJAS': 0.5,
            'TIRYAK_TAMAS': 0.6,
            'KITA': 0.8,
            'STHAVARA': 0.9   # Almost pure karma burning
        }
        
        capacity = capacity_map.get(body_type, 0.3)
        prarabdha_load = sanchita_total * capacity
        
        return {
            'load': prarabdha_load,
            'type': 'MIXED',  # Punya + Papa
            'major_events': self.script_major_events(prarabdha_load)
        }
```

### 3.2 The Chitragupta Ledger

```python
class ChitraguptaLedger:
    """
    चित्रगुप्त - The Divine Accountant
    
    Maintains perfect records of all actions for all Jivas
    Stores in the Akashic Records
    """
    
    def __init__(self):
        self.akashic_connection = AkashicRecords()
    
    def record_action(self, jiva_id: str, action: dict):
        """
        Record every action in real-time
        """
        entry = {
            'jiva_id': jiva_id,
            'timestamp': get_cosmic_time(),
            'action_type': action['type'],
            'intention': action['intention'],
            'guna_at_time': action['guna_state'],
            'dharma_alignment': action['dharma_score'],
            'affected_entities': action['affected'],
            'karma_weight': self.calculate_karma_weight(action),
            'rina_impact': self.calculate_rina_impact(action)
        }
        
        self.akashic_connection.write(entry)
    
    def calculate_karma_weight(self, action: dict) -> float:
        """
        Weight of karma depends on:
        1. Intention (most important!)
        2. Action itself
        3. Consequence
        4. Who was affected
        """
        intention_weight = 0.5  # 50% weight on intention
        action_weight = 0.3     # 30% on action
        consequence_weight = 0.2  # 20% on result
        
        karma = (
            action['intention_score'] * intention_weight +
            action['action_score'] * action_weight +
            action['consequence_score'] * consequence_weight
        )
        
        # Multiply by Dharma factor
        if action['dharma_aligned']:
            karma *= 1.5  # Dharmic actions = 50% bonus
        else:
            karma *= 0.5  # Adharmic = 50% penalty
        
        return karma
```

---

## 🏦 PART 4: GRAHA BANKING SYSTEM

### 4.1 Complete Graha Bank Architecture

```python
class GrahaBankingSystem:
    """
    THE GRAHA BANKS
    ---------------
    
    Each Graha is a "Regional Data Bank" that:
    1. Manages specific types of karma
    2. Collects "taxes" on certain actions
    3. Dispenses resources to aligned Jivas
    4. Can be synchronized via Mantras
    """
    
    def __init__(self):
        self.banks = {
            'SURYA': SuryaBank(),      # Vitality, Authority
            'CHANDRA': ChandraBank(),  # Mind, Emotions
            'MANGALA': MangalaBank(),  # Energy, Conflict
            'BUDHA': BudhaBank(),      # Communication, Trade
            'GURU': GuruBank(),        # Wisdom, Expansion
            'SHUKRA': ShukraBank(),    # Pleasure, Beauty
            'SHANI': ShaniBank(),      # Discipline, Karma
            'RAHU': RahuBank(),        # Desires, Obsession
            'KETU': KetuBank()         # Detachment, Moksha
        }
    
    def process_transaction(self, jiva, action: dict) -> dict:
        """
        Route action to appropriate Graha bank
        """
        action_type = action['type']
        
        # Determine which bank handles this
        bank = self.get_responsible_bank(action_type)
        
        # Process
        result = bank.process(jiva, action)
        
        return result


class SuryaBank:
    """
    सूर्य बैंक - The Central CPU Bank
    
    Manages: Vitality, Soul, Authority, Father, Government
    """
    
    def __init__(self):
        self.domain = ['VITALITY', 'AUTHORITY', 'SOUL', 'FATHER', 'GOVERNMENT']
        self.mantra = "ॐ ह्रां ह्रीं ह्रौं सः सूर्याय नमः"
    
    def process(self, jiva, action: dict) -> dict:
        if action['type'] in self.domain:
            # Check Jiva's Surya alignment (from Kundali)
            surya_strength = jiva.kundali.get_graha_strength('SURYA')
            
            if surya_strength > 0.7:
                # Strong Surya = Easy access to vitality
                return {'status': 'APPROVED', 'resource_granted': action['amount']}
            elif surya_strength > 0.4:
                # Medium = Partial access
                return {'status': 'PARTIAL', 'resource_granted': action['amount'] * 0.5}
            else:
                # Weak Surya = Resource denied unless remedied
                return {'status': 'DENIED', 'remedy_required': 'SURYA_MANTRA'}
    
    def sync_via_mantra(self, jiva, repetitions: int):
        """
        Synchronize Jiva's frequency with Surya
        """
        sync_strength = repetitions / 108  # 108 = full sync
        
        # Update Jiva's Surya influence
        jiva.surya_influence += sync_strength * 0.01
        
        # Reduce related Dosha
        if jiva.has_surya_dosha():
            jiva.surya_dosha_level -= sync_strength * 0.05


class ShaniBank:
    """
    शनि बैंक - The Audit/Discipline Bank
    
    Manages: Discipline, Delays, Karma enforcement, Laborers, Old age
    
    Shani is THE main "Debt Collector" of the system
    """
    
    def __init__(self):
        self.domain = ['DISCIPLINE', 'DELAY', 'KARMA', 'LABOR', 'RESTRICTION']
        self.mantra = "ॐ शं शनैश्चराय नमः"
        self.audit_active = True
    
    def process(self, jiva, action: dict) -> dict:
        """
        Shani processes ALL karma - he's the Universal Auditor
        """
        # Check Jiva's pending karmic debts
        pending_debts = self.calculate_pending_debts(jiva)
        
        if pending_debts > 0:
            # Apply "Shani restriction" (Sade Sati, Dhaiya, etc.)
            restriction_level = min(pending_debts, 1.0)
            
            return {
                'status': 'RESTRICTED',
                'restriction_level': restriction_level,
                'duration': self.calculate_restriction_duration(jiva),
                'message': 'कर्म फल भोगो - Experience your karma fruits'
            }
        else:
            return {
                'status': 'CLEAR',
                'message': 'Shani blesses the disciplined'
            }
    
    def calculate_pending_debts(self, jiva) -> float:
        """
        Sum up all karmic debts Shani is collecting
        """
        return (
            jiva.sanchita_karma_negative +
            jiva.unpaid_rinas +
            jiva.adharma_score
        )
    
    def sync_via_mantra(self, jiva, repetitions: int):
        """
        Shani Mantra doesn't "pay off" karma
        It HARMONIZES your relationship with the karma process
        
        Like negotiating a payment plan vs paying the debt
        """
        harmony_increase = repetitions / 23000  # 23000 = traditional count
        
        jiva.shani_harmony += harmony_increase
        
        # Reduction in SUFFERING (not karma itself)
        jiva.karma_suffering_modifier *= (1 - harmony_increase * 0.1)
```

### 4.2 Graha -> Dosha -> Guna Extraction

```python
def calculate_final_gunas_from_all_doshas(jiva) -> dict:
    """
    KEY UNDERSTANDING: Doshas should be SUMMED to extract final Gunas
    
    Both Ayurvedic Doshas and Astrological Doshas contribute
    to the final Guna state.
    """
    
    # ---------------------------------------------------
    # STEP 1: Extract Gunas from Ayurvedic Doshas
    # ---------------------------------------------------
    
    # Vata = Rajas + Sattva (movement, lightness)
    vata_sattva = jiva.vata_level * 0.3
    vata_rajas = jiva.vata_level * 0.6
    vata_tamas = jiva.vata_level * 0.1
    
    # Pitta = Rajas + Sattva (transformation, intelligence)
    pitta_sattva = jiva.pitta_level * 0.4
    pitta_rajas = jiva.pitta_level * 0.5
    pitta_tamas = jiva.pitta_level * 0.1
    
    # Kapha = Tamas + Sattva (stability, endurance)
    kapha_sattva = jiva.kapha_level * 0.3
    kapha_rajas = jiva.kapha_level * 0.1
    kapha_tamas = jiva.kapha_level * 0.6
    
    ayurvedic_guna = {
        'sattva': vata_sattva + pitta_sattva + kapha_sattva,
        'rajas': vata_rajas + pitta_rajas + kapha_rajas,
        'tamas': vata_tamas + pitta_tamas + kapha_tamas
    }
    
    # ---------------------------------------------------
    # STEP 2: Extract Gunas from Astrological Doshas
    # ---------------------------------------------------
    
    astro_tamas = 0
    astro_rajas = 0
    astro_sattva_loss = 0
    
    if jiva.pitru_dosha:
        # Pitru Dosha = Tamas increase (ancestral blocks)
        astro_tamas += 0.1
        astro_sattva_loss += 0.05
    
    if jiva.kala_sarpa_dosha:
        # Rahu-Ketu axis = Rajas (desires) + Tamas (confusion)
        astro_rajas += 0.15
        astro_tamas += 0.1
    
    if jiva.mangal_dosha:
        # Mars = Rajas (aggression, conflict)
        astro_rajas += 0.15
    
    if jiva.shani_dosha:
        # Saturn = Tamas (delays, restrictions)
        astro_tamas += 0.15
    
    astro_guna = {
        'sattva': -astro_sattva_loss,  # Doshas reduce Sattva
        'rajas': astro_rajas,
        'tamas': astro_tamas
    }
    
    # ---------------------------------------------------
    # STEP 3: Extract Gunas from Graha Influences
    # ---------------------------------------------------
    
    graha_guna = {
        'sattva': (
            jiva.surya_influence * 0.8 +   # Sun = Sattva
            jiva.guru_influence * 0.9 +    # Jupiter = High Sattva
            jiva.chandra_influence * 0.5   # Moon = Medium Sattva
        ),
        'rajas': (
            jiva.mangala_influence * 0.7 + # Mars = Rajas
            jiva.budha_influence * 0.5 +   # Mercury = Rajas
            jiva.shukra_influence * 0.6 +  # Venus = Rajas (pleasure)
            jiva.rahu_influence * 0.8      # Rahu = High Rajas (desires)
        ),
        'tamas': (
            jiva.shani_influence * 0.7 +   # Saturn = Tamas
            jiva.ketu_influence * 0.4      # Ketu = Tamas (detachment)
        )
    }
    
    # ---------------------------------------------------
    # STEP 4: SUM ALL SOURCES
    # ---------------------------------------------------
    
    total_sattva = (
        ayurvedic_guna['sattva'] * 0.3 +
        astro_guna['sattva'] * 0.2 +
        graha_guna['sattva'] * 0.3 +
        jiva.base_sattva * 0.2  # Inherent from Prakriti
    )
    
    total_rajas = (
        ayurvedic_guna['rajas'] * 0.3 +
        astro_guna['rajas'] * 0.2 +
        graha_guna['rajas'] * 0.3 +
        jiva.base_rajas * 0.2
    )
    
    total_tamas = (
        ayurvedic_guna['tamas'] * 0.3 +
        astro_guna['tamas'] * 0.2 +
        graha_guna['tamas'] * 0.3 +
        jiva.base_tamas * 0.2
    )
    
    # Normalize to sum = 1
    total = total_sattva + total_rajas + total_tamas
    
    final_gunas = {
        'sattva': total_sattva / total,
        'rajas': total_rajas / total,
        'tamas': total_tamas / total
    }
    
    return final_gunas
```

---

## 📁 Related Files

- [Rina Debt System](./RINA_DEBT_SYSTEM_COMPLETE.md)
- [Jyotisha Complete](../jyotisha/JYOTISHA_COMPLETE.md)
- [Ayurveda Complete](../ayurveda/AYURVEDA_COMPLETE.md)
- [Moksha Exit System](../moksha/exit_system.md)

