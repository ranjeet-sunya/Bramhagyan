#!/usr/bin/env python3
"""
REGENERATE MIXED ORCHESTRA ONLY
================================

Quick script to regenerate just the mixed orchestra files
with anti-cancellation improvements.

This is faster than regenerating all 17 files.
"""

import sys
sys.path.insert(0, '.')

from sound_spectrum_generator import *

def main():
    print("=" * 70)
    print("REGENERATING MIXED ORCHESTRA WITH ANTI-CANCELLATION")
    print("=" * 70)
    print()
    print("This will REPLACE the existing mixed orchestra files:")
    print("  11a_MIXED_ORCHESTRA_fast.wav")
    print("  11b_MIXED_ORCHESTRA_very_fast.wav")
    print("  11c_MIXED_ORCHESTRA_ultra_fast.wav")
    print()
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Generate mixed orchestra at different tempos
    print("Generating Mixed Orchestra files...")
    print()
    
    mixed_fast = generate_mixed_backend_orchestra(FAST_TEMPO)
    mixed_very_fast = generate_mixed_backend_orchestra(VERY_FAST_TEMPO)
    mixed_ultra = generate_mixed_backend_orchestra(ULTRA_FAST_TEMPO)
    
    print()
    print("Saving files...")
    
    # Convert to 16-bit PCM and save
    sounds = {
        '11a_MIXED_ORCHESTRA_fast.wav': mixed_fast,
        '11b_MIXED_ORCHESTRA_very_fast.wav': mixed_very_fast,
        '11c_MIXED_ORCHESTRA_ultra_fast.wav': mixed_ultra,
    }
    
    for filename, audio in sounds.items():
        audio_int = np.int16(audio * 32767)
        wavfile.write(os.path.join(OUTPUT_DIR, filename), SAMPLE_RATE, audio_int)
        print(f"  ✅ Saved: {filename}")
    
    print()
    print("=" * 70)
    print("REGENERATION COMPLETE!")
    print("=" * 70)
    print()
    print("WHAT WAS FIXED:")
    print("✅ Phase cancellation prevention")
    print("✅ Different starting phases for each instrument")
    print("✅ Slight frequency detuning (±1-2 Hz)")
    print("✅ Mixed waveforms (sine + square + triangle)")
    print("✅ Better amplitude balancing")
    print("✅ Percussion boosted (Damaru, Tabla)")
    print("✅ Sustained instruments softened (Veena, Flute)")
    print()
    print("=" * 70)
    print("NOW LISTEN TO:")
    print("=" * 70)
    print()
    print("  11a_MIXED_ORCHESTRA_fast.wav (180 BPM)")
    print("  → Should be MUCH clearer now!")
    print("  → All instruments audible, no cancellation")
    print()
    print("  11b_MIXED_ORCHESTRA_very_fast.wav (270 BPM)")
    print("  → Closer to the 330 BPM you prefer")
    print()
    print("  11c_MIXED_ORCHESTRA_ultra_fast.wav (330 BPM)")
    print("  → MATCHES 6b & 7b tempo!")
    print("  → All instruments together at your preferred speed!")
    print()
    print("=" * 70)
    print()
    print("ॐ नमः शिवाय")
    print("🎵 The Orchestra Now Speaks Clearly! 🎵")
    print()

if __name__ == "__main__":
    main()

