#!/usr/bin/env python3
"""
🌍 पर्यावरण-ध्वनि-चिकित्सा — Environmental Sound Healing Generator
====================================================================

Generate healing frequencies for environmental restoration.

> "ध्वनि शक्तिः पृथ्वी चिकित्सा"
> "Dhvani Shaktih Prithvi Chikitsa"
> "Sound power heals the Earth."

Usage:
    python frequency_generator.py [mode]
    
Modes:
    water     - Generate water healing frequencies (528 Hz primary)
    air       - Generate air purification frequencies
    soil      - Generate soil regeneration frequencies
    schumann  - Generate Schumann resonance (7.83 Hz)
    om        - Generate OM frequency (136.1 Hz)
    solfeggio - Generate all Solfeggio frequencies
    all       - Generate complete healing set

Requirements:
    pip install numpy scipy

Author: Shunya-0 Project
License: Open for Dharmic and Environmental Use
"""

import numpy as np
from scipy.io import wavfile
import os
import sys

# =============================================================================
# HEALING FREQUENCIES
# =============================================================================

FREQUENCIES = {
    # Earth Resonance
    'schumann': {
        'hz': 7.83,
        'name': 'Schumann Resonance',
        'purpose': 'Earth heartbeat, grounding all life',
        'element': 'Earth'
    },
    
    # Universal OM
    'om': {
        'hz': 136.1,
        'name': 'OM Frequency',
        'purpose': 'Universal harmonizer, cosmic tuning',
        'element': 'Akasha'
    },
    
    # Solfeggio Frequencies
    'ut': {
        'hz': 396,
        'name': 'UT - Liberation',
        'purpose': 'Release fear and guilt, grounding',
        'element': 'Earth'
    },
    're': {
        'hz': 417,
        'name': 'RE - Resonance',
        'purpose': 'Facilitate change, break patterns',
        'element': 'Water'
    },
    'mi': {
        'hz': 528,
        'name': 'MI - Miracle',
        'purpose': 'DNA repair, water structuring ★',
        'element': 'Water'
    },
    'fa': {
        'hz': 639,
        'name': 'FA - Family',
        'purpose': 'Reconnection, relationship healing',
        'element': 'Air'
    },
    'sol': {
        'hz': 741,
        'name': 'SOL - Solve',
        'purpose': 'Awakening intuition, problem solving',
        'element': 'Fire'
    },
    'la': {
        'hz': 852,
        'name': 'LA - Labii',
        'purpose': 'Return to spiritual order',
        'element': 'Akasha'
    },
    'si': {
        'hz': 963,
        'name': 'SI - Saints',
        'purpose': 'Divine connection, highest healing',
        'element': 'Akasha'
    },
    
    # Additional Healing Frequencies
    'healing_174': {
        'hz': 174,
        'name': 'Foundation Frequency',
        'purpose': 'Pain relief, security, foundation',
        'element': 'Earth'
    },
    'healing_285': {
        'hz': 285,
        'name': 'Regeneration Frequency',
        'purpose': 'Tissue regeneration, cell repair',
        'element': 'Water'
    },
    'verdi_432': {
        'hz': 432,
        'name': 'Verdi Tuning',
        'purpose': 'Natural harmony, mathematical tuning',
        'element': 'All'
    },
}

# =============================================================================
# CONSTANTS
# =============================================================================

SAMPLE_RATE = 44100
DEFAULT_DURATION = 300  # 5 minutes

# =============================================================================
# SOUND GENERATION
# =============================================================================

def generate_pure_tone(frequency, duration, sample_rate=SAMPLE_RATE):
    """Generate a pure sine wave tone."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * frequency * t)
    return wave


def generate_binaural(base_freq, beat_freq, duration, sample_rate=SAMPLE_RATE):
    """
    Generate binaural beat.
    
    Left ear: base_freq
    Right ear: base_freq + beat_freq
    
    Brain perceives the difference as a beat.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    left = np.sin(2 * np.pi * base_freq * t)
    right = np.sin(2 * np.pi * (base_freq + beat_freq) * t)
    
    # Combine into stereo
    stereo = np.column_stack((left, right))
    return stereo


def generate_harmonic_rich(frequency, duration, sample_rate=SAMPLE_RATE):
    """Generate a harmonically rich tone (more natural than pure sine)."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Fundamental + harmonics
    wave = np.sin(2 * np.pi * frequency * t)
    wave += 0.5 * np.sin(2 * np.pi * frequency * 2 * t)
    wave += 0.25 * np.sin(2 * np.pi * frequency * 3 * t)
    wave += 0.125 * np.sin(2 * np.pi * frequency * 4 * t)
    wave += 0.0625 * np.sin(2 * np.pi * frequency * 5 * t)
    
    # Normalize
    wave = wave / np.max(np.abs(wave))
    return wave


def apply_envelope(wave, fade_in=5.0, fade_out=5.0, sample_rate=SAMPLE_RATE):
    """Apply fade in/out envelope."""
    fade_in_samples = int(fade_in * sample_rate)
    fade_out_samples = int(fade_out * sample_rate)
    
    envelope = np.ones(len(wave))
    
    # Fade in
    if fade_in_samples > 0:
        envelope[:fade_in_samples] = np.linspace(0, 1, fade_in_samples)
    
    # Fade out
    if fade_out_samples > 0:
        envelope[-fade_out_samples:] = np.linspace(1, 0, fade_out_samples)
    
    return wave * envelope


def add_nature_sounds(wave, intensity=0.1, sample_rate=SAMPLE_RATE):
    """Add subtle nature-like ambient sounds (pink noise)."""
    # Generate pink noise (1/f noise - more natural)
    white = np.random.randn(len(wave))
    
    # Simple pink noise approximation
    pink = np.cumsum(white)
    pink = pink - np.mean(pink)
    pink = pink / np.max(np.abs(pink))
    
    # Very subtle
    return wave + intensity * pink


def generate_layered_healing(primary_freq, duration, sample_rate=SAMPLE_RATE):
    """
    Generate layered healing sound with:
    - Primary healing frequency
    - Schumann resonance base
    - Subtle harmonics
    - Natural fade
    """
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Primary frequency (harmonic rich)
    primary = generate_harmonic_rich(primary_freq, duration, sample_rate)
    
    # Schumann resonance as subtle modulation (7.83 Hz)
    schumann_mod = 0.1 * np.sin(2 * np.pi * 7.83 * t)
    
    # OM undertone (136.1 Hz) - very subtle
    om_undertone = 0.1 * np.sin(2 * np.pi * 136.1 * t)
    
    # Combine
    wave = primary * (1 + schumann_mod) + om_undertone
    
    # Normalize
    wave = wave / np.max(np.abs(wave))
    
    # Apply envelope
    wave = apply_envelope(wave)
    
    return wave


# =============================================================================
# PRESET GENERATORS
# =============================================================================

def generate_water_healing(duration=DEFAULT_DURATION, output_dir='healing_frequencies'):
    """Generate complete water healing frequency set."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print("\n💧 Generating Water Healing Frequencies...")
    print("=" * 50)
    
    # Primary: 528 Hz (Miracle frequency)
    wave = generate_layered_healing(528, duration)
    save_wav(wave, os.path.join(output_dir, 'water_528hz_miracle.wav'))
    print("✅ 528 Hz (MI - Miracle) - Primary water structuring")
    
    # Secondary: 417 Hz (Breaking patterns)
    wave = generate_layered_healing(417, duration)
    save_wav(wave, os.path.join(output_dir, 'water_417hz_change.wav'))
    print("✅ 417 Hz (RE - Resonance) - Breaking pollution patterns")
    
    # Tertiary: 285 Hz (Regeneration)
    wave = generate_layered_healing(285, duration)
    save_wav(wave, os.path.join(output_dir, 'water_285hz_regeneration.wav'))
    print("✅ 285 Hz (Regeneration) - Cell/molecular repair")
    
    # Combined water healing
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    combined = (
        np.sin(2 * np.pi * 528 * t) * 0.6 +
        np.sin(2 * np.pi * 417 * t) * 0.25 +
        np.sin(2 * np.pi * 285 * t) * 0.15
    )
    combined = apply_envelope(combined)
    save_wav(combined, os.path.join(output_dir, 'water_combined_healing.wav'))
    print("✅ Combined water healing frequency")
    
    print("\n🙏 Water healing frequencies generated!")
    print(f"   Output directory: {output_dir}/")


def generate_air_healing(duration=DEFAULT_DURATION, output_dir='healing_frequencies'):
    """Generate air purification frequency set."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print("\n🌬️ Generating Air Healing Frequencies...")
    print("=" * 50)
    
    # 639 Hz (Reconnection)
    wave = generate_layered_healing(639, duration)
    save_wav(wave, os.path.join(output_dir, 'air_639hz_connection.wav'))
    print("✅ 639 Hz (FA - Family) - Ecosystem reconnection")
    
    # 741 Hz (Problem solving)
    wave = generate_layered_healing(741, duration)
    save_wav(wave, os.path.join(output_dir, 'air_741hz_clearing.wav'))
    print("✅ 741 Hz (SOL - Solve) - Clearing and awakening")
    
    # 852 Hz (Returning to order)
    wave = generate_layered_healing(852, duration)
    save_wav(wave, os.path.join(output_dir, 'air_852hz_order.wav'))
    print("✅ 852 Hz (LA - Labii) - Restoring natural order")
    
    print("\n🙏 Air healing frequencies generated!")


def generate_soil_healing(duration=DEFAULT_DURATION, output_dir='healing_frequencies'):
    """Generate soil regeneration frequency set."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print("\n🌱 Generating Soil Healing Frequencies...")
    print("=" * 50)
    
    # 174 Hz (Foundation)
    wave = generate_layered_healing(174, duration)
    save_wav(wave, os.path.join(output_dir, 'soil_174hz_foundation.wav'))
    print("✅ 174 Hz (Foundation) - Soil stress reduction")
    
    # 396 Hz (Liberation)
    wave = generate_layered_healing(396, duration)
    save_wav(wave, os.path.join(output_dir, 'soil_396hz_liberation.wav'))
    print("✅ 396 Hz (UT - Liberation) - Grounding energy")
    
    # 285 Hz (Regeneration)
    wave = generate_layered_healing(285, duration)
    save_wav(wave, os.path.join(output_dir, 'soil_285hz_regeneration.wav'))
    print("✅ 285 Hz (Regeneration) - Microbial enhancement")
    
    # Plant growth frequencies (research-based)
    # 1000-1500 Hz range activates plant stomata
    wave = generate_layered_healing(1200, duration)
    save_wav(wave, os.path.join(output_dir, 'soil_1200hz_plant_growth.wav'))
    print("✅ 1200 Hz - Plant growth activation")
    
    print("\n🙏 Soil healing frequencies generated!")


def generate_schumann(duration=DEFAULT_DURATION, output_dir='healing_frequencies'):
    """Generate Schumann resonance (Earth's frequency)."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print("\n🌍 Generating Schumann Resonance...")
    print("=" * 50)
    
    # 7.83 Hz is too low to hear directly
    # We create it as binaural beats or modulation
    
    # Method 1: Binaural beats (requires headphones)
    binaural = generate_binaural(200, 7.83, duration)
    save_wav_stereo(binaural, os.path.join(output_dir, 'schumann_binaural.wav'))
    print("✅ Schumann binaural (use headphones)")
    
    # Method 2: Modulated carrier
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    carrier = np.sin(2 * np.pi * 136.1 * t)  # OM as carrier
    modulator = np.sin(2 * np.pi * 7.83 * t)
    wave = carrier * (1 + 0.3 * modulator)
    wave = apply_envelope(wave)
    save_wav(wave, os.path.join(output_dir, 'schumann_om_modulated.wav'))
    print("✅ Schumann modulated with OM carrier")
    
    print("\n🙏 Schumann resonance generated!")


def generate_om(duration=DEFAULT_DURATION, output_dir='healing_frequencies'):
    """Generate OM frequency (136.1 Hz)."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print("\n🕉️ Generating OM Frequency...")
    print("=" * 50)
    
    wave = generate_layered_healing(136.1, duration)
    save_wav(wave, os.path.join(output_dir, 'om_136hz.wav'))
    print("✅ OM frequency (136.1 Hz)")
    
    # OM with Schumann modulation
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    om = generate_harmonic_rich(136.1, duration)
    schumann = np.sin(2 * np.pi * 7.83 * t)
    combined = om * (1 + 0.2 * schumann)
    combined = apply_envelope(combined)
    save_wav(combined, os.path.join(output_dir, 'om_schumann_combined.wav'))
    print("✅ OM + Schumann combined")
    
    print("\n🙏 OM frequency generated!")


def generate_all_solfeggio(duration=DEFAULT_DURATION, output_dir='healing_frequencies'):
    """Generate all Solfeggio frequencies."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print("\n🎵 Generating All Solfeggio Frequencies...")
    print("=" * 50)
    
    solfeggio = [
        (174, 'healing_174hz_foundation'),
        (285, 'healing_285hz_regeneration'),
        (396, 'solfeggio_396hz_liberation'),
        (417, 'solfeggio_417hz_change'),
        (528, 'solfeggio_528hz_miracle'),
        (639, 'solfeggio_639hz_connection'),
        (741, 'solfeggio_741hz_awakening'),
        (852, 'solfeggio_852hz_order'),
        (963, 'solfeggio_963hz_divine'),
    ]
    
    for freq, name in solfeggio:
        wave = generate_layered_healing(freq, duration)
        save_wav(wave, os.path.join(output_dir, f'{name}.wav'))
        print(f"✅ {freq} Hz - {name.split('_')[-1].capitalize()}")
    
    print("\n🙏 All Solfeggio frequencies generated!")


# =============================================================================
# FILE I/O
# =============================================================================

def save_wav(wave, filename, sample_rate=SAMPLE_RATE):
    """Save mono wave as WAV file."""
    wave = wave / np.max(np.abs(wave)) * 0.9
    wave_int16 = np.int16(wave * 32767)
    wavfile.write(filename, sample_rate, wave_int16)


def save_wav_stereo(wave, filename, sample_rate=SAMPLE_RATE):
    """Save stereo wave as WAV file."""
    wave = wave / np.max(np.abs(wave)) * 0.9
    wave_int16 = np.int16(wave * 32767)
    wavfile.write(filename, sample_rate, wave_int16)


# =============================================================================
# MAIN
# =============================================================================

def print_usage():
    print("""
🌍 Environmental Sound Healing Generator
=========================================

Usage: python frequency_generator.py [mode] [duration_minutes]

Modes:
  water     - Water healing frequencies (528 Hz primary)
  air       - Air purification frequencies
  soil      - Soil regeneration frequencies
  schumann  - Schumann resonance (7.83 Hz)
  om        - OM frequency (136.1 Hz)
  solfeggio - All Solfeggio frequencies
  all       - Generate complete healing set

Examples:
  python frequency_generator.py water
  python frequency_generator.py all 10   (10 minute files)
  python frequency_generator.py om 30    (30 minute OM)

Output: healing_frequencies/ folder
    """)


def main():
    if len(sys.argv) < 2:
        print_usage()
        mode = 'all'
    else:
        mode = sys.argv[1].lower()
    
    # Duration in minutes (default 5)
    duration_minutes = 5
    if len(sys.argv) >= 3:
        try:
            duration_minutes = int(sys.argv[2])
        except:
            pass
    
    duration_seconds = duration_minutes * 60
    
    print("=" * 60)
    print("🌍 पर्यावरण-ध्वनि-चिकित्सा — Environmental Sound Healing")
    print("=" * 60)
    print(f"\nMode: {mode}")
    print(f"Duration: {duration_minutes} minutes per file")
    
    if mode == 'water':
        generate_water_healing(duration_seconds)
    elif mode == 'air':
        generate_air_healing(duration_seconds)
    elif mode == 'soil':
        generate_soil_healing(duration_seconds)
    elif mode == 'schumann':
        generate_schumann(duration_seconds)
    elif mode == 'om':
        generate_om(duration_seconds)
    elif mode == 'solfeggio':
        generate_all_solfeggio(duration_seconds)
    elif mode == 'all':
        generate_water_healing(duration_seconds)
        generate_air_healing(duration_seconds)
        generate_soil_healing(duration_seconds)
        generate_schumann(duration_seconds)
        generate_om(duration_seconds)
        generate_all_solfeggio(duration_seconds)
    else:
        print(f"\n❌ Unknown mode: {mode}")
        print_usage()
        return
    
    print("\n" + "=" * 60)
    print("✅ Generation complete!")
    print("=" * 60)
    print("\n🙏 ॐ भूम्यै नमः — May sound heal the Earth")
    print("\nHOW TO USE:")
    print("• Water: Play near water bodies, in water treatment")
    print("• Air: Play in polluted areas, during Agnihotra")
    print("• Soil: Play in gardens, farms, degraded land")
    print("• Use speakers (not headphones) for environmental healing")
    print("• Minimum 20-30 minutes per session")
    print("• Combine with intention and Sankalpa")


if __name__ == "__main__":
    main()

