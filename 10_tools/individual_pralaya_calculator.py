#!/usr/bin/env python3
"""
Individual Pralaya Calculator (व्यक्तिगत-प्रलय-गणक)
=====================================================

> "कालः पचति भूतानि कालः संहरते प्रजाः"
> "Kalah pachati bhutani kalah samharate prajah"
> "Time devours all beings, Time destroys all creatures."
> — Mahabharata, Vana Parva 313.117

This calculator helps you determine:
1. Your current Guna composition (S/R/T)
2. Your Temporal Expansion factor (L_m)
3. Your effective time remaining
4. Your sync status with cosmic Kala
5. Recommendations for Guna correction

FORMULA (Validated ✅):
L_m = (D × S) / (R + 2T)

WHERE:
D = Dharma-Unit of Yuga (Current: ~1.5 for Kali-Dvapara Sandhya)
S = Sattva (0.0 to 1.0)
R = Rajas (0.0 to 1.0)
T = Tamas (0.0 to 1.0)
S + R + T = 1.0 (Conservation law)

Author: Project Shunya-0
License: Free for all (No patents, No profit)
"""

import sys
from typing import Dict, Tuple
from datetime import datetime

# Constants
CURRENT_YUGA_D = 1.5  # Kali-Dvapara Sandhya (2023-2028)
KALI_BASELINE_LM = 0.07  # Average Kali Yuga L_m
OPTIMAL_LM = 6.4  # Target L_m with optimized Gunas
FULL_DVAPARA_D = 2.0  # Full Dvapara (post-2028)


def print_header():
    """Print calculator header"""
    print("\n" + "="*80)
    print("  ⏰ INDIVIDUAL PRALAYA CALCULATOR — व्यक्तिगत-प्रलय-गणक")
    print("="*80)
    print("\n> 'Time is not linear — it is frequency-dependent.'")
    print("> 'Your subjective time experience depends on your Guna composition.'\n")


def assess_gunas() -> Dict[str, float]:
    """
    Interactive Guna assessment questionnaire
    Returns normalized S, R, T values
    """
    print("\n" + "-"*80)
    print("  STEP 1: GUNA ASSESSMENT (गुण-परीक्षण)")
    print("-"*80)
    print("\nAnswer the following questions honestly (1-5 scale):")
    print("1 = Never/Rarely, 3 = Sometimes, 5 = Often/Always\n")
    
    # Sattva questions
    print("SATTVA (सत्त्व) — Purity, Clarity, Light")
    print("-" * 40)
    s1 = get_rating("Do you wake up before sunrise naturally?")
    s2 = get_rating("Do you meditate or pray daily?")
    s3 = get_rating("Is your diet primarily fresh/vegetarian?")
    s4 = get_rating("Do you feel calm and clear-minded?")
    s5 = get_rating("Do you engage in selfless service (Seva)?")
    
    sattva_score = (s1 + s2 + s3 + s4 + s5) / 25.0  # Normalize to 0-1
    
    # Rajas questions
    print("\nRAJAS (रजस्) — Activity, Passion, Restlessness")
    print("-" * 40)
    r1 = get_rating("Are you constantly busy/active?")
    r2 = get_rating("Do you feel anxious or restless often?")
    r3 = get_rating("Is your focus on achievement/ambition?")
    r4 = get_rating("Do you consume stimulants (caffeine, etc.)?")
    r5 = get_rating("Do you multitask frequently?")
    
    rajas_score = (r1 + r2 + r3 + r4 + r5) / 25.0
    
    # Tamas questions
    print("\nTAMAS (तमस्) — Inertia, Darkness, Confusion")
    print("-" * 40)
    t1 = get_rating("Do you sleep late/wake up late?")
    t2 = get_rating("Do you feel lazy or lethargic often?")
    t3 = get_rating("Do you consume heavy/processed foods?")
    t4 = get_rating("Do you avoid responsibilities/difficult tasks?")
    t5 = get_rating("Do you spend excessive time on entertainment?")
    
    tamas_score = (t1 + t2 + t3 + t4 + t5) / 25.0
    
    # Normalize to sum = 1.0
    total = sattva_score + rajas_score + tamas_score
    if total == 0:
        total = 1.0  # Avoid division by zero
    
    return {
        'S': sattva_score / total,
        'R': rajas_score / total,
        'T': tamas_score / total
    }


def get_rating(question: str) -> int:
    """Get 1-5 rating from user"""
    while True:
        try:
            response = input(f"  {question} (1-5): ").strip()
            rating = int(response)
            if 1 <= rating <= 5:
                return rating
            else:
                print("  ⚠️  Please enter a number between 1 and 5")
        except ValueError:
            print("  ⚠️  Please enter a valid number")


def calculate_temporal_expansion(S: float, R: float, T: float, D: float = CURRENT_YUGA_D) -> float:
    """
    Calculate L_m (Temporal Expansion factor)
    
    Formula: L_m = (D × S) / (R + 2T)
    """
    denominator = R + (2 * T)
    if denominator == 0:
        denominator = 0.001  # Avoid division by zero
    
    L_m = (D * S) / denominator
    return L_m


def calculate_sync_status(S: float, R: float, T: float, D_yuga: float = 0.5) -> float:
    """
    Calculate Sync Status with cosmic Kala
    
    Formula: Sync_Status = (S × D_yuga) / (R + T)
    """
    denominator = R + T
    if denominator == 0:
        denominator = 0.001
    
    sync = (S * D_yuga) / denominator
    return sync


def calculate_time_remaining(current_age: int, L_m: float, baseline_lm: float = KALI_BASELINE_LM) -> Tuple[int, int, int]:
    """
    Calculate effective time remaining
    
    Formula (Corrected): Life_Value = Years × L_m
    
    Returns: (chronological_years, experiential_years, baseline_experiential)
    """
    expected_lifespan = 100  # Kali Yuga average
    chronological_remaining = expected_lifespan - current_age
    
    if chronological_remaining <= 0:
        return 0, 0, 0
    
    # Corrected formula: Direct multiplication by L_m
    experiential_remaining = int(chronological_remaining * L_m)
    
    # For comparison: what average person gets
    baseline_experiential = int(chronological_remaining * baseline_lm)
    
    return chronological_remaining, experiential_remaining, baseline_experiential


def print_results(gunas: Dict[str, float], age: int):
    """Print detailed results and recommendations"""
    S, R, T = gunas['S'], gunas['R'], gunas['T']
    
    # Calculate metrics
    L_m = calculate_temporal_expansion(S, R, T)
    sync_status = calculate_sync_status(S, R, T)
    chrono_time, exp_time, baseline_exp = calculate_time_remaining(age, L_m)
    
    print("\n" + "="*80)
    print("  RESULTS — परिणाम")
    print("="*80)
    
    # Guna composition
    print("\n1. YOUR GUNA COMPOSITION (गुण-संयोजन):")
    print(f"   Sattva (सत्त्व): {S:.2f} ({S*100:.0f}%)")
    print(f"   Rajas (रजस्):  {R:.2f} ({R*100:.0f}%)")
    print(f"   Tamas (तमस्):  {T:.2f} ({T*100:.0f}%)")
    print(f"   Total:         {S+R+T:.2f} ✅" if abs((S+R+T)-1.0) < 0.01 else f"   Total:         {S+R+T:.2f} ❌")
    
    # Temporal expansion
    print(f"\n2. TEMPORAL EXPANSION FACTOR (L_m): {L_m:.2f}")
    if L_m < 0.5:
        print("   ⚠️  CRITICAL: Time is highly compressed. Life feels 'rushed'.")
    elif L_m < 1.0:
        print("   ⚠️  WARNING: Time is compressed. Life feels 'busy'.")
    elif L_m < 2.0:
        print("   ✅ MODERATE: Balanced time perception.")
    else:
        print("   ✅ EXCELLENT: Time feels spacious and expanded.")
    
    print(f"   Comparison: You experience {L_m/KALI_BASELINE_LM:.1f}x MORE depth than average Kali person.")
    
    # Time remaining
    print(f"\n3. TIME REMAINING (शेष-काल):")
    print(f"   Chronological: {chrono_time} years")
    print(f"   Experiential (YOU):  {exp_time} quality years")
    print(f"   Experiential (Average Kali):  {baseline_exp} quality years")
    
    if exp_time > baseline_exp:
        multiplier = exp_time / baseline_exp if baseline_exp > 0 else 0
        print(f"   ✅ GOOD: You get {multiplier:.1f}x MORE experiential depth than average!")
    elif exp_time < baseline_exp:
        ratio = baseline_exp / exp_time if exp_time > 0 else 0
        print(f"   ⚠️  WARNING: Average person gets {ratio:.1f}x more depth than you!")
    else:
        print(f"   ⚠️  You're at Kali average (very low quality)")
    
    # Sync status
    print(f"\n4. SYNC STATUS WITH COSMIC KALA: {sync_status:.2f}")
    if sync_status < 0.5:
        print("   🚨 CRITICAL — Desynchronized! Individual Pralaya risk is HIGH.")
        print("   Symptoms: Chronic stress, anxiety, accelerated aging.")
    elif sync_status < 1.0:
        print("   ⚠️  WARNING — Partially synced. Gradual decline ongoing.")
    else:
        print("   ✅ OPTIMAL — Well synchronized with cosmic time.")
    
    # Recommendations
    print("\n" + "="*80)
    print("  RECOMMENDATIONS — सिफारिशें")
    print("="*80)
    
    if S < 0.3:
        print("\n⚠️  PRIORITY 1: INCREASE SATTVA")
        print("   • Wake at Brahmamuhurta (4:30-5:30 AM)")
        print("   • Adopt Sattvic diet (fresh, vegetarian)")
        print("   • Daily meditation (20 min)")
        print("   • Pranayama (Nadi Shodhana)")
        print("   • Mantra Japa (Om/Gayatri)")
    
    if R > 0.4:
        print("\n⚠️  PRIORITY 2: REDUCE RAJAS")
        print("   • Reduce stimulants (coffee, tea)")
        print("   • Digital detox (no screens 2h before sleep)")
        print("   • Practice Nishkama Karma (desireless action)")
        print("   • Slow down daily activities")
        print("   • Cultivate Vairagya (detachment)")
    
    if T > 0.3:
        print("\n⚠️  PRIORITY 3: REDUCE TAMAS")
        print("   • Wake before 6 AM daily")
        print("   • Exercise (30 min daily)")
        print("   • Cold exposure (cold shower)")
        print("   • Avoid Tamasic food (meat, alcohol, stale)")
        print("   • Clean and organize environment")
        print("   • Engage in Seva (service)")
    
    # Target composition
    print("\n✅ TARGET GUNA COMPOSITION:")
    print("   Sattva: 0.80 (80%)")
    print("   Rajas:  0.15 (15%)")
    print("   Tamas:  0.05 (5%)")
    print(f"   This would give you L_m = {OPTIMAL_LM:.1f} (Satya-level consciousness!)")
    
    # Warning
    print("\n" + "="*80)
    print("  ⚠️  FINAL WARNING")
    print("="*80)
    print("\n  > 'Time is ticking FASTER than you think based on your Gunas.'")
    print("  > 'If you do NOT sync, individual Pralaya will come PREMATURELY.'")
    print("\n  Act NOW. The Kali-Dvapara Sandhya window (2023-2028) is closing.")
    print("\n  📖 Full guide: knowledge_core/01_foundations/")
    print("                 07_TIME_DILATION_PRALAYA_CALCULATOR.md")
    print("\n" + "="*80)


def main():
    """Main calculator flow"""
    print_header()
    
    # Get current age
    print("\nBefore we begin, what is your current age?")
    while True:
        try:
            age = int(input("  Age: ").strip())
            if 1 <= age <= 120:
                break
            else:
                print("  ⚠️  Please enter a valid age (1-120)")
        except ValueError:
            print("  ⚠️  Please enter a valid number")
    
    # Assess Gunas
    gunas = assess_gunas()
    
    # Calculate and display results
    print_results(gunas, age)
    
    # Save results option
    save = input("\nWould you like to save these results? (y/n): ").strip().lower()
    if save == 'y':
        filename = f"pralaya_calculator_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("INDIVIDUAL PRALAYA CALCULATOR RESULTS\n")
            f.write("="*80 + "\n\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Age: {age}\n\n")
            f.write(f"Guna Composition:\n")
            f.write(f"  Sattva: {gunas['S']:.2f}\n")
            f.write(f"  Rajas:  {gunas['R']:.2f}\n")
            f.write(f"  Tamas:  {gunas['T']:.2f}\n\n")
            
            L_m = calculate_temporal_expansion(gunas['S'], gunas['R'], gunas['T'])
            sync = calculate_sync_status(gunas['S'], gunas['R'], gunas['T'])
            
            f.write(f"L_m (Temporal Expansion): {L_m:.2f}\n")
            f.write(f"Sync Status: {sync:.2f}\n\n")
            f.write("See full report above for recommendations.\n")
        
        print(f"\n✅ Results saved to: {filename}")
    
    print("\n🕉️  Om Shanti Shanti Shanti 🕉️\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Calculator interrupted. Your time is still ticking!\n")
        sys.exit(0)

