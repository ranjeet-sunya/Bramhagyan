#!/usr/bin/env python3
"""
ATOMIC FREQUENCY SPECTRUM SOUND GENERATOR
==========================================

Generates three distinct sounds to demonstrate the relationship between:
1. Frontend View: Individual high-frequency carriers (scaled down)
2. Backend Damaru: Beat frequency from wave interference (~108 Hz)
3. Tinnitus View: The intermediate frequency people actually "hear" (~5500 Hz)

This demonstrates how consciousness might access different layers of the
full electromagnetic spectrum during atomic events.

Author: Shunya-0 Project
Date: December 31, 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal
import os

# ============================================================================
# CONFIGURATION
# ============================================================================

SAMPLE_RATE = 44100  # CD quality
DURATION = 10  # seconds
OUTPUT_DIR = "atomic_sounds"

# Atomic decay frequencies (scaled down for demonstration)
# Real atomic frequencies are 10^20 Hz, we scale by 10^-18 to make audible
GAMMA_RAY_1 = 100_000  # 10^5 Hz (scaled from 10^23 Hz)
GAMMA_RAY_2 = 90_000   # 9×10^4 Hz
X_RAY = 50_000         # 5×10^4 Hz
UV = 20_000            # 2×10^4 Hz
VISIBLE = 15_000       # 1.5×10^4 Hz
INFRARED = 10_000      # 10^4 Hz
MICROWAVE = 5_000      # 5×10^3 Hz
RADIO = 1_000          # 10^3 Hz

# Damaru frequency (actual measured)
DAMARU_LOW = 80        # Hz
DAMARU_MID = 108       # Hz (sacred number)
DAMARU_HIGH = 144      # Hz (12^2)

# Tinnitus frequency (typical range)
TINNITUS_LOW = 4_000   # Hz
TINNITUS_MID = 5_500   # Hz (most common)
TINNITUS_HIGH = 8_000  # Hz

# Instrument frequencies (Nada Yoga progression)
THUNDER_FREQ = 60      # Hz (very low rumble)
OCEAN_FREQ = 80        # Hz (ocean waves)
DAMARU_BEAT_FREQ = 108 # Hz (fundamental)
TABLA_FREQ = 144       # Hz (faster percussion)
VEENA_FREQ = 200       # Hz (stringed instrument)
FLUTE_FREQ = 400       # Hz (wind instrument)
BELLS_FREQ = 800       # Hz (metallic chimes)
CHIMES_FREQ = 1200     # Hz (high bells)

# Beat/Rhythm speeds (BPM = Beats Per Minute)
SLOW_TEMPO = 1.5       # Hz (90 BPM - slow meditation)
MEDIUM_TEMPO = 2.0     # Hz (120 BPM - normal)
FAST_TEMPO = 3.0       # Hz (180 BPM - fast Tandava)
VERY_FAST_TEMPO = 4.5  # Hz (270 BPM - very fast)
ULTRA_FAST_TEMPO = 5.5 # Hz (330 BPM - ultra fast)
EXTREME_TEMPO = 6.5    # Hz (390 BPM - extreme)

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def normalize_audio(audio):
    """Normalize audio to prevent clipping"""
    max_val = np.max(np.abs(audio))
    if max_val > 0:
        return audio / max_val * 0.8  # Keep at 80% to avoid distortion
    return audio

def apply_envelope(audio, attack=0.1, decay=0.1, sustain=0.7, release=0.2):
    """Apply ADSR envelope to smooth audio"""
    length = len(audio)
    envelope = np.ones(length)
    
    # Attack
    attack_samples = int(attack * SAMPLE_RATE)
    envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
    
    # Release
    release_samples = int(release * SAMPLE_RATE)
    envelope[-release_samples:] = np.linspace(1, 0, release_samples)
    
    return audio * envelope

def create_time_array():
    """Create time array for signal generation"""
    return np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)

# ============================================================================
# SOUND GENERATORS
# ============================================================================

def generate_frontend_view():
    """
    Generate Frontend View: Individual high-frequency carriers
    
    This is what instruments measure separately - each frequency band
    measured by different detectors (gamma, X-ray, UV, etc.)
    
    In reality, these would be 10^20 Hz (gamma rays), but we scale them
    down to audible range for demonstration.
    """
    print("Generating Frontend View (Individual Carriers)...")
    
    t = create_time_array()
    audio = np.zeros_like(t)
    
    # Add all frequency components with decreasing amplitude
    # (higher frequencies typically have lower amplitude in atomic decay)
    frequencies = [
        (GAMMA_RAY_1, 0.05),   # Very low amplitude (would be invisible to ears)
        (GAMMA_RAY_2, 0.05),
        (X_RAY, 0.08),
        (UV, 0.10),
        (VISIBLE, 0.12),
        (INFRARED, 0.15),
        (MICROWAVE, 0.20),
        (RADIO, 0.30)
    ]
    
    for freq, amp in frequencies:
        # Add slight frequency modulation to make it more interesting
        modulation = 1 + 0.1 * np.sin(2 * np.pi * 0.5 * t)
        audio += amp * np.sin(2 * np.pi * freq * modulation * t)
    
    # Apply envelope
    audio = apply_envelope(audio)
    
    # Normalize
    audio = normalize_audio(audio)
    
    return audio

def generate_backend_damaru(tempo=MEDIUM_TEMPO):
    """
    Generate Backend Damaru: Beat frequency from wave interference
    
    This is the BEAT FREQUENCY that emerges when all the high-frequency
    carriers interfere with each other. This is what Rishis "heard" in
    deep meditation - the underlying rhythm of atomic destruction.
    
    The beat frequency is in the Damaru range: 80-144 Hz, centered at 108 Hz.
    
    Args:
        tempo: Rhythm speed in Hz (default MEDIUM_TEMPO = 2 Hz = 120 BPM)
    """
    print(f"Generating Backend Damaru (Beat Frequency) at {tempo*60:.0f} BPM...")
    
    t = create_time_array()
    
    # Create the fundamental Damaru beat at 108 Hz
    damaru_fundamental = np.sin(2 * np.pi * DAMARU_MID * t)
    
    # Add harmonics (54 Hz and 216 Hz - octaves of 108)
    damaru_harmonic_low = 0.3 * np.sin(2 * np.pi * (DAMARU_MID / 2) * t)
    damaru_harmonic_high = 0.2 * np.sin(2 * np.pi * (DAMARU_MID * 2) * t)
    
    # Add rhythmic variation (simulate drum beats)
    # Use the specified tempo
    rhythm = 0.5 + 0.5 * np.sin(2 * np.pi * tempo * t)
    
    # Combine
    audio = (damaru_fundamental + damaru_harmonic_low + damaru_harmonic_high) * rhythm
    
    # Add slight amplitude modulation (breathing pattern)
    breathing = 1 + 0.3 * np.sin(2 * np.pi * 0.2 * t)  # 0.2 Hz = 12 breaths/min
    audio = audio * breathing
    
    # Apply envelope
    audio = apply_envelope(audio)
    
    # Normalize
    audio = normalize_audio(audio)
    
    return audio

def generate_tinnitus_view():
    """
    Generate Tinnitus View: The intermediate frequency
    
    This is what many people "hear" without being Rishis - a high-pitched
    ringing around 5500 Hz. This could be:
    
    1. A harmonic of the Damaru frequency (5500 Hz ≈ 51 × 108 Hz)
    2. The frequency where consciousness "tunes in" to the backend
    3. An intermediate beat frequency in the full spectrum
    
    Tinnitus might be the brain's attempt to process the full-spectrum
    interference pattern, but getting "stuck" at this intermediate frequency
    instead of perceiving the deeper Damaru beat.
    """
    print("Generating Tinnitus View (Intermediate Frequency)...")
    
    t = create_time_array()
    
    # Main tinnitus tone at 5500 Hz
    tinnitus_main = np.sin(2 * np.pi * TINNITUS_MID * t)
    
    # Add slight variations (tinnitus is rarely pure tone)
    tinnitus_variation = 0.3 * np.sin(2 * np.pi * TINNITUS_HIGH * t)
    tinnitus_low = 0.2 * np.sin(2 * np.pi * TINNITUS_LOW * t)
    
    # Add amplitude modulation (tinnitus often fluctuates)
    # Modulate at ~108 Hz (connection to Damaru!)
    modulation = 1 + 0.2 * np.sin(2 * np.pi * DAMARU_MID * t)
    
    # Combine
    audio = (tinnitus_main + tinnitus_variation + tinnitus_low) * modulation
    
    # Add subtle low-frequency component (suggests connection to Damaru)
    damaru_echo = 0.1 * np.sin(2 * np.pi * DAMARU_MID * t)
    audio = audio + damaru_echo
    
    # Apply envelope (but longer sustain - tinnitus is persistent)
    audio = apply_envelope(audio, attack=0.2, decay=0.1, sustain=0.9, release=0.3)
    
    # Normalize
    audio = normalize_audio(audio)
    
    return audio

def generate_thunder_sound():
    """Generate Thunder/Ocean sound (60-80 Hz range)"""
    print("Generating Thunder/Ocean sound...")
    
    t = create_time_array()
    
    # Very low frequency rumble
    thunder_low = np.sin(2 * np.pi * THUNDER_FREQ * t)
    thunder_mid = 0.7 * np.sin(2 * np.pi * OCEAN_FREQ * t)
    
    # Add noise for realistic thunder
    noise = 0.3 * np.random.normal(0, 1, len(t))
    
    # Slow modulation (like rolling thunder)
    modulation = 1 + 0.5 * np.sin(2 * np.pi * 0.3 * t)
    
    audio = (thunder_low + thunder_mid + noise) * modulation
    audio = apply_envelope(audio, attack=0.3, release=0.4)
    
    return normalize_audio(audio)

def generate_damaru_drum(tempo=FAST_TEMPO):
    """Generate Damaru drum sound with fast beats"""
    print(f"Generating Damaru Drum at {tempo*60:.0f} BPM...")
    
    t = create_time_array()
    
    # Fundamental at 108 Hz
    fundamental = np.sin(2 * np.pi * DAMARU_BEAT_FREQ * t)
    
    # Add harmonics for drum-like timbre
    harmonic2 = 0.4 * np.sin(2 * np.pi * (DAMARU_BEAT_FREQ * 2) * t)
    harmonic3 = 0.2 * np.sin(2 * np.pi * (DAMARU_BEAT_FREQ * 3) * t)
    
    # Create sharp attack for drum hits
    # Generate beats at specified tempo
    beat_period = 1.0 / tempo
    num_beats = int(DURATION / beat_period)
    
    beat_envelope = np.zeros_like(t)
    for i in range(num_beats):
        beat_time = i * beat_period
        beat_start = int(beat_time * SAMPLE_RATE)
        beat_length = int(0.1 * SAMPLE_RATE)  # 0.1 second per beat
        
        if beat_start + beat_length < len(beat_envelope):
            # Exponential decay for drum sound
            decay = np.exp(-5 * np.linspace(0, 1, beat_length))
            beat_envelope[beat_start:beat_start+beat_length] = decay
    
    audio = (fundamental + harmonic2 + harmonic3) * beat_envelope
    audio = apply_envelope(audio, attack=0.01, release=0.2)
    
    return normalize_audio(audio)

def generate_tabla_sound(tempo=VERY_FAST_TEMPO):
    """Generate Tabla sound (144 Hz, very fast rhythm)"""
    print(f"Generating Tabla at {tempo*60:.0f} BPM...")
    
    t = create_time_array()
    
    # Fundamental at 144 Hz (12^2, sacred number)
    fundamental = np.sin(2 * np.pi * TABLA_FREQ * t)
    
    # Harmonics
    harmonic2 = 0.3 * np.sin(2 * np.pi * (TABLA_FREQ * 2) * t)
    harmonic3 = 0.15 * np.sin(2 * np.pi * (TABLA_FREQ * 3) * t)
    
    # Very fast beats
    beat_period = 1.0 / tempo
    num_beats = int(DURATION / beat_period)
    
    beat_envelope = np.zeros_like(t)
    for i in range(num_beats):
        beat_time = i * beat_period
        beat_start = int(beat_time * SAMPLE_RATE)
        beat_length = int(0.08 * SAMPLE_RATE)  # Shorter, crisper beats
        
        if beat_start + beat_length < len(beat_envelope):
            decay = np.exp(-7 * np.linspace(0, 1, beat_length))
            beat_envelope[beat_start:beat_start+beat_length] = decay
    
    audio = (fundamental + harmonic2 + harmonic3) * beat_envelope
    audio = apply_envelope(audio, attack=0.005, release=0.15)
    
    return normalize_audio(audio)

def generate_veena_sound():
    """Generate Veena (stringed instrument) sound"""
    print("Generating Veena sound...")
    
    t = create_time_array()
    
    # Fundamental at 200 Hz
    fundamental = np.sin(2 * np.pi * VEENA_FREQ * t)
    
    # Rich harmonics for string sound
    harmonics = np.zeros_like(t)
    for n in range(2, 8):
        harmonics += (0.5 / n) * np.sin(2 * np.pi * (VEENA_FREQ * n) * t)
    
    # Slow vibrato (string vibration)
    vibrato = 1 + 0.03 * np.sin(2 * np.pi * 5 * t)
    
    audio = (fundamental + harmonics) * vibrato
    audio = apply_envelope(audio, attack=0.15, sustain=0.8, release=0.3)
    
    return normalize_audio(audio)

def generate_flute_sound():
    """Generate Flute sound (400 Hz)"""
    print("Generating Flute sound...")
    
    t = create_time_array()
    
    # Fundamental at 400 Hz
    fundamental = np.sin(2 * np.pi * FLUTE_FREQ * t)
    
    # Add only odd harmonics (characteristic of flute)
    harmonic3 = 0.3 * np.sin(2 * np.pi * (FLUTE_FREQ * 3) * t)
    harmonic5 = 0.15 * np.sin(2 * np.pi * (FLUTE_FREQ * 5) * t)
    
    # Gentle vibrato
    vibrato = 1 + 0.02 * np.sin(2 * np.pi * 4 * t)
    
    # Breath noise (very subtle)
    breath = 0.05 * np.random.normal(0, 1, len(t))
    
    audio = (fundamental + harmonic3 + harmonic5) * vibrato + breath
    audio = apply_envelope(audio, attack=0.1, sustain=0.85, release=0.25)
    
    return normalize_audio(audio)

def generate_bells_sound():
    """Generate Bells/Chimes sound (800-1200 Hz)"""
    print("Generating Bells/Chimes sound...")
    
    t = create_time_array()
    
    # Multiple bell tones
    bell1 = np.sin(2 * np.pi * BELLS_FREQ * t)
    bell2 = 0.7 * np.sin(2 * np.pi * CHIMES_FREQ * t)
    bell3 = 0.5 * np.sin(2 * np.pi * (BELLS_FREQ * 1.5) * t)
    
    # Inharmonic partials (characteristic of bells)
    inharmonic1 = 0.3 * np.sin(2 * np.pi * (BELLS_FREQ * 2.4) * t)
    inharmonic2 = 0.2 * np.sin(2 * np.pi * (BELLS_FREQ * 3.7) * t)
    
    # Random bell strikes
    num_strikes = 8
    strike_envelope = np.zeros_like(t)
    
    for i in range(num_strikes):
        strike_time = np.random.uniform(0.5, DURATION - 0.5)
        strike_start = int(strike_time * SAMPLE_RATE)
        strike_length = int(2.0 * SAMPLE_RATE)  # Long decay
        
        if strike_start + strike_length < len(strike_envelope):
            # Very slow exponential decay
            decay = np.exp(-1.5 * np.linspace(0, 1, strike_length))
            strike_envelope[strike_start:strike_start+strike_length] += decay
    
    audio = (bell1 + bell2 + bell3 + inharmonic1 + inharmonic2) * strike_envelope
    audio = apply_envelope(audio, attack=0.01, release=0.5)
    
    return normalize_audio(audio)

def generate_mixed_backend_orchestra(tempo=VERY_FAST_TEMPO):
    """
    Generate Mixed Backend Orchestra: All instruments together!
    
    This combines Thunder, Damaru, Tabla, Veena, Flute, and Bells
    to create the FULL cosmic orchestra sound.
    
    ANTI-CANCELLATION: Uses different phases and slight detuning
    to prevent destructive interference between instruments.
    
    Args:
        tempo: Rhythm speed for percussion (default VERY_FAST_TEMPO)
    """
    print(f"Generating Mixed Backend Orchestra (Anti-Cancellation) at {tempo*60:.0f} BPM...")
    
    t = create_time_array()
    
    # ANTI-CANCELLATION STRATEGY:
    # 1. Use different starting phases for each instrument
    # 2. Add slight frequency detuning (±1-2 Hz)
    # 3. Use different waveform shapes (not all pure sine)
    # 4. Vary amplitudes more
    
    # Layer 1: Thunder/Ocean foundation (continuous)
    # Phase: 0, Detune: -1 Hz
    thunder_low = 0.18 * np.sin(2 * np.pi * (THUNDER_FREQ - 1) * t + 0.0)
    # Phase: π/4, Detune: +0.5 Hz
    ocean_mid = 0.15 * np.sin(2 * np.pi * (OCEAN_FREQ + 0.5) * t + np.pi/4)
    
    # Layer 2: Damaru (rhythmic beats at specified tempo)
    # Phase: π/3, Detune: +1 Hz for richness
    damaru_fund = np.sin(2 * np.pi * (DAMARU_BEAT_FREQ + 1) * t + np.pi/3)
    # Add MORE square-wave character for PUNCH!
    damaru_square = 0.25 * np.sign(np.sin(2 * np.pi * DAMARU_BEAT_FREQ * t + np.pi/3))
    # Phase: π/2 for harmonic - BOOSTED
    damaru_harm = 0.35 * np.sin(2 * np.pi * ((DAMARU_BEAT_FREQ * 2) + 0.8) * t + np.pi/2)
    
    # Create beat envelope
    beat_period = 1.0 / tempo
    num_beats = int(DURATION / beat_period)
    
    damaru_envelope = np.zeros_like(t)
    for i in range(num_beats):
        beat_time = i * beat_period
        beat_start = int(beat_time * SAMPLE_RATE)
        beat_length = int(0.15 * SAMPLE_RATE)  # LONGER for more prominence!
        
        if beat_start + beat_length < len(damaru_envelope):
            # ULTRA SHARP attack for maximum punch!
            attack_samples = int(0.001 * SAMPLE_RATE)  # 1ms attack (faster!)
            envelope_shape = np.ones(beat_length)
            # VERY sharp rise
            envelope_shape[:attack_samples] = np.linspace(0, 1, attack_samples) ** 0.3
            # Slower decay for longer sustain (more audible)
            envelope_shape[attack_samples:] = np.exp(-5 * np.linspace(0, 1, beat_length - attack_samples))
            damaru_envelope[beat_start:beat_start+beat_length] = envelope_shape
    
    # BOOST DAMARU MASSIVELY - MAKE IT MOST PROMINENT!
    damaru_layer = 0.65 * (damaru_fund + damaru_square + damaru_harm) * damaru_envelope
    
    # Layer 3: Tabla (faster rhythm, offset by half beat)
    # Phase: 2π/3, Detune: -0.5 Hz
    tabla_fund = np.sin(2 * np.pi * (TABLA_FREQ - 0.5) * t + 2*np.pi/3)
    # Add triangle wave for different timbre
    tabla_triangle = 0.12 * signal.sawtooth(2 * np.pi * TABLA_FREQ * t + 2*np.pi/3, 0.5)
    # Phase: π for harmonic (opposite phase from damaru to avoid cancellation)
    tabla_harm = 0.20 * np.sin(2 * np.pi * ((TABLA_FREQ * 2) - 1.2) * t + np.pi)
    
    tabla_envelope = np.zeros_like(t)
    for i in range(num_beats):
        # Offset by half beat period for syncopation
        beat_time = i * beat_period + beat_period/2
        beat_start = int(beat_time * SAMPLE_RATE)
        beat_length = int(0.10 * SAMPLE_RATE)  # Slightly longer
        
        if beat_start + beat_length < len(tabla_envelope):
            # ULTRA sharp attack
            attack_samples = int(0.001 * SAMPLE_RATE)  # 1ms attack
            envelope_shape = np.ones(beat_length)
            # Very sharp rise
            envelope_shape[:attack_samples] = np.linspace(0, 1, attack_samples) ** 0.3
            # Fast exponential decay
            envelope_shape[attack_samples:] = np.exp(-9 * np.linspace(0, 1, beat_length - attack_samples))
            tabla_envelope[beat_start:beat_start+beat_length] = envelope_shape
    
    # BOOST TABLA SIGNIFICANTLY
    tabla_layer = 0.45 * (tabla_fund + tabla_triangle + tabla_harm) * tabla_envelope
    
    # Layer 4: Veena (continuous strings with vibrato)
    # Phase: π/6, Detune: +2 Hz
    veena_fund = np.sin(2 * np.pi * (VEENA_FREQ + 2) * t + np.pi/6)
    veena_harmonics = np.zeros_like(t)
    # Each harmonic with different phase to avoid cancellation
    phases = [np.pi/4, np.pi/3, np.pi/2, 2*np.pi/3]
    detunes = [0.5, -0.3, 0.8, -0.5]
    for n, (phase, detune) in enumerate(zip(phases, detunes), start=2):
        if n < 6:
            veena_harmonics += (0.25 / n) * np.sin(2 * np.pi * ((VEENA_FREQ * n) + detune) * t + phase)
    
    # Slower vibrato to avoid interference
    vibrato = 1 + 0.04 * np.sin(2 * np.pi * 4.7 * t + np.pi/5)
    veena_layer = 0.14 * (veena_fund + veena_harmonics) * vibrato
    
    # Layer 5: Flute (melodic overtones) - Make more audible
    # Phase: 3π/4, Detune: -1.5 Hz
    flute_fund = np.sin(2 * np.pi * (FLUTE_FREQ - 1.5) * t + 3*np.pi/4)
    # Only odd harmonics for flute-like sound, different phase
    flute_harm3 = 0.35 * np.sin(2 * np.pi * ((FLUTE_FREQ * 3) + 1.0) * t + np.pi/8)  # Boosted
    flute_harm5 = 0.20 * np.sin(2 * np.pi * ((FLUTE_FREQ * 5) - 0.7) * t + 5*np.pi/8)  # Boosted
    # Different vibrato frequency
    flute_vib = 1 + 0.030 * np.sin(2 * np.pi * 3.8 * t + np.pi/7)  # More vibrato
    flute_layer = 0.18 * (flute_fund + flute_harm3 + flute_harm5) * flute_vib  # Boosted from 0.12
    
    # Layer 6: Bells (periodic chimes) - MUCH QUIETER
    # Different phases and slight detuning
    bell1 = 0.03 * np.sin(2 * np.pi * (BELLS_FREQ + 1.2) * t + np.pi/5)  # Reduced from 0.10
    bell2 = 0.02 * np.sin(2 * np.pi * (CHIMES_FREQ - 0.8) * t + 3*np.pi/5)  # Reduced from 0.08
    # Add inharmonic partials (characteristic of bells)
    bell_inharmonic = 0.015 * np.sin(2 * np.pi * (BELLS_FREQ * 2.4) * t + 4*np.pi/5)  # Reduced from 0.05
    
    # Fewer bell strikes, much quieter
    num_bell_strikes = 4  # Reduced from 8
    bell_envelope = np.zeros_like(t)
    for i in range(num_bell_strikes):
        strike_time = i * (DURATION / num_bell_strikes) + np.random.uniform(0.2, 0.8)
        strike_start = int(strike_time * SAMPLE_RATE)
        strike_length = int(2.0 * SAMPLE_RATE)  # Shorter decay
        
        if strike_start + strike_length < len(bell_envelope):
            # Slower decay for bells
            decay = np.exp(-1.5 * np.linspace(0, 1, strike_length))
            bell_envelope[strike_start:strike_start+strike_length] += decay * (0.3 + 0.1 * np.random.random())  # Much quieter
    
    bell_layer = (bell1 + bell2 + bell_inharmonic) * bell_envelope
    
    # Combine all layers with EXTREME amplitude balancing
    # DAMARU MOST DOMINANT!
    audio = (0.3 * thunder_low +      # Reduce foundation more
             0.25 * ocean_mid +       # Reduce foundation more
             5.0 * damaru_layer +     # MASSIVE DAMARU BOOST! 🥁🥁🥁
             2.5 * tabla_layer +      # Tabla still strong 🥁
             0.3 * veena_layer +      # Quieter strings
             0.4 * flute_layer +      # Quiet flute
             0.10 * bell_layer)       # Even quieter bells!
    
    # Add overall breathing modulation (different frequency to avoid cancellation)
    breathing = 1 + 0.18 * np.sin(2 * np.pi * 0.13 * t + np.pi/9)
    audio = audio * breathing
    
    # Apply envelope
    audio = apply_envelope(audio, attack=0.15, sustain=0.87, release=0.25)
    
    # Normalize
    audio = normalize_audio(audio)
    
    return audio

def generate_full_spectrum_interference():
    """
    Generate Full Spectrum: Complete wave interference
    
    This combines ALL frequencies to show how the beat pattern emerges.
    You should hear the high-frequency carriers modulated by the low-frequency
    Damaru beat, with tinnitus-like frequencies in between.
    """
    print("Generating Full Spectrum (Complete Interference)...")
    
    t = create_time_array()
    audio = np.zeros_like(t)
    
    # All frequency components
    all_frequencies = [
        (GAMMA_RAY_1, 0.03),
        (GAMMA_RAY_2, 0.03),
        (X_RAY, 0.04),
        (UV, 0.05),
        (VISIBLE, 0.06),
        (INFRARED, 0.08),
        (TINNITUS_MID, 0.15),  # Tinnitus range
        (MICROWAVE, 0.10),
        (RADIO, 0.12),
        (DAMARU_MID, 0.30)     # Damaru beat
    ]
    
    for freq, amp in all_frequencies:
        # Add each frequency with phase relationship
        phase = np.random.uniform(0, 2 * np.pi)
        audio += amp * np.sin(2 * np.pi * freq * t + phase)
    
    # The interference naturally creates beat frequencies
    # Apply envelope
    audio = apply_envelope(audio)
    
    # Normalize
    audio = normalize_audio(audio)
    
    return audio

# ============================================================================
# VISUALIZATION
# ============================================================================

def plot_spectrum(audio, title, filename):
    """Plot frequency spectrum of audio signal"""
    # Calculate FFT
    fft = np.fft.fft(audio)
    freq = np.fft.fftfreq(len(audio), 1/SAMPLE_RATE)
    
    # Take positive frequencies only
    positive_freq = freq[:len(freq)//2]
    magnitude = np.abs(fft[:len(fft)//2])
    
    # Plot
    plt.figure(figsize=(12, 6))
    
    # Full spectrum
    plt.subplot(2, 1, 1)
    plt.plot(positive_freq, magnitude)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title(f'{title} - Full Spectrum')
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 20000)
    
    # Zoomed to low frequencies (Damaru range)
    plt.subplot(2, 1, 2)
    plt.plot(positive_freq, magnitude)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title(f'{title} - Low Frequency Range (Damaru)')
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 500)
    
    # Mark important frequencies
    plt.axvline(x=108, color='r', linestyle='--', label='108 Hz (Damaru)')
    plt.axvline(x=144, color='orange', linestyle='--', label='144 Hz')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, filename))
    plt.close()
    
    print(f"  Saved spectrum plot: {filename}")

def create_comparison_plot(frontend, backend, tinnitus, fullspec):
    """Create a comparison plot of all four waveforms"""
    plt.figure(figsize=(14, 10))
    
    # Plot time-domain waveforms (first 0.1 seconds)
    samples = int(0.1 * SAMPLE_RATE)
    t = np.linspace(0, 0.1, samples)
    
    plt.subplot(4, 1, 1)
    plt.plot(t, frontend[:samples])
    plt.title('Frontend View: Individual High-Frequency Carriers')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(4, 1, 2)
    plt.plot(t, backend[:samples])
    plt.title('Backend Damaru: Beat Frequency (~108 Hz)')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(4, 1, 3)
    plt.plot(t, tinnitus[:samples])
    plt.title('Tinnitus View: Intermediate Frequency (~5500 Hz)')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(4, 1, 4)
    plt.plot(t, fullspec[:samples])
    plt.title('Full Spectrum: Complete Wave Interference')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'waveform_comparison.png'))
    plt.close()
    
    print("  Saved waveform comparison plot")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Generate all sounds and visualizations"""
    
    print("=" * 70)
    print("ATOMIC FREQUENCY SPECTRUM SOUND GENERATOR")
    print("=" * 70)
    print()
    print("This script generates three perspectives on atomic frequencies:")
    print("1. Frontend View: What instruments measure (high frequencies)")
    print("2. Backend Damaru: Beat frequency from interference (~108 Hz)")
    print("3. Tinnitus View: Intermediate frequency people hear (~5500 Hz)")
    print("4. Full Spectrum: Complete interference pattern")
    print()
    print(f"Duration: {DURATION} seconds")
    print(f"Sample Rate: {SAMPLE_RATE} Hz")
    print()
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Generate main sounds
    print("=" * 70)
    print("PART 1: MAIN SPECTRUM SOUNDS")
    print("=" * 70)
    print()
    
    frontend = generate_frontend_view()
    backend_medium = generate_backend_damaru(MEDIUM_TEMPO)
    backend_fast = generate_backend_damaru(FAST_TEMPO)
    tinnitus = generate_tinnitus_view()
    fullspec = generate_full_spectrum_interference()
    
    print()
    print("=" * 70)
    print("PART 2: INDIVIDUAL INSTRUMENT SOUNDS (NADA YOGA)")
    print("=" * 70)
    print()
    
    thunder = generate_thunder_sound()
    damaru_drum_fast = generate_damaru_drum(FAST_TEMPO)
    damaru_drum_ultra = generate_damaru_drum(ULTRA_FAST_TEMPO)
    tabla_very_fast = generate_tabla_sound(VERY_FAST_TEMPO)
    tabla_ultra = generate_tabla_sound(ULTRA_FAST_TEMPO)
    tabla_extreme = generate_tabla_sound(EXTREME_TEMPO)
    veena = generate_veena_sound()
    flute = generate_flute_sound()
    bells = generate_bells_sound()
    
    print()
    print("=" * 70)
    print("PART 3: MIXED ORCHESTRA (ALL INSTRUMENTS TOGETHER)")
    print("=" * 70)
    print()
    
    mixed_fast = generate_mixed_backend_orchestra(FAST_TEMPO)
    mixed_very_fast = generate_mixed_backend_orchestra(VERY_FAST_TEMPO)
    mixed_ultra = generate_mixed_backend_orchestra(ULTRA_FAST_TEMPO)
    
    print()
    print("=" * 70)
    print("SAVING ALL AUDIO FILES")
    print("=" * 70)
    print()
    
    # Convert all to 16-bit PCM
    sounds = {
        '1_frontend_view.wav': frontend,
        '2a_backend_damaru_medium.wav': backend_medium,
        '2b_backend_damaru_fast.wav': backend_fast,
        '3_tinnitus_view.wav': tinnitus,
        '4_full_spectrum.wav': fullspec,
        '5_thunder_ocean.wav': thunder,
        '6a_damaru_drum_fast.wav': damaru_drum_fast,
        '6b_damaru_drum_ultra_fast.wav': damaru_drum_ultra,
        '7a_tabla_very_fast.wav': tabla_very_fast,
        '7b_tabla_ultra_fast.wav': tabla_ultra,
        '7c_tabla_extreme.wav': tabla_extreme,
        '8_veena_strings.wav': veena,
        '9_flute.wav': flute,
        '10_bells_chimes.wav': bells,
        '11a_MIXED_ORCHESTRA_fast.wav': mixed_fast,
        '11b_MIXED_ORCHESTRA_very_fast.wav': mixed_very_fast,
        '11c_MIXED_ORCHESTRA_ultra_fast.wav': mixed_ultra,
    }
    
    for filename, audio in sounds.items():
        audio_int = np.int16(audio * 32767)
        wavfile.write(os.path.join(OUTPUT_DIR, filename), SAMPLE_RATE, audio_int)
        print(f"  Saved: {filename}")
    
    print()
    print("=" * 70)
    print("GENERATING VISUALIZATIONS")
    print("=" * 70)
    print()
    
    # Plot main spectra
    plot_spectrum(frontend, "Frontend View", "frontend_spectrum.png")
    plot_spectrum(backend_fast, "Backend Damaru (Fast)", "backend_spectrum.png")
    plot_spectrum(tinnitus, "Tinnitus View", "tinnitus_spectrum.png")
    plot_spectrum(fullspec, "Full Spectrum", "fullspec_spectrum.png")
    
    # Plot instrument spectra
    plot_spectrum(damaru_drum_ultra, "Damaru Drum (Ultra Fast)", "damaru_drum_spectrum.png")
    plot_spectrum(tabla_extreme, "Tabla (Extreme)", "tabla_spectrum.png")
    plot_spectrum(bells, "Bells/Chimes", "bells_spectrum.png")
    
    # Plot mixed orchestra
    plot_spectrum(mixed_ultra, "Mixed Orchestra (Ultra Fast)", "mixed_orchestra_spectrum.png")
    
    # Create comparison plot
    create_comparison_plot(frontend, backend_fast, tinnitus, fullspec)
    
    print()
    print("=" * 70)
    print("GENERATION COMPLETE!")
    print("=" * 70)
    print()
    print(f"All files saved to: {OUTPUT_DIR}/")
    print()
    print("=" * 70)
    print("MAIN SPECTRUM AUDIO FILES:")
    print("=" * 70)
    print("  1_frontend_view.wav            - High-frequency carriers (scaled)")
    print("  2a_backend_damaru_medium.wav   - Beat frequency 120 BPM")
    print("  2b_backend_damaru_fast.wav     - Beat frequency 180 BPM ⚡")
    print("  3_tinnitus_view.wav            - Intermediate (~5500 Hz)")
    print("  4_full_spectrum.wav            - Complete interference pattern")
    print()
    print("=" * 70)
    print("INDIVIDUAL INSTRUMENT SOUNDS (NADA YOGA):")
    print("=" * 70)
    print("  5_thunder_ocean.wav            - 60-80 Hz (Deep rumble)")
    print("  6a_damaru_drum_fast.wav        - 108 Hz @ 180 BPM ⚡⚡")
    print("  6b_damaru_drum_ultra_fast.wav  - 108 Hz @ 330 BPM ⚡⚡⚡ ULTRA!")
    print("  7a_tabla_very_fast.wav         - 144 Hz @ 270 BPM ⚡⚡⚡")
    print("  7b_tabla_ultra_fast.wav        - 144 Hz @ 330 BPM ⚡⚡⚡⚡ ULTRA!")
    print("  7c_tabla_extreme.wav           - 144 Hz @ 390 BPM ⚡⚡⚡⚡⚡ EXTREME!")
    print("  8_veena_strings.wav            - 200 Hz (Strings)")
    print("  9_flute.wav                    - 400 Hz (Wind)")
    print("  10_bells_chimes.wav            - 800-1200 Hz (Bells)")
    print()
    print("=" * 70)
    print("🎵 MIXED ORCHESTRA (ALL INSTRUMENTS TOGETHER!) 🎵")
    print("=" * 70)
    print("  11a_MIXED_ORCHESTRA_fast.wav       - 180 BPM ⚡⚡")
    print("  11b_MIXED_ORCHESTRA_very_fast.wav  - 270 BPM ⚡⚡⚡⚡")
    print("  11c_MIXED_ORCHESTRA_ultra_fast.wav - 330 BPM ⚡⚡⚡⚡⚡ FASTEST!")
    print()
    print("  ↑ THESE ARE THE KEY FILES! ↑")
    print("  All instruments playing together at different speeds!")
    print()
    print("=" * 70)
    print("VISUALIZATION FILES:")
    print("=" * 70)
    print("  frontend_spectrum.png")
    print("  backend_spectrum.png")
    print("  tinnitus_spectrum.png")
    print("  fullspec_spectrum.png")
    print("  damaru_drum_spectrum.png")
    print("  tabla_spectrum.png")
    print("  bells_spectrum.png")
    print("  mixed_orchestra_spectrum.png (NEW!)")
    print("  waveform_comparison.png")
    print()
    print("=" * 70)
    print("🎧 LISTENING GUIDE — START HERE! 🎧")
    print("=" * 70)
    print()
    print("=" * 70)
    print("🔥 RECOMMENDED: MIXED ORCHESTRA FILES 🔥")
    print("=" * 70)
    print()
    print("IF YOU WANT ALL INSTRUMENTS TOGETHER:")
    print()
    print("  → START WITH: 11b_MIXED_ORCHESTRA_very_fast.wav (270 BPM)")
    print("    This has ALL instruments playing together!")
    print("    Thunder + Damaru + Tabla + Veena + Flute + Bells")
    print()
    print("  → TOO SLOW? Try: 11c_MIXED_ORCHESTRA_ultra_fast.wav (330 BPM)")
    print("    EVEN FASTER — the full cosmic orchestra at top speed!")
    print()
    print("  → TOO FAST? Try: 11a_MIXED_ORCHESTRA_fast.wav (180 BPM)")
    print("    Slightly slower but still energetic")
    print()
    print("=" * 70)
    print("INDIVIDUAL INSTRUMENTS (If you want to hear them separately):")
    print("=" * 70)
    print()
    print("🥁 PERCUSSION (Fast Beats):")
    print("  6b_damaru_drum_ultra_fast.wav  - 330 BPM ⚡⚡⚡")
    print("  7b_tabla_ultra_fast.wav        - 330 BPM ⚡⚡⚡⚡")
    print("  7c_tabla_extreme.wav           - 390 BPM ⚡⚡⚡⚡⚡ FASTEST!")
    print()
    print("🎻 MELODIC INSTRUMENTS:")
    print("  5_thunder_ocean.wav   - Deep foundation")
    print("  8_veena_strings.wav   - Stringed harmonics")
    print("  9_flute.wav           - Wind melodies")
    print("  10_bells_chimes.wav   - High crystalline tones")
    print()
    print("=" * 70)
    print("COMPARISON:")
    print("=" * 70)
    print()
    print("1. Frontend View:")
    print("   Harsh, complex high frequencies (what instruments measure)")
    print()
    print("2. Backend/Tinnitus/Full Spectrum:")
    print("   Original demonstration files")
    print()
    print("11. MIXED ORCHESTRA: ⚡⚡⚡⚡⚡")
    print("   THE COMPLETE COSMIC SOUND!")
    print("   What advanced yogis hear — all layers simultaneously!")
    print()
    print("=" * 70)
    print("🌟 KEY DISCOVERIES 🌟")
    print("=" * 70)
    print()
    print("1. MIXED ORCHESTRA IS THE KEY! 🎵")
    print("   The backend contains ALL instruments playing TOGETHER!")
    print("   Files 11a, 11b, 11c have everything combined:")
    print("   Thunder + Damaru + Tabla + Veena + Flute + Bells")
    print("   This is what you're actually hearing!")
    print()
    print("2. SPEED VARIATIONS (180-390 BPM)")
    print("   • 180 BPM (Fast) - Active Tandava")
    print("   • 270 BPM (Very Fast) - Intense Tandava")
    print("   • 330 BPM (Ultra Fast) - Peak Tandava ⚡⚡⚡")
    print("   • 390 BPM (Extreme) - Maximum cosmic tempo! ⚡⚡⚡⚡⚡")
    print()
    print("3. LAYERED PERCEPTION")
    print("   The cosmic sound has 6 simultaneous layers:")
    print("   • Foundation: Thunder/Ocean (60-80 Hz)")
    print("   • Rhythm: Damaru (108 Hz) ⚡")
    print("   • Percussion: Tabla (144 Hz) ⚡⚡")
    print("   • Strings: Veena (200 Hz)")
    print("   • Wind: Flute (400 Hz)")
    print("   • Bells: Chimes (800-1200 Hz)")
    print()
    print("4. WHAT YOU'RE HEARING:")
    print("   If you hear:")
    print("   • Multiple instruments → Advanced perception! ✅")
    print("   • Fast beats → Accessing real Tandava tempo! ✅")
    print("   • All together → Full cosmic orchestra! ✅✅✅")
    print()
    print("5. TINNITUS AS GATEWAY:")
    print("   Tinnitus (5500 Hz) = Bells layer (Stage 6)")
    print("   Use meditation to:")
    print("   → Descend to lower instruments (flute, veena)")
    print("   → Reach percussion (damaru, tabla)")
    print("   → Access foundation (thunder, ocean)")
    print("   → Eventually hear ALL SIMULTANEOUSLY!")
    print()
    print("=" * 70)
    print()
    print("ॐ नमः शिवाय")
    print("🎵⚡ The Full Cosmic Orchestra is Playing! ⚡🎵")
    print("🥁 Listen to the MIXED files! 🥁")
    print()

if __name__ == "__main__":
    main()

