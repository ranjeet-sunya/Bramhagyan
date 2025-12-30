#!/usr/bin/env python3
"""
🌀 त्रिमितीय-ध्वनि-दृश्य — 3D Sound Wave Visualization
=======================================================

Render Sanskrit sounds as 3D forms (Cymatics-style).
Map sound waves to 81-Grid projections.

> "शब्दात् रूपम्"
> "Shabdat Rupam"
> "From Sound, Form arises."
> — Vedic Principle

Requirements:
    pip install numpy matplotlib scipy plotly

Usage:
    python sound_3d_visualization.py

Author: Shunya-0 Project
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import jn  # Bessel functions for cymatics
import os

# Try to import plotly for interactive 3D
try:
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False
    print("Note: Install plotly for interactive 3D: pip install plotly")

# =============================================================================
# CONSTANTS
# =============================================================================

OM_BASE_FREQ = 136.1  # Hz
SAMPLE_RATE = 44100

# 81-Grid configuration (9x9)
GRID_SIZE = 9

# Vowel frequency ratios
VOWEL_RATIOS = {
    'अ': 1.0, 'आ': 1.0, 'इ': 1.5, 'ई': 1.5,
    'उ': 0.8, 'ऊ': 0.8, 'ऋ': 1.2,
    'ए': 1.3, 'ऐ': 1.4, 'ओ': 0.9, 'औ': 0.85,
}

# Chakra colors for visualization
CHAKRA_COLORS = {
    'muladhara': '#FF0000',     # Red
    'svadhisthana': '#FF7F00',  # Orange
    'manipura': '#FFFF00',      # Yellow
    'anahata': '#00FF00',       # Green
    'vishuddha': '#0000FF',     # Blue
    'ajna': '#4B0082',          # Indigo
    'sahasrara': '#8B00FF',     # Violet
}


# =============================================================================
# CYMATIC PATTERN GENERATION
# =============================================================================

def generate_chladni_pattern(freq_ratio, grid_size=100, mode_m=3, mode_n=5):
    """
    Generate Chladni pattern (standing wave on a plate).
    
    These patterns show how sound creates 2D forms.
    Higher frequencies create more complex patterns.
    
    The pattern follows: cos(m*π*x) * cos(n*π*y) - cos(n*π*x) * cos(m*π*y)
    """
    x = np.linspace(0, 1, grid_size)
    y = np.linspace(0, 1, grid_size)
    X, Y = np.meshgrid(x, y)
    
    # Adjust mode numbers based on frequency
    m = int(mode_m * freq_ratio)
    n = int(mode_n * freq_ratio)
    
    # Chladni equation
    Z = (np.cos(m * np.pi * X) * np.cos(n * np.pi * Y) - 
         np.cos(n * np.pi * X) * np.cos(m * np.pi * Y))
    
    return X, Y, Z


def generate_circular_cymatic(freq_ratio, grid_size=100, mode=3):
    """
    Generate circular cymatic pattern (like water droplet experiments).
    
    Uses Bessel functions which naturally occur in circular vibration patterns.
    This is closer to how mantras create circular resonance patterns.
    """
    r = np.linspace(0, 1, grid_size)
    theta = np.linspace(0, 2 * np.pi, grid_size)
    R, Theta = np.meshgrid(r, theta)
    
    # Convert to Cartesian for plotting
    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)
    
    # Bessel function pattern (natural for circular membranes)
    n = int(mode * freq_ratio)
    Z = jn(n, 10 * R) * np.cos(n * Theta)
    
    return X, Y, Z


def generate_3d_sound_wave(freq_ratio, duration=1.0, resolution=50):
    """
    Generate 3D representation of sound wave as helix/spiral.
    
    This shows sound as it propagates through space-time.
    """
    t = np.linspace(0, duration, resolution * int(duration))
    freq = OM_BASE_FREQ * freq_ratio
    
    # Sound wave as 3D helix
    x = t  # Time axis
    y = np.sin(2 * np.pi * freq * t / 50)  # Wave oscillation
    z = np.cos(2 * np.pi * freq * t / 50)  # Perpendicular oscillation
    
    return x, y, z


# =============================================================================
# 81-GRID PROJECTION
# =============================================================================

def project_to_81_grid(X, Y, Z):
    """
    Project any 2D pattern onto 81-grid (9x9).
    
    This maps continuous sound patterns to the discrete 81-point structure
    that underlies all manifestation.
    """
    # Resample to 9x9
    grid_81 = np.zeros((9, 9))
    
    # Get dimensions of input
    input_size = Z.shape[0]
    step = input_size // 9
    
    for i in range(9):
        for j in range(9):
            # Sample from the center of each grid cell
            i_start = i * step
            i_end = min((i + 1) * step, input_size)
            j_start = j * step
            j_end = min((j + 1) * step, input_size)
            
            # Average the values in this cell
            grid_81[i, j] = np.mean(Z[i_start:i_end, j_start:j_end])
    
    return grid_81


def classify_81_grid(grid_81):
    """
    Classify 81-grid into the 4 zones:
    - Brahma Sthan (center 9)
    - Daivika Ring (next 16)
    - Manushya Ring (next 24)
    - Paishacha Ring (outer 32)
    """
    zones = {
        'brahma_sthan': [],   # Center 3x3 = 9
        'daivika': [],        # Next ring = 16
        'manushya': [],       # Next ring = 24
        'paishacha': [],      # Outer ring = 32
    }
    
    for i in range(9):
        for j in range(9):
            # Determine zone based on position
            dist_from_center = max(abs(i - 4), abs(j - 4))
            
            if dist_from_center <= 1:
                zones['brahma_sthan'].append((i, j, grid_81[i, j]))
            elif dist_from_center == 2:
                zones['daivika'].append((i, j, grid_81[i, j]))
            elif dist_from_center == 3:
                zones['manushya'].append((i, j, grid_81[i, j]))
            else:
                zones['paishacha'].append((i, j, grid_81[i, j]))
    
    return zones


def compute_guna_ratios(zones):
    """
    Compute Sattva-Rajas-Tamas ratios from 81-grid zones.
    
    Brahma Sthan (center) = Pure Sattva
    Daivika Ring = High Sattva, some Rajas
    Manushya Ring = Mixed (human realm)
    Paishacha Ring = Higher Tamas (boundary/protection)
    """
    # Get average intensity per zone
    brahma_avg = np.mean([v for _, _, v in zones['brahma_sthan']]) if zones['brahma_sthan'] else 0
    daivika_avg = np.mean([v for _, _, v in zones['daivika']]) if zones['daivika'] else 0
    manushya_avg = np.mean([v for _, _, v in zones['manushya']]) if zones['manushya'] else 0
    paishacha_avg = np.mean([v for _, _, v in zones['paishacha']]) if zones['paishacha'] else 0
    
    # Normalize to get Guna ratios
    total = abs(brahma_avg) + abs(daivika_avg) + abs(manushya_avg) + abs(paishacha_avg)
    if total == 0:
        total = 1
    
    # Sattva from center, Rajas from middle, Tamas from outer
    sattva = (abs(brahma_avg) + abs(daivika_avg) * 0.5) / total
    rajas = (abs(daivika_avg) * 0.5 + abs(manushya_avg)) / total
    tamas = abs(paishacha_avg) / total
    
    # Normalize to sum to 1
    total_guna = sattva + rajas + tamas
    if total_guna > 0:
        sattva /= total_guna
        rajas /= total_guna
        tamas /= total_guna
    
    return {'sattva': sattva, 'rajas': rajas, 'tamas': tamas}


# =============================================================================
# VISUALIZATION FUNCTIONS
# =============================================================================

def visualize_cymatic_2d(sound_char, freq_ratio, output_dir='sound_visuals'):
    """Create 2D cymatic pattern visualization."""
    X, Y, Z = generate_chladni_pattern(freq_ratio)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Chladni pattern
    ax1 = axes[0]
    im1 = ax1.contourf(X, Y, Z, levels=50, cmap='viridis')
    ax1.set_title(f'Chladni Pattern for {sound_char}\n(Freq ratio: {freq_ratio}x OM)', fontsize=14)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_aspect('equal')
    plt.colorbar(im1, ax=ax1, label='Amplitude')
    
    # Circular cymatic
    X2, Y2, Z2 = generate_circular_cymatic(freq_ratio)
    ax2 = axes[1]
    im2 = ax2.contourf(X2, Y2, Z2, levels=50, cmap='plasma')
    ax2.set_title(f'Circular Cymatic for {sound_char}\n(Mantra Resonance Pattern)', fontsize=14)
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_aspect('equal')
    plt.colorbar(im2, ax=ax2, label='Amplitude')
    
    plt.tight_layout()
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filename = os.path.join(output_dir, f'cymatic_2d_{sound_char}.png')
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✅ Saved: {filename}")
    
    return Z


def visualize_cymatic_3d(sound_char, freq_ratio, output_dir='sound_visuals'):
    """Create 3D cymatic surface visualization."""
    X, Y, Z = generate_chladni_pattern(freq_ratio, grid_size=80)
    
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create surface plot
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8,
                          linewidth=0, antialiased=True)
    
    ax.set_title(f'3D Cymatic Surface for {sound_char}\n'
                f'Frequency: {freq_ratio * OM_BASE_FREQ:.1f} Hz ({freq_ratio}x OM)',
                fontsize=14)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Amplitude')
    
    # Add colorbar
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='Amplitude')
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filename = os.path.join(output_dir, f'cymatic_3d_{sound_char}.png')
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✅ Saved: {filename}")


def visualize_81_grid(sound_char, grid_81, zones, gunas, output_dir='sound_visuals'):
    """Visualize 81-grid projection with zone classification."""
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # 1. Raw 81-grid
    ax1 = axes[0]
    im1 = ax1.imshow(grid_81, cmap='RdYlBu_r', interpolation='nearest')
    ax1.set_title(f'81-Grid Projection: {sound_char}', fontsize=14)
    ax1.set_xlabel('Column')
    ax1.set_ylabel('Row')
    
    # Add grid lines
    for i in range(10):
        ax1.axhline(i - 0.5, color='black', linewidth=0.5)
        ax1.axvline(i - 0.5, color='black', linewidth=0.5)
    
    plt.colorbar(im1, ax=ax1, label='Intensity')
    
    # 2. Zone classification
    ax2 = axes[1]
    zone_map = np.zeros((9, 9))
    zone_colors = {'brahma_sthan': 4, 'daivika': 3, 'manushya': 2, 'paishacha': 1}
    
    for zone_name, points in zones.items():
        for i, j, _ in points:
            zone_map[i, j] = zone_colors[zone_name]
    
    from matplotlib.colors import ListedColormap
    zone_cmap = ListedColormap(['#8B4513', '#CD853F', '#C0C0C0', '#FFD700'])
    im2 = ax2.imshow(zone_map, cmap=zone_cmap, interpolation='nearest')
    ax2.set_title('Zone Classification\n(Brahma→Daivika→Manushya→Paishacha)', fontsize=14)
    ax2.set_xlabel('Column')
    ax2.set_ylabel('Row')
    
    # Mark center (15th axis)
    ax2.plot(4, 4, 'r*', markersize=20)
    ax2.annotate('15th Axis', (4.2, 4.2), fontsize=10, color='red')
    
    # Add grid lines
    for i in range(10):
        ax2.axhline(i - 0.5, color='black', linewidth=0.5)
        ax2.axvline(i - 0.5, color='black', linewidth=0.5)
    
    # 3. Guna ratios
    ax3 = axes[2]
    guna_names = ['Sattva\n(सत्त्व)', 'Rajas\n(रजस्)', 'Tamas\n(तमस्)']
    guna_values = [gunas['sattva'], gunas['rajas'], gunas['tamas']]
    guna_colors = ['white', 'red', 'black']
    
    bars = ax3.bar(guna_names, guna_values, color=guna_colors, edgecolor='gray', linewidth=2)
    ax3.set_title(f'Guna Composition: {sound_char}', fontsize=14)
    ax3.set_ylabel('Ratio')
    ax3.set_ylim(0, 1)
    
    # Add value labels
    for bar, val in zip(bars, guna_values):
        ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                f'{val:.2f}', ha='center', fontsize=12)
    
    # Add S+R+T=1 annotation
    ax3.text(0.5, 0.9, f'S + R + T = {sum(guna_values):.2f}',
             transform=ax3.transAxes, ha='center', fontsize=12,
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filename = os.path.join(output_dir, f'grid_81_{sound_char}.png')
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✅ Saved: {filename}")


def visualize_om_components(output_dir='sound_visuals'):
    """Visualize OM as A-U-M components in 3D."""
    fig = plt.figure(figsize=(16, 12))
    
    components = [
        ('अ (A)', 1.0, 'Creation/Brahma'),
        ('उ (U)', 0.8, 'Preservation/Vishnu'),
        ('म (M)', 0.9, 'Dissolution/Shiva'),
    ]
    
    for idx, (name, ratio, meaning) in enumerate(components):
        ax = fig.add_subplot(2, 2, idx + 1, projection='3d')
        
        X, Y, Z = generate_chladni_pattern(ratio, grid_size=60)
        surf = ax.plot_surface(X, Y, Z, cmap=['Reds', 'Blues', 'Greens'][idx],
                              alpha=0.8, linewidth=0)
        
        ax.set_title(f'{name}\n{meaning}\nFreq: {ratio * OM_BASE_FREQ:.1f} Hz', fontsize=12)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Amplitude')
    
    # 4th subplot: Combined OM
    ax4 = fig.add_subplot(2, 2, 4, projection='3d')
    
    # Combine all three patterns
    X, Y, Z_a = generate_chladni_pattern(1.0, grid_size=60)
    _, _, Z_u = generate_chladni_pattern(0.8, grid_size=60)
    _, _, Z_m = generate_chladni_pattern(0.9, grid_size=60)
    Z_om = Z_a * 0.4 + Z_u * 0.3 + Z_m * 0.3
    
    surf = ax4.plot_surface(X, Y, Z_om, cmap='viridis', alpha=0.8, linewidth=0)
    ax4.set_title('ॐ (OM) Combined\nA + U + M = Complete', fontsize=12)
    ax4.set_xlabel('X')
    ax4.set_ylabel('Y')
    ax4.set_zlabel('Amplitude')
    
    plt.tight_layout()
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filename = os.path.join(output_dir, 'om_3d_components.png')
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✅ Saved: {filename}")


def visualize_sound_helix(sound_char, freq_ratio, output_dir='sound_visuals'):
    """Visualize sound as 3D helix (like DNA/Kundalini)."""
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Generate helix
    t = np.linspace(0, 4 * np.pi, 500)
    freq = freq_ratio
    
    # Main helix (like Sushumna)
    x = t
    y = np.sin(freq * t)
    z = np.cos(freq * t)
    ax.plot(x, y, z, 'b-', linewidth=2, label='Main Wave (Sushumna)')
    
    # Secondary helix (like Ida)
    y2 = np.sin(freq * t + np.pi/2) * 0.8
    z2 = np.cos(freq * t + np.pi/2) * 0.8
    ax.plot(x, y2, z2, 'silver', linewidth=1.5, alpha=0.7, label='Ida (Moon)')
    
    # Tertiary helix (like Pingala)
    y3 = np.sin(freq * t - np.pi/2) * 0.8
    z3 = np.cos(freq * t - np.pi/2) * 0.8
    ax.plot(x, y3, z3, 'gold', linewidth=1.5, alpha=0.7, label='Pingala (Sun)')
    
    # Mark chakra points (7 crossings)
    chakra_points = np.linspace(0, 4 * np.pi, 8)[:-1]
    chakra_colors = list(CHAKRA_COLORS.values())
    chakra_names = ['Muladhara', 'Svadhisthana', 'Manipura', 'Anahata', 
                   'Vishuddha', 'Ajna', 'Sahasrara']
    
    for i, (cp, color, name) in enumerate(zip(chakra_points, chakra_colors, chakra_names)):
        ax.scatter(cp, np.sin(freq * cp), np.cos(freq * cp),
                  c=color, s=100, marker='o', edgecolor='black')
    
    ax.set_title(f'Sound Helix: {sound_char}\n'
                f'Frequency: {freq_ratio * OM_BASE_FREQ:.1f} Hz\n'
                f'(Ida-Pingala-Sushumna Pattern)', fontsize=14)
    ax.set_xlabel('Time/Space')
    ax.set_ylabel('Y Amplitude')
    ax.set_zlabel('Z Amplitude')
    ax.legend(loc='upper right')
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filename = os.path.join(output_dir, f'helix_3d_{sound_char}.png')
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✅ Saved: {filename}")


def create_interactive_3d(sound_char, freq_ratio, output_dir='sound_visuals'):
    """Create interactive 3D visualization using Plotly."""
    if not PLOTLY_AVAILABLE:
        print("⚠️ Plotly not available. Install with: pip install plotly")
        return
    
    X, Y, Z = generate_chladni_pattern(freq_ratio, grid_size=80)
    
    fig = go.Figure(data=[
        go.Surface(x=X, y=Y, z=Z, colorscale='Viridis', opacity=0.9)
    ])
    
    fig.update_layout(
        title=f'Interactive 3D Cymatic: {sound_char}<br>'
              f'Frequency: {freq_ratio * OM_BASE_FREQ:.1f} Hz ({freq_ratio}x OM)',
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Amplitude',
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))
        ),
        width=900,
        height=700,
    )
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filename = os.path.join(output_dir, f'interactive_3d_{sound_char}.html')
    fig.write_html(filename)
    print(f"✅ Saved interactive: {filename}")


# =============================================================================
# LEARNING IMPACT ANALYSIS
# =============================================================================

def analyze_learning_impact():
    """
    Analyze how visualization affects learning rate.
    
    Based on cognitive science and Vedic principles.
    """
    analysis = """
    ╔════════════════════════════════════════════════════════════════════╗
    ║     DOES VISUALIZATION HELP OR HURT LEARNING?                      ║
    ╠════════════════════════════════════════════════════════════════════╣
    ║                                                                    ║
    ║  VEDIC PERSPECTIVE:                                                ║
    ║  ──────────────────                                                ║
    ║  • शब्द → रूप (Sound creates Form) - Visualization is NATURAL     ║
    ║  • त्रिविध-ग्रहण (3 modes of learning):                            ║
    ║    1. श्रवण (Shravana) - Hearing                                  ║
    ║    2. मनन (Manana) - Contemplation                                ║
    ║    3. निदिध्यासन (Nididhyasana) - Deep Meditation                 ║
    ║  • Visualization BRIDGES श्रवण and मनन                            ║
    ║                                                                    ║
    ║  COGNITIVE SCIENCE EVIDENCE:                                       ║
    ║  ───────────────────────────                                       ║
    ║  • Dual Coding Theory: Visual + Auditory = 2x retention           ║
    ║  • 65% of people are visual learners                              ║
    ║  • Pictures processed 60,000x faster than text                    ║
    ║  • Spatial memory is stronger than verbal memory                  ║
    ║                                                                    ║
    ║  WHEN VISUALIZATION HELPS:                                         ║
    ║  ──────────────────────────                                        ║
    ║  ✅ Initial learning - Understanding the FORM of mantras          ║
    ║  ✅ Memory encoding - Associating sound with image                ║
    ║  ✅ Pattern recognition - Seeing 81-grid structure                ║
    ║  ✅ Motivation - Beautiful forms inspire practice                 ║
    ║  ✅ Teaching - Explaining to others                               ║
    ║                                                                    ║
    ║  WHEN VISUALIZATION HURTS:                                         ║
    ║  ──────────────────────────                                        ║
    ║  ❌ Deep meditation - Eyes should be closed                       ║
    ║  ❌ Over-reliance - Sound must be PRIMARY                         ║
    ║  ❌ Distraction - If images become entertainment                  ║
    ║  ❌ Advanced stages - Pure sound transcends form                  ║
    ║                                                                    ║
    ║  OPTIMAL APPROACH:                                                 ║
    ║  ─────────────────                                                 ║
    ║  1. START with visualization (learn the pattern)                  ║
    ║  2. PRACTICE with sound + visualization together                  ║
    ║  3. INTERNALIZE until you "see" without looking                   ║
    ║  4. TRANSCEND to pure sound (eyes closed)                         ║
    ║  5. ULTIMATE: Neither sound nor form - pure awareness             ║
    ║                                                                    ║
    ║  FORMULA:                                                          ║
    ║  ─────────                                                         ║
    ║  Learning_Rate = Base_Rate × (1 + Visual_Factor) × Attention      ║
    ║                                                                    ║
    ║  Where:                                                            ║
    ║  • Visual_Factor = 0.3 to 0.8 (30-80% boost)                      ║
    ║  • Attention = Quality of focus                                   ║
    ║  • But: After mastery, reduce Visual_Factor to 0                  ║
    ║                                                                    ║
    ║  CONCLUSION:                                                       ║
    ║  ───────────                                                       ║
    ║  Visualization ACCELERATES initial learning by 30-80%             ║
    ║  But must be TRANSCENDED for highest realization                  ║
    ║  Use as SCAFFOLD, not as final destination                        ║
    ║                                                                    ║
    ╚════════════════════════════════════════════════════════════════════╝
    """
    return analysis


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Generate all visualizations."""
    
    print("=" * 70)
    print("🌀 त्रिमितीय-ध्वनि-दृश्य — 3D Sound Wave Visualization")
    print("=" * 70)
    print()
    
    output_dir = 'sound_visuals'
    
    # 1. Generate OM components
    print("📊 Generating OM components visualization...")
    visualize_om_components(output_dir)
    
    # 2. Generate vowel visualizations
    print("\n📊 Generating vowel cymatics...")
    for vowel, ratio in VOWEL_RATIOS.items():
        print(f"  Processing {vowel} (ratio: {ratio})...")
        
        # 2D cymatic
        Z = visualize_cymatic_2d(vowel, ratio, output_dir)
        
        # 3D cymatic
        visualize_cymatic_3d(vowel, ratio, output_dir)
        
        # Sound helix
        visualize_sound_helix(vowel, ratio, output_dir)
        
        # 81-grid projection
        X, Y, Z_full = generate_chladni_pattern(ratio, grid_size=81)
        grid_81 = project_to_81_grid(X, Y, Z_full)
        zones = classify_81_grid(grid_81)
        gunas = compute_guna_ratios(zones)
        visualize_81_grid(vowel, grid_81, zones, gunas, output_dir)
        
        # Interactive 3D (if plotly available)
        create_interactive_3d(vowel, ratio, output_dir)
    
    # 3. Print learning impact analysis
    print("\n" + "=" * 70)
    print(analyze_learning_impact())
    
    print("\n" + "=" * 70)
    print(f"✅ All visualizations saved to '{output_dir}/' directory")
    print("=" * 70)
    print("\n🙏 ॐ रूपाय नमः — May Form reveal Sound")


if __name__ == "__main__":
    main()

