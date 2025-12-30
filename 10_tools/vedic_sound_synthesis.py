#!/usr/bin/env python3
"""
🕉️ वैदिक-ध्वनि-संश्लेषण — Vedic Sound Synthesis
================================================

A Python implementation for synthesizing pure Sanskrit phonemes
based on Vedic pronunciation principles.

> "नादो ब्रह्म, नादो विष्णुः"
> "Nado Brahma, Nado Vishnuh"
> "Sound is Brahma, Sound is Vishnu"

Usage:
    python vedic_sound_synthesis.py

Requirements:
    pip install numpy scipy matplotlib

Author: Shunya-0 Project
License: Open for Dharmic use
"""

import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, filtfilt
import os

# =============================================================================
# CONSTANTS — Based on Vedic Sound Science
# =============================================================================

# OM Base Frequency (Earth's Year Frequency)
OM_BASE_FREQ = 136.1  # Hz

# Sample Rate for audio
SAMPLE_RATE = 44100  # Hz

# Base duration for 1 Matra (short vowel unit)
MATRA_DURATION = 0.25  # seconds

# =============================================================================
# VOWEL FREQUENCY RATIOS
# Relative to OM base frequency, based on articulatory phonetics
# =============================================================================

VOWEL_DATA = {
    # Hrasva (Short) Vowels - 1 Matra
    'अ': {'ratio': 1.0, 'matras': 1, 'name': 'a', 'position': 'throat'},
    'इ': {'ratio': 1.5, 'matras': 1, 'name': 'i', 'position': 'palate'},
    'उ': {'ratio': 0.8, 'matras': 1, 'name': 'u', 'position': 'lips'},
    'ऋ': {'ratio': 1.2, 'matras': 1, 'name': 'ri', 'position': 'retroflex'},
    
    # Dirgha (Long) Vowels - 2 Matras
    'आ': {'ratio': 1.0, 'matras': 2, 'name': 'aa', 'position': 'throat'},
    'ई': {'ratio': 1.5, 'matras': 2, 'name': 'ii', 'position': 'palate'},
    'ऊ': {'ratio': 0.8, 'matras': 2, 'name': 'uu', 'position': 'lips'},
    
    # Sandhyakshara (Compound) Vowels
    'ए': {'ratio': 1.3, 'matras': 2, 'name': 'e', 'position': 'palate-throat'},
    'ऐ': {'ratio': 1.4, 'matras': 2, 'name': 'ai', 'position': 'palate-throat'},
    'ओ': {'ratio': 0.9, 'matras': 2, 'name': 'o', 'position': 'lips-throat'},
    'औ': {'ratio': 0.85, 'matras': 2, 'name': 'au', 'position': 'lips-throat'},
    
    # Anusvara and Visarga
    'अं': {'ratio': 1.1, 'matras': 1, 'name': 'am', 'position': 'nasal'},
    'अः': {'ratio': 1.0, 'matras': 1, 'name': 'ah', 'position': 'aspirate'},
}

# =============================================================================
# CONSONANT DATA (Sparsha Varnas - Stop Consonants)
# =============================================================================

CONSONANT_DATA = {
    # Kanthya Varga (Guttural/Throat)
    'क': {'base': 0.5, 'voiced': False, 'aspirated': False, 'nasal': False, 'varga': 'kanthya'},
    'ख': {'base': 0.5, 'voiced': False, 'aspirated': True, 'nasal': False, 'varga': 'kanthya'},
    'ग': {'base': 0.5, 'voiced': True, 'aspirated': False, 'nasal': False, 'varga': 'kanthya'},
    'घ': {'base': 0.5, 'voiced': True, 'aspirated': True, 'nasal': False, 'varga': 'kanthya'},
    'ङ': {'base': 0.5, 'voiced': True, 'aspirated': False, 'nasal': True, 'varga': 'kanthya'},
    
    # Talavya Varga (Palatal)
    'च': {'base': 0.8, 'voiced': False, 'aspirated': False, 'nasal': False, 'varga': 'talavya'},
    'छ': {'base': 0.8, 'voiced': False, 'aspirated': True, 'nasal': False, 'varga': 'talavya'},
    'ज': {'base': 0.8, 'voiced': True, 'aspirated': False, 'nasal': False, 'varga': 'talavya'},
    'झ': {'base': 0.8, 'voiced': True, 'aspirated': True, 'nasal': False, 'varga': 'talavya'},
    'ञ': {'base': 0.8, 'voiced': True, 'aspirated': False, 'nasal': True, 'varga': 'talavya'},
    
    # Murdhanya Varga (Retroflex)
    'ट': {'base': 0.7, 'voiced': False, 'aspirated': False, 'nasal': False, 'varga': 'murdhanya'},
    'ठ': {'base': 0.7, 'voiced': False, 'aspirated': True, 'nasal': False, 'varga': 'murdhanya'},
    'ड': {'base': 0.7, 'voiced': True, 'aspirated': False, 'nasal': False, 'varga': 'murdhanya'},
    'ढ': {'base': 0.7, 'voiced': True, 'aspirated': True, 'nasal': False, 'varga': 'murdhanya'},
    'ण': {'base': 0.7, 'voiced': True, 'aspirated': False, 'nasal': True, 'varga': 'murdhanya'},
    
    # Dantya Varga (Dental)
    'त': {'base': 0.9, 'voiced': False, 'aspirated': False, 'nasal': False, 'varga': 'dantya'},
    'थ': {'base': 0.9, 'voiced': False, 'aspirated': True, 'nasal': False, 'varga': 'dantya'},
    'द': {'base': 0.9, 'voiced': True, 'aspirated': False, 'nasal': False, 'varga': 'dantya'},
    'ध': {'base': 0.9, 'voiced': True, 'aspirated': True, 'nasal': False, 'varga': 'dantya'},
    'न': {'base': 0.9, 'voiced': True, 'aspirated': False, 'nasal': True, 'varga': 'dantya'},
    
    # Oshthya Varga (Labial)
    'प': {'base': 0.6, 'voiced': False, 'aspirated': False, 'nasal': False, 'varga': 'oshthya'},
    'फ': {'base': 0.6, 'voiced': False, 'aspirated': True, 'nasal': False, 'varga': 'oshthya'},
    'ब': {'base': 0.6, 'voiced': True, 'aspirated': False, 'nasal': False, 'varga': 'oshthya'},
    'भ': {'base': 0.6, 'voiced': True, 'aspirated': True, 'nasal': False, 'varga': 'oshthya'},
    'म': {'base': 0.6, 'voiced': True, 'aspirated': False, 'nasal': True, 'varga': 'oshthya'},
}

# =============================================================================
# SOUND GENERATION FUNCTIONS
# =============================================================================

def generate_sine(freq, duration, sample_rate=SAMPLE_RATE):
    """Generate a pure sine wave."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    return np.sin(2 * np.pi * freq * t)


def generate_harmonics(fundamental, duration, harmonic_weights=None, sample_rate=SAMPLE_RATE):
    """
    Generate a tone with harmonics (more natural than pure sine).
    
    Human voice typically has these harmonic ratios:
    - Fundamental (1x): 100%
    - 2nd harmonic (2x): 50%
    - 3rd harmonic (3x): 25%
    - 4th harmonic (4x): 12.5%
    """
    if harmonic_weights is None:
        harmonic_weights = [1.0, 0.5, 0.25, 0.125, 0.0625]
    
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.zeros_like(t)
    
    for i, weight in enumerate(harmonic_weights):
        harmonic_freq = fundamental * (i + 1)
        wave += weight * np.sin(2 * np.pi * harmonic_freq * t)
    
    return wave / np.max(np.abs(wave))


def apply_envelope(wave, attack=0.05, decay=0.05, sustain_level=0.8, release=0.1):
    """Apply ADSR envelope to a wave."""
    total_samples = len(wave)
    
    attack_samples = int(attack * SAMPLE_RATE)
    decay_samples = int(decay * SAMPLE_RATE)
    release_samples = int(release * SAMPLE_RATE)
    sustain_samples = total_samples - attack_samples - decay_samples - release_samples
    
    if sustain_samples < 0:
        # If too short, just do simple attack-release
        envelope = np.concatenate([
            np.linspace(0, 1, total_samples // 2),
            np.linspace(1, 0, total_samples - total_samples // 2)
        ])
    else:
        envelope = np.concatenate([
            np.linspace(0, 1, attack_samples),  # Attack
            np.linspace(1, sustain_level, decay_samples),  # Decay
            np.full(sustain_samples, sustain_level),  # Sustain
            np.linspace(sustain_level, 0, release_samples)  # Release
        ])
    
    # Ensure envelope matches wave length
    if len(envelope) < len(wave):
        envelope = np.pad(envelope, (0, len(wave) - len(envelope)), 'constant')
    elif len(envelope) > len(wave):
        envelope = envelope[:len(wave)]
    
    return wave * envelope


def add_nasal_resonance(wave, nasal_freq=280, nasal_amount=0.3):
    """Add nasal resonance for nasal consonants (ङ, ञ, ण, न, म)."""
    nasal_component = nasal_amount * generate_sine(nasal_freq, len(wave) / SAMPLE_RATE)
    return wave + nasal_component


def add_aspiration(wave, aspiration_duration=0.05, aspiration_amount=0.2):
    """Add aspiration noise for aspirated consonants (ख, घ, छ, झ, etc.)."""
    aspiration_samples = int(aspiration_duration * SAMPLE_RATE)
    noise = aspiration_amount * np.random.randn(aspiration_samples)
    
    # Apply envelope to noise
    noise_envelope = np.linspace(1, 0, aspiration_samples)
    noise = noise * noise_envelope
    
    # Append noise after the main wave
    return np.concatenate([wave, noise])


# =============================================================================
# VOWEL GENERATION
# =============================================================================

def generate_vowel(vowel_char, pitch_factor=1.0, base_freq=OM_BASE_FREQ):
    """
    Generate a Sanskrit vowel sound.
    
    Parameters:
        vowel_char: Devanagari vowel character
        pitch_factor: Multiplier for pitch (default 1.0)
        base_freq: Base frequency (default OM = 136.1 Hz)
    
    Returns:
        numpy array of audio samples
    """
    if vowel_char not in VOWEL_DATA:
        print(f"Warning: Unknown vowel '{vowel_char}', using अ")
        vowel_char = 'अ'
    
    data = VOWEL_DATA[vowel_char]
    freq = base_freq * data['ratio'] * pitch_factor
    duration = data['matras'] * MATRA_DURATION
    
    # Generate base tone with harmonics
    wave = generate_harmonics(freq, duration)
    
    # Add vowel-specific characteristics
    if data['position'] == 'nasal':
        wave = add_nasal_resonance(wave)
    
    # Apply envelope
    wave = apply_envelope(wave, attack=0.03, release=0.05)
    
    return wave


# =============================================================================
# CONSONANT GENERATION
# =============================================================================

def generate_consonant(consonant_char, following_vowel='अ', base_freq=OM_BASE_FREQ):
    """
    Generate a Sanskrit consonant + inherent vowel.
    
    In Sanskrit, consonants are pronounced with inherent 'a' (schwa).
    """
    if consonant_char not in CONSONANT_DATA:
        print(f"Warning: Unknown consonant '{consonant_char}'")
        return np.array([])
    
    data = CONSONANT_DATA[consonant_char]
    
    # Consonant portion (very short)
    consonant_duration = 0.08
    vowel_duration = MATRA_DURATION
    
    # Base frequency for consonant
    freq = base_freq * data['base']
    
    # Generate consonant attack
    if data['voiced']:
        # Voiced consonants have continuous vibration
        consonant_wave = generate_harmonics(freq, consonant_duration)
    else:
        # Voiceless consonants start with silence/burst
        consonant_wave = np.zeros(int(consonant_duration * SAMPLE_RATE))
        # Add brief burst
        burst_duration = 0.02
        burst = 0.3 * np.random.randn(int(burst_duration * SAMPLE_RATE))
        consonant_wave[:len(burst)] = burst
    
    # Add nasal if needed
    if data['nasal']:
        consonant_wave = add_nasal_resonance(consonant_wave)
    
    # Generate following vowel
    vowel_wave = generate_vowel(following_vowel, base_freq=base_freq)
    
    # Add aspiration if needed
    if data['aspirated']:
        consonant_wave = add_aspiration(consonant_wave)
    
    # Combine consonant and vowel
    combined = np.concatenate([consonant_wave, vowel_wave])
    
    # Apply overall envelope
    combined = apply_envelope(combined, attack=0.02, release=0.08)
    
    return combined


# =============================================================================
# OM GENERATION — The Most Sacred Sound
# =============================================================================

def generate_om(duration=3.0, base_freq=OM_BASE_FREQ):
    """
    Generate the sacred OM (ॐ) sound.
    
    OM = A (40%) + U (30%) + M (20%) + Silence (10%)
    
    This represents:
    - A (अ): Waking state, creation, Brahma
    - U (उ): Dream state, preservation, Vishnu
    - M (म): Deep sleep, dissolution, Shiva
    - Silence: Turiya, pure consciousness
    """
    a_duration = duration * 0.4
    u_duration = duration * 0.3
    m_duration = duration * 0.2
    silence_duration = duration * 0.1
    
    # A component - open throat, fundamental frequency
    a_freq = base_freq * 1.0
    a_wave = generate_harmonics(a_freq, a_duration)
    
    # U component - lips rounded, slightly lower frequency
    u_freq = base_freq * 0.8
    u_wave = generate_harmonics(u_freq, u_duration)
    
    # M component - lips closed, nasal resonance
    m_freq = base_freq * 0.9
    m_wave = generate_harmonics(m_freq, m_duration)
    m_wave = add_nasal_resonance(m_wave, nasal_amount=0.4)
    
    # Silence
    silence = np.zeros(int(silence_duration * SAMPLE_RATE))
    
    # Create smooth transitions
    transition_samples = int(0.05 * SAMPLE_RATE)
    
    # A to U transition
    a_fade = np.linspace(1, 0, transition_samples)
    u_fade = np.linspace(0, 1, transition_samples)
    a_wave[-transition_samples:] *= a_fade
    u_wave[:transition_samples] *= u_fade
    
    # U to M transition
    u_wave[-transition_samples:] *= a_fade
    m_wave[:transition_samples] *= u_fade
    
    # Combine all components
    om = np.concatenate([a_wave, u_wave, m_wave, silence])
    
    # Apply master envelope
    master_envelope = np.ones(len(om))
    fade_out_samples = int(0.3 * len(om))
    master_envelope[-fade_out_samples:] = np.linspace(1, 0, fade_out_samples)
    
    om = om * master_envelope
    
    return om


# =============================================================================
# MANTRA GENERATION
# =============================================================================

def generate_simple_mantra(text, base_freq=OM_BASE_FREQ):
    """
    Generate a simple mantra from Devanagari text.
    (Basic implementation - handles only common characters)
    """
    result = []
    
    i = 0
    while i < len(text):
        char = text[i]
        
        # Skip spaces and punctuation
        if char in ' ।॥':
            # Add brief silence for word/phrase breaks
            silence = np.zeros(int(0.2 * SAMPLE_RATE))
            result.append(silence)
            i += 1
            continue
        
        # Check for OM symbol
        if char == 'ॐ':
            result.append(generate_om(2.0, base_freq))
            i += 1
            continue
        
        # Check for vowel
        if char in VOWEL_DATA:
            result.append(generate_vowel(char, base_freq=base_freq))
            i += 1
            continue
        
        # Check for consonant
        if char in CONSONANT_DATA:
            # Look ahead for vowel modifier
            following_vowel = 'अ'  # Default inherent vowel
            if i + 1 < len(text):
                next_char = text[i + 1]
                # Map matra (vowel signs) to full vowels
                matra_map = {
                    'ा': 'आ', 'ि': 'इ', 'ी': 'ई', 'ु': 'उ', 'ू': 'ऊ',
                    'े': 'ए', 'ै': 'ऐ', 'ो': 'ओ', 'ौ': 'औ', 'ं': 'अं', 'ः': 'अः',
                    '्': None  # Halant - no vowel
                }
                if next_char in matra_map:
                    following_vowel = matra_map[next_char] if matra_map[next_char] else ''
                    i += 1
            
            if following_vowel:
                result.append(generate_consonant(char, following_vowel, base_freq))
            else:
                # Halant - consonant without vowel (simplified)
                result.append(generate_consonant(char, 'अ', base_freq)[:int(0.1 * SAMPLE_RATE)])
            
            i += 1
            continue
        
        # Unknown character - skip
        i += 1
    
    if result:
        return np.concatenate(result)
    else:
        return np.array([])


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def normalize_audio(audio):
    """Normalize audio to prevent clipping."""
    max_val = np.max(np.abs(audio))
    if max_val > 0:
        return audio / max_val * 0.9
    return audio


def save_wav(audio, filename, sample_rate=SAMPLE_RATE):
    """Save audio as WAV file."""
    audio = normalize_audio(audio)
    audio_int16 = np.int16(audio * 32767)
    wavfile.write(filename, sample_rate, audio_int16)
    print(f"✅ Saved: {filename}")


# =============================================================================
# MAIN - Generate Sample Files
# =============================================================================

def main():
    """Generate sample Vedic sound files."""
    
    print("=" * 60)
    print("🕉️ वैदिक-ध्वनि-संश्लेषण — Vedic Sound Synthesis")
    print("=" * 60)
    print()
    
    # Create output directory
    output_dir = "vedic_sounds"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 1. Generate OM
    print("Generating ॐ (OM)...")
    om = generate_om(3.0)
    save_wav(om, os.path.join(output_dir, "om.wav"))
    
    # 2. Generate all vowels
    print("\nGenerating vowels (स्वर)...")
    for vowel in ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ']:
        wave = generate_vowel(vowel)
        name = VOWEL_DATA[vowel]['name']
        save_wav(wave, os.path.join(output_dir, f"vowel_{name}.wav"))
    
    # 3. Generate consonant samples
    print("\nGenerating consonants (व्यञ्जन)...")
    sample_consonants = ['क', 'ख', 'ग', 'घ', 'ङ', 'म', 'न', 'प', 'ब']
    for consonant in sample_consonants:
        wave = generate_consonant(consonant)
        save_wav(wave, os.path.join(output_dir, f"consonant_{consonant}.wav"))
    
    # 4. Generate simple mantras
    print("\nGenerating mantras...")
    
    # Short OM mantra
    mantra1 = "ॐ नमः"
    wave1 = generate_simple_mantra(mantra1)
    save_wav(wave1, os.path.join(output_dir, "mantra_om_namah.wav"))
    
    # Om Shanti
    mantra2 = "ॐ शान्तिः"
    wave2 = generate_simple_mantra(mantra2)
    save_wav(wave2, os.path.join(output_dir, "mantra_om_shantih.wav"))
    
    print("\n" + "=" * 60)
    print(f"✅ All files saved to '{output_dir}/' directory")
    print("=" * 60)
    print("\n🙏 ॐ वाचे नमः — May Sound guide us to Truth")


if __name__ == "__main__":
    main()

