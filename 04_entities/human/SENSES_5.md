# 👁️ PANCHA JNANENDRIYA — Five Senses Backend Architecture

> **"इन्द्रियाणि हयानाहुर्विषयांस्तेषु गोचरान्"**
> "Indriyani hayān āhur vishayāns teshu gocharān"
> "The senses are called horses, their objects are the paths they tread."
> — Katha Upanishad 1.3.4

> **"शब्दः स्पर्शश्च रूपं च रसो गन्धश्च पञ्चमः"**
> "Shabdah sparshash cha rupam cha raso gandhash cha panchamah"
> "Sound, Touch, Form, Taste, and Smell are the five."
> — Sankhya Karika 25

---

## 🌀 THE BACKEND ARCHITECTURE: TANMATRA -> INDRIYA -> MANAS

```
--------------------------------------------------------------------------------
                     SENSE PERCEPTION BACKEND ARCHITECTURE                       
----------------------------------------------------------------------------------�
                                                                                
   LEVEL 1: TANMATRA (तन्मात्र) — Subtle Data Packets                          
   ---------------------------------------------------                          
   Pure information before rendering. "That-only" (tan-matra)                   
   These are the RAW DATA before sense organs process them.                     
                                                                                
   LEVEL 2: MAHABHUTA (महाभूत) — Medium/Carrier                                 
   ---------------------------------------------------                          
   The physical medium that carries the Tanmatra.                               
                                                                                
   LEVEL 3: INDRIYA (इन्द्रिय) — Sensor Hardware                                
   ---------------------------------------------------                          
   The physical organ that receives and converts data.                          
                                                                                
   LEVEL 4: MANAS (मनस्) — Signal Processing                                    
   ---------------------------------------------------                          
   Mind processes raw sensor data into coherent perception.                     
                                                                                
   LEVEL 5: BUDDHI (बुद्धि) — Interpretation & Decision                         
   ---------------------------------------------------                          
   Intellect interprets and decides what the data means.                        
                                                                                
   LEVEL 6: AHAMKARA (अहंकार) — Self-Reference                                  
   ---------------------------------------------------                          
   Ego tags perception as "my experience."                                      
                                                                                
   LEVEL 7: PURUSHA/ATMAN (पुरुष/आत्मन्) — Witness                              
   ---------------------------------------------------                          
   Consciousness witnesses the processed experience.                            
                                                                                
--------------------------------------------------------------------------------
```

---

## 📊 COMPLETE FIVE SENSES MAPPING

| # | Sense | Sanskrit | Tanmatra | Mahabhuta | Organ | Vedic Function |
|---|-------|----------|----------|-----------|-------|----------------|
| 1 | **Hearing** | Shrotra (श्रोत्र) | Shabda (शब्द) | Akasha (आकाश) | Ear | Vibration detection |
| 2 | **Touch** | Tvak (त्वक्) | Sparsha (स्पर्श) | Vayu (वायु) | Skin | Pressure/motion sensing |
| 3 | **Sight** | Chakshu (चक्षु) | Rupa (रूप) | Agni (अग्नि) | Eye | Light/color detection |
| 4 | **Taste** | Rasana (रसना) | Rasa (रस) | Jala (जल) | Tongue | Chemical sensing (wet) |
| 5 | **Smell** | Ghrana (घ्राण) | Gandha (गन्ध) | Prithvi (पृथ्वी) | Nose | Particle detection |

---

## 👂 1. HEARING / Shrotra (श्रोत्र) — SHABDA (Sound)

### Frontend (Science)
```
Sound = Mechanical pressure waves through medium (air, water, solid)
Frequency: 20 Hz - 20 kHz (human range)
Mechanism: Eardrum -> Ossicles -> Cochlea -> Hair cells -> Neural signals
```

### Backend (Vedic)
```python
class ShrotraIndriya:
    """
    HEARING = SHABDA TANMATRA DETECTION
    ------------------------------------
    
    Shabda (शब्द) is the FIRST Tanmatra to emerge from Brahman.
    "From Shunya came Shabda, from Shabda came all."
    
    Sound is PRIOR to all other senses because:
    • Akasha (space) is the first element
    • Akasha's quality is Shabda
    • Without Akasha, nothing else can manifest
    • Mantras work through Shabda (sound = creation)
    """
    
    # BACKEND PROCESS
    tanmatra = "Shabda (शब्द)"       # Pure vibration pattern
    mahabhuta = "Akasha (आकाश)"      # Space carries vibration
    indriya = "Shrotra (श्रोत्र)"    # Ear apparatus
    
    def backend_hearing_process(self, shabda_wave):
        """
        Step 1: SHABDA exists in Akasha (subtle vibration pattern)
        Step 2: Akasha transmits Shabda through space
        Step 3: Shrotra (ear) receives Akasha vibration
        Step 4: Converts to neural Prana signals
        Step 5: Manas processes raw signal
        Step 6: Buddhi interprets meaning
        Step 7: Ahamkara says "I hear this"
        Step 8: Purusha witnesses the experience
        """
        
        # Why hearing is most SUBTLE:
        # - Akasha is the subtlest element
        # - Sound exists even in darkness
        # - Mantras affect reality through Shabda
        # - OM (Pranava) is the primordial sound
        
        return {
            'guna_composition': {'S': 0.6, 'R': 0.3, 'T': 0.1},  # Sattva dominant
            'detection_range': '20 Hz - 20 kHz (human)',
            'akasha_dependency': 'High (needs space medium)',
            'why_first': 'Shabda = Brahman\'s first vibration',
        }
```

### Why Sound is FIRST (Backend Logic)
```
MANIFESTATION ORDER (From Brahman):
-------------------------------------
1. Brahman -> Shabda (sound/vibration)
2. Shabda -> Akasha (space to hold vibration)
3. Akasha + Shabda -> Vayu (motion in space)
4. Vayu + Sparsha -> Agni (friction creates fire)
5. Agni + Rupa -> Jala (cooling creates water)
6. Jala + Rasa -> Prithvi (solidification creates earth)

EACH ELEMENT CARRIES ALL PREVIOUS TANMATRAS:
• Akasha = Shabda only
• Vayu = Shabda + Sparsha
• Agni = Shabda + Sparsha + Rupa
• Jala = Shabda + Sparsha + Rupa + Rasa
• Prithvi = ALL 5 (Shabda + Sparsha + Rupa + Rasa + Gandha)
```

---

## ✋ 2. TOUCH / Tvak (त्वक्) — SPARSHA (Contact)

### Frontend (Science)
```
Touch = Mechanoreceptors detecting pressure, temperature, pain
Types: Pressure, Temperature, Pain (nociception), Proprioception
Mechanism: Nerve endings -> Spinal cord -> Brain
```

### Backend (Vedic)
```python
class TvakIndriya:
    """
    TOUCH = SPARSHA TANMATRA DETECTION
    -----------------------------------
    
    Sparsha (स्पर्श) is the quality of Vayu (Air/Motion).
    Touch detects MOTION and CONTACT.
    
    Touch is the sense of BOUNDARY detection:
    • Where does "I" end and "other" begin?
    • Pressure = external Vayu meeting body Vayu
    • Temperature = Rajas level difference
    """
    
    tanmatra = "Sparsha (स्पर्श)"     # Pure contact/motion pattern
    mahabhuta = "Vayu (वायु)"         # Air carries touch info
    indriya = "Tvak (त्वक्)"         # Skin apparatus
    
    def backend_touch_process(self, sparsha_signal):
        """
        TOUCH = GUNA INTERACTION AT BOUNDARY
        
        What we feel as "touch" is:
        1. Two Guna-systems meeting at a boundary
        2. Information exchange between systems
        3. The "cost" of this exchange = sensation
        
        Pressure = High Tamas density meeting low density
        Temperature = Rajas differential (heat = high Rajas)
        Pain = Damage signal (high Tamas accumulation)
        Pleasure = Harmonious Guna exchange
        """
        
        # Temperature is Rajas differential
        hot = 'High Rajas in object > Body Rajas'
        cold = 'Low Rajas in object < Body Rajas'
        
        # Pressure is Tamas interaction
        hard_pressure = 'High Tamas meets High Tamas'
        soft_touch = 'Low Tamas meets Low Tamas'
        
        return {
            'guna_composition': {'S': 0.3, 'R': 0.5, 'T': 0.2},  # Rajas dominant
            'detection_types': ['pressure', 'temperature', 'pain', 'pleasure'],
            'vayu_dependency': 'High (motion/vibration medium)',
            'why_second': 'Vayu emerges from Akasha, carries motion',
        }
```

### Touch as Guna Differential Detection
```
WHAT TOUCH ACTUALLY DETECTS (Backend):
--------------------------------------
• PRESSURE = Tamas differential at boundary
  - Hard surface = high Tamas meeting your Tamas
  - Soft surface = low Tamas, less resistance

• TEMPERATURE = Rajas differential
  - Hot = object has MORE Rajas than body -> flows IN
  - Cold = object has LESS Rajas -> flows OUT
  - (Heat always flows from high to low Rajas)

• PAIN = Damage signal (excessive Guna disturbance)
  - Sharp pain = sudden high Tamas puncture
  - Burning = excessive Rajas destroying tissue
  - Ache = chronic Guna imbalance

• PLEASURE = Harmonious Guna resonance
  - Massage = Rajas redistribution (circulation)
  - Comfort = Guna balance maintained
```

---

## 👁️ 3. SIGHT / Chakshu (चक्षु) — RUPA (Form)

### Frontend (Science)
```
Vision = Electromagnetic radiation (380-740 nm wavelength)
Mechanism: Cornea -> Lens -> Retina -> Rods/Cones -> Optic nerve -> Brain
Color = Different wavelength frequencies
```

### Backend (Vedic)
```python
class ChakshuIndriya:
    """
    SIGHT = RUPA TANMATRA DETECTION
    --------------------------------
    
    Rupa (रूप) is the quality of Agni (Fire/Light).
    Vision detects FORM and COLOR.
    
    Agni = Light = Sattva carrier
    That's why we say "see the light" for understanding.
    
    The eye is a FIRE organ:
    • Projects Tejas (inner light) outward
    • Receives external Tejas (reflected light)
    • Without inner Tejas, no perception (blind)
    """
    
    tanmatra = "Rupa (रूप)"          # Pure form/color pattern
    mahabhuta = "Agni (अग्नि)"        # Fire/light carries form
    indriya = "Chakshu (चक्षु)"      # Eye apparatus
    
    def backend_vision_process(self, rupa_signal):
        """
        VISION = RENDER FRAME RECEPTION
        
        The eye is like a DISPLAY receiving frames:
        1. Maya renders objects into Rupa (form/color)
        2. Agni (light) carries Rupa information
        3. Chakshu receives and converts to Prana signals
        4. Manas assembles frame from pixels
        5. Buddhi interprets objects/meanings
        
        WHY VISION DEPENDS ON AGNI (LIGHT):
        • Without Agni, Rupa cannot travel
        • In darkness, Rupa exists but isn't transmitted
        • Sun = Cosmic Agni source for Bhuloka
        • Inner Tejas = Why we "see" dreams
        """
        
        # Color = Guna signature in light
        colors_as_gunas = {
            'white': {'S': 0.8, 'R': 0.1, 'T': 0.1},   # Pure Sattva
            'red': {'S': 0.2, 'R': 0.7, 'T': 0.1},     # Rajas dominant
            'black': {'S': 0.1, 'R': 0.1, 'T': 0.8},   # Tamas dominant
            'yellow': {'S': 0.5, 'R': 0.4, 'T': 0.1},  # Sattva-Rajas
            'blue': {'S': 0.6, 'R': 0.2, 'T': 0.2},    # Sattva-calm
        }
        
        return {
            'guna_composition': {'S': 0.5, 'R': 0.4, 'T': 0.1},  # Sattva-Rajas
            'detection_range': '380-740 nm (visible spectrum)',
            'agni_dependency': 'Critical (no light = no vision)',
            'why_third': 'Agni emerges from Vayu friction',
        }
```

### Color as Guna Signature
```
COLOR GUNA MAPPING (Backend):
-----------------------------
• WHITE = Pure Sattva (all colors = clarity)
• RED = Rajas dominant (fire, passion, blood)
• BLUE = Sattva-calm (sky, water, peace)
• YELLOW = Sattva-Rajas (sun, gold, wisdom)
• GREEN = Balance (nature, growth)
• BLACK = Tamas dominant (absence, absorption)

WHY SUNRISE/SUNSET ARE RED-ORANGE:
• Light travels through more atmosphere
• Sattva (blue) scatters first
• Rajas (red-orange) travels further
• Sunrise/sunset = Rajas time (activity transition)

WHY SKY IS BLUE:
• Short wavelength (Sattva) scatters easily
• We see scattered Sattva-light
• Sky = Sattva display layer
```

---

## 👅 4. TASTE / Rasana (रसना) — RASA (Essence)

### Frontend (Science)
```
Taste = Chemical receptors detecting dissolved molecules
Types: Sweet, Sour, Salty, Bitter, Umami, (Fat?)
Mechanism: Taste buds -> Gustatory nerves -> Brain
Requires: Saliva (water) to dissolve chemicals
```

### Backend (Vedic)
```python
class RasanaIndriya:
    """
    TASTE = RASA TANMATRA DETECTION
    --------------------------------
    
    Rasa (रस) is the quality of Jala (Water).
    Taste detects ESSENCE and NUTRITION.
    
    Why water is required:
    • Rasa only transmits through Jala
    • Dry tongue cannot taste
    • Saliva = Jala medium for Rasa
    
    The 6 Rasas (Shad-Rasa / षड्-रस):
    1. Madhura (Sweet) - Earth + Water
    2. Amla (Sour) - Earth + Fire
    3. Lavana (Salty) - Water + Fire
    4. Tikta (Bitter) - Air + Ether
    5. Katu (Pungent) - Air + Fire
    6. Kashaya (Astringent) - Air + Earth
    """
    
    tanmatra = "Rasa (रस)"           # Pure essence/flavor pattern
    mahabhuta = "Jala (जल)"          # Water carries taste
    indriya = "Rasana (रसना)"        # Tongue apparatus
    
    def backend_taste_process(self, rasa_signal):
        """
        TASTE = NUTRITIONAL DATA EXTRACTION
        
        Taste tells the body what's coming:
        1. Sweet = Energy incoming (carbs)
        2. Sour = Acidic (vitamin C, fermented)
        3. Salty = Minerals (electrolytes)
        4. Bitter = Potentially toxic (alkaloids)
        5. Pungent = Metabolic activator (spices)
        6. Astringent = Binding/drying (tannins)
        
        Each Rasa has Guna composition:
        """
        
        shad_rasa_gunas = {
            'madhura_sweet': {'S': 0.6, 'R': 0.3, 'T': 0.1},   # Nourishing
            'amla_sour': {'S': 0.2, 'R': 0.5, 'T': 0.3},       # Stimulating
            'lavana_salty': {'S': 0.3, 'R': 0.4, 'T': 0.3},    # Retaining
            'tikta_bitter': {'S': 0.5, 'R': 0.3, 'T': 0.2},    # Cleansing
            'katu_pungent': {'S': 0.2, 'R': 0.7, 'T': 0.1},    # Heating
            'kashaya_astringent': {'S': 0.4, 'R': 0.2, 'T': 0.4}, # Cooling
        }
        
        return {
            'guna_composition': {'S': 0.3, 'R': 0.3, 'T': 0.4},  # Balanced-Tamas
            'detection_types': list(shad_rasa_gunas.keys()),
            'jala_dependency': 'Critical (needs water/saliva)',
            'why_fourth': 'Jala emerges from Agni cooling',
        }
```

### Six Tastes and Their Functions
```
SHAD-RASA (6 Tastes) — BACKEND FUNCTIONS:
-------------------------------------------

1. MADHURA (मधुर) — Sweet
   • Mahabhuta: Prithvi + Jala
   • Guna: Sattva dominant
   • Effect: Builds tissue, calms mind
   • Examples: Sugar, rice, milk

2. AMLA (अम्ल) — Sour
   • Mahabhuta: Prithvi + Agni
   • Guna: Rajas dominant
   • Effect: Stimulates digestion, awakens
   • Examples: Lemon, yogurt, vinegar

3. LAVANA (लवण) — Salty
   • Mahabhuta: Jala + Agni
   • Guna: Rajas-Tamas
   • Effect: Retains water, grounds
   • Examples: Salt, seaweed

4. TIKTA (तिक्त) — Bitter
   • Mahabhuta: Vayu + Akasha
   • Guna: Sattva (cleansing)
   • Effect: Detoxifies, clears
   • Examples: Neem, turmeric, coffee

5. KATU (कटु) — Pungent
   • Mahabhuta: Vayu + Agni
   • Guna: Rajas dominant
   • Effect: Increases metabolism, heat
   • Examples: Chili, ginger, pepper

6. KASHAYA (कषाय) — Astringent
   • Mahabhuta: Vayu + Prithvi
   • Guna: Sattva-Tamas
   • Effect: Contracts, dries, binds
   • Examples: Unripe banana, tea
```

---

## 👃 5. SMELL / Ghrana (घ्राण) — GANDHA (Scent)

### Frontend (Science)
```
Smell = Olfactory receptors detecting airborne molecules
Mechanism: Nose -> Olfactory bulb -> Limbic system -> Brain
~400 receptor types, can detect 1 trillion+ distinct scents
Most "primitive" sense (direct brain connection)
```

### Backend (Vedic)
```python
class GhranaIndriya:
    """
    SMELL = GANDHA TANMATRA DETECTION
    ---------------------------------
    
    Gandha (गन्ध) is the quality of Prithvi (Earth).
    Smell detects PARTICLES — the most gross Tanmatra.
    
    Prithvi is the FINAL element, containing ALL Tanmatras:
    • Prithvi has Shabda + Sparsha + Rupa + Rasa + Gandha
    • That's why earth-based things have all 5 qualities
    • Smell requires PARTICLES (matter) to travel
    
    Smell is the MOST GROUNDED sense:
    • Direct connection to survival (food, danger)
    • Linked to memory (limbic system)
    • Animals rely heavily on smell
    """
    
    tanmatra = "Gandha (गन्ध)"        # Pure scent pattern
    mahabhuta = "Prithvi (पृथ्वी)"    # Earth carries scent particles
    indriya = "Ghrana (घ्राण)"       # Nose apparatus
    
    def backend_smell_process(self, gandha_signal):
        """
        SMELL = PARTICLE DATA DETECTION
        
        Smell requires physical particles:
        1. Object releases Gandha-particles
        2. Vayu (air) carries particles to nose
        3. Ghrana receptors detect molecular pattern
        4. Direct limbic connection (emotion/memory)
        5. Manas associates with past experiences
        
        WHY SMELL IS MOST "EARTHY":
        • Only solid objects have strong smell
        • Gases have minimal smell (except some)
        • More Tamas = stronger Gandha potential
        • Earth is the densest, most Tamas element
        """
        
        return {
            'guna_composition': {'S': 0.2, 'R': 0.3, 'T': 0.5},  # Tamas dominant
            'detection_range': '1 trillion+ distinct scents',
            'prithvi_dependency': 'Critical (needs particles)',
            'why_fifth': 'Prithvi is final, most gross element',
            'memory_link': 'Direct limbic connection (survival)',
        }
```

### Why Smell Triggers Memory
```
SMELL-MEMORY CONNECTION (Backend):
-----------------------------------
• Smell bypasses Manas and goes DIRECTLY to Chitta (memory)
• This is why smells trigger instant, powerful memories
• Other senses process through Manas first (cognitive delay)

BACKEND REASON:
• Prithvi (earth) contains ALL 5 Tanmatras
• Gandha is the most "complete" information packet
• It carries compressed data from all elements
• Direct write to Chitta = survival advantage
• "This smell = danger" must be INSTANT

GUNA LOGIC:
• Tamas dominant = tied to physical matter
• Matter = survival (food, shelter, threat)
• Survival data = direct Chitta access
```

---

## 🔄 COMPLETE PERCEPTION PIPELINE

```
--------------------------------------------------------------------------------
                    COMPLETE SENSE PERCEPTION PIPELINE                          
----------------------------------------------------------------------------------�
                                                                                
   EXTERNAL WORLD (Maya's render)                                               
                                                                               
          v                                                                     
   ---------------------------------------------------------------------     
    TANMATRA (5 subtle data types)                                           
     Shabda -> Sparsha -> Rupa -> Rasa -> Gandha                                
   ---------------------------------------------------------------------     
                                                                               
          v                                                                     
   ---------------------------------------------------------------------     
    MAHABHUTA (5 carrier mediums)                                            
     Akasha -> Vayu -> Agni -> Jala -> Prithvi                                  
   ---------------------------------------------------------------------     
                                                                               
          v                                                                     
   ---------------------------------------------------------------------     
    JNANENDRIYA (5 sense organs)                                             
     Shrotra (Ear) -> Tvak (Skin) -> Chakshu (Eye) ->                          
     Rasana (Tongue) -> Ghrana (Nose)                                         
   ---------------------------------------------------------------------     
                                                                               
          v                                                                     
   ---------------------------------------------------------------------     
    MANAS (मनस्) — Signal Processing                                         
     • Combines 5 sense streams                                              
     • Creates unified perception                                            
     • Filters based on attention                                            
   ---------------------------------------------------------------------     
                                                                               
          v                                                                     
   ---------------------------------------------------------------------     
    BUDDHI (बुद्धि) — Interpretation                                         
     • "What is this?"                                                       
     • "Is this good/bad?"                                                   
     • Decision making                                                       
   ---------------------------------------------------------------------     
                                                                               
          v                                                                     
   ---------------------------------------------------------------------     
    AHAMKARA (अहंकार) — Self-Reference                                       
     • "I see this"                                                          
     • "This is happening to ME"                                             
     • Ego ownership of experience                                           
   ---------------------------------------------------------------------     
                                                                               
          v                                                                     
   ---------------------------------------------------------------------     
    CHITTA (चित्त) — Memory Storage                                          
     • Records as Samskara                                                   
     • Compares with past                                                    
     • Updates Vasana (preferences)                                          
   ---------------------------------------------------------------------     
                                                                               
          v                                                                     
   ---------------------------------------------------------------------     
    PURUSHA / ATMAN (पुरुष/आत्मन्) — Pure Witness                            
     • Witnesses ALL processed experience                                    
     • Does NOT act or react                                                 
     • Pure consciousness observing                                          
   ---------------------------------------------------------------------     
                                                                                
--------------------------------------------------------------------------------
```

---

## 📐 GUNA COMPOSITION OF EACH SENSE

| Sense | S (Sattva) | R (Rajas) | T (Tamas) | Dominant | Reason |
|-------|------------|-----------|-----------|----------|--------|
| **Hearing** | 0.6 | 0.3 | 0.1 | Sattva | Akasha is subtlest |
| **Touch** | 0.3 | 0.5 | 0.2 | Rajas | Vayu is motion |
| **Sight** | 0.5 | 0.4 | 0.1 | Sattva | Agni is light |
| **Taste** | 0.3 | 0.3 | 0.4 | Tamas | Jala needs contact |
| **Smell** | 0.2 | 0.3 | 0.5 | Tamas | Prithvi is densest |

---

## 🔬 VALIDATION: SCIENCE ↔ VEDIC

| Frontend (Science) | Backend (Vedic) | Match? |
|-------------------|-----------------|--------|
| Sound = pressure waves | Shabda = Akasha vibration | ✅ |
| Touch = mechanoreceptors | Sparsha = Vayu contact | ✅ |
| Light = EM radiation | Rupa = Agni carrier | ✅ |
| Taste = chemical (wet) | Rasa = Jala medium | ✅ |
| Smell = particles | Gandha = Prithvi particles | ✅ |
| Smell -> memory link | Gandha -> direct Chitta | ✅ |
| Vision needs light | Chakshu needs Agni | ✅ |
| Taste needs saliva | Rasa needs Jala | ✅ |

---

## 🎯 KEY INSIGHTS

```
--------------------------------------------------------------------------------
                              KEY INSIGHTS                                       
----------------------------------------------------------------------------------�
                                                                                
  1. SENSES ARE INPUT PORTS, NOT THE EXPERIENCE                                 
     • The ear doesn't "hear" — Purusha witnesses hearing                       
     • Organs are hardware, consciousness is the user                           
                                                                                
  2. TANMATRAS ARE RAW DATA, NOT PERCEPTION                                     
     • Shabda exists whether anyone hears it or not                             
     • Rupa exists whether anyone sees it or not                                
     • Maya renders, senses receive, consciousness witnesses                    
                                                                                
  3. ORDER MATTERS: SUBTLE -> GROSS                                              
     • Akasha -> Vayu -> Agni -> Jala -> Prithvi                                   
     • Each contains all previous qualities                                     
     • Prithvi has ALL 5 Tanmatras (most information-dense)                    
                                                                                
  4. GUNAS DETERMINE SENSE QUALITY                                              
     • High Sattva = clear perception (hearing, sight)                          
     • High Rajas = active sensing (touch)                                      
     • High Tamas = gross detection (smell, taste)                              
                                                                                
  5. ANTAHKARANA PROCESSES, ATMAN WITNESSES                                     
     • Manas = Signal processor                                                 
     • Buddhi = Interpreter                                                     
     • Ahamkara = "I" tagger                                                    
     • Chitta = Memory                                                          
     • Atman = Silent witness (never acts)                                      
                                                                                
--------------------------------------------------------------------------------
```

---

> **"यतो वाचो निवर्तन्ते अप्राप्य मनसा सह"**
> "Yato vacho nivartante aprapya manasa saha"
> "From where words return along with the mind, unable to reach."
> — Taittiriya Upanishad 2.9.1

*The senses are doors. What enters is data. What witnesses is Atman.*

