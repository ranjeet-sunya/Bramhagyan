#!/usr/bin/env python3
"""
☀️ सौर-अनुकूलक — Solar Panel Optimizer
========================================

Calculate optimal solar panel configuration for maximum efficiency.

> "सूर्यो विश्वस्य भुवनस्य गोप्ता"
> "Suryo Vishvasya Bhuvanasya Gopta"
> "The Sun is the protector of the entire world."
> — Rig Veda

Usage:
    python solar_optimizer.py [latitude]

Requirements:
    pip install numpy

Author: Shunya-0 Project
License: Open for Dharmic and Environmental Use
"""

import numpy as np
import sys
from datetime import datetime, timedelta
import math

# =============================================================================
# SOLAR CONSTANTS
# =============================================================================

SOLAR_CONSTANT = 1361  # W/m² (solar irradiance at Earth's distance)

# Panel efficiency by technology
PANEL_EFFICIENCY = {
    'monocrystalline': 0.20,      # 20%
    'polycrystalline': 0.17,       # 17%
    'thin_film_cigs': 0.15,        # 15%
    'thin_film_cdte': 0.14,        # 14%
    'perovskite': 0.25,            # 25% (emerging)
    'perovskite_silicon': 0.30,    # 30% (hybrid, emerging)
    'quantum_dot': 0.35,           # 35% (research)
}

# Temperature coefficient (% loss per °C above 25°C)
TEMP_COEFFICIENT = {
    'monocrystalline': -0.004,     # -0.4%/°C
    'polycrystalline': -0.005,     # -0.5%/°C
    'thin_film': -0.002,           # -0.2%/°C
}

# =============================================================================
# SOLAR CALCULATIONS
# =============================================================================

def calculate_solar_declination(day_of_year):
    """
    Calculate solar declination angle.
    
    The Sun's position varies throughout the year.
    This determines the optimal tilt angle.
    """
    # Declination angle in degrees
    declination = 23.45 * np.sin(np.radians(360 * (284 + day_of_year) / 365))
    return declination


def calculate_optimal_tilt(latitude, day_of_year=None):
    """
    Calculate optimal tilt angle for solar panels.
    
    For fixed panels:
    - Annual optimal: latitude angle
    - Summer: latitude - 15°
    - Winter: latitude + 15°
    """
    if day_of_year is None:
        # Annual average
        return abs(latitude)
    
    declination = calculate_solar_declination(day_of_year)
    
    # Optimal tilt = latitude - declination
    optimal_tilt = abs(latitude) - declination
    
    # Clamp to reasonable range
    optimal_tilt = max(0, min(90, optimal_tilt))
    
    return optimal_tilt


def calculate_solar_hours(latitude, day_of_year):
    """Calculate hours of sunlight for a given day."""
    declination = np.radians(calculate_solar_declination(day_of_year))
    latitude_rad = np.radians(latitude)
    
    # Hour angle at sunrise/sunset
    try:
        hour_angle = np.arccos(-np.tan(latitude_rad) * np.tan(declination))
        daylight_hours = 2 * np.degrees(hour_angle) / 15
    except:
        # Polar regions edge case
        if latitude > 66.5:
            daylight_hours = 24 if day_of_year > 80 and day_of_year < 265 else 0
        elif latitude < -66.5:
            daylight_hours = 0 if day_of_year > 80 and day_of_year < 265 else 24
        else:
            daylight_hours = 12
    
    return daylight_hours


def calculate_peak_sun_hours(latitude, day_of_year, cloud_factor=0.8):
    """
    Calculate Peak Sun Hours (PSH).
    
    PSH = Equivalent hours of 1000 W/m² irradiance.
    Actual energy = Panel_Watts × PSH
    """
    daylight = calculate_solar_hours(latitude, day_of_year)
    
    # Peak sun is typically 4-6 hours even in 12-hour days
    # due to low angle at morning/evening
    
    # Simplified model: Peak = daylight × efficiency factor × cloud factor
    efficiency_factor = 0.5  # Morning/evening angles reduce effective sunlight
    peak_sun_hours = daylight * efficiency_factor * cloud_factor
    
    return peak_sun_hours


def calculate_solar_irradiance(latitude, day_of_year, hour):
    """
    Calculate solar irradiance at a specific time.
    
    Returns W/m² on a horizontal surface.
    """
    declination = np.radians(calculate_solar_declination(day_of_year))
    latitude_rad = np.radians(latitude)
    
    # Hour angle (solar noon = 0)
    hour_angle = np.radians(15 * (hour - 12))
    
    # Solar altitude angle
    sin_altitude = (np.sin(latitude_rad) * np.sin(declination) +
                   np.cos(latitude_rad) * np.cos(declination) * np.cos(hour_angle))
    
    if sin_altitude <= 0:
        return 0  # Sun below horizon
    
    # Air mass correction
    altitude = np.arcsin(sin_altitude)
    air_mass = 1 / sin_altitude if sin_altitude > 0.01 else 100
    
    # Simplified atmospheric transmission
    transmission = 0.7 ** (air_mass ** 0.678)
    
    irradiance = SOLAR_CONSTANT * sin_altitude * transmission
    
    return max(0, irradiance)


def calculate_panel_output(panel_watts, efficiency, temperature, 
                          irradiance, panel_type='monocrystalline'):
    """
    Calculate actual panel output considering real-world factors.
    
    Factors:
    - Irradiance level
    - Temperature derating
    - Dust/soiling (assume 3% loss)
    - Wiring losses (assume 2%)
    - Inverter efficiency (assume 95%)
    """
    # Temperature derating
    temp_coeff = TEMP_COEFFICIENT.get(panel_type, -0.004)
    if temperature > 25:
        temp_factor = 1 + temp_coeff * (temperature - 25)
    else:
        temp_factor = 1
    
    # Standard test conditions: 1000 W/m²
    irradiance_factor = irradiance / 1000
    
    # Derating factors
    dust_factor = 0.97       # 3% loss
    wiring_factor = 0.98     # 2% loss
    inverter_factor = 0.95   # 5% loss
    
    total_factor = temp_factor * irradiance_factor * dust_factor * wiring_factor * inverter_factor
    
    actual_output = panel_watts * total_factor
    
    return max(0, actual_output)


def calculate_daily_energy(latitude, panel_watts, panel_type='monocrystalline',
                          day_of_year=None, temperature=30, cloud_factor=0.8):
    """
    Calculate total daily energy production (Wh).
    """
    if day_of_year is None:
        day_of_year = datetime.now().timetuple().tm_yday
    
    efficiency = PANEL_EFFICIENCY.get(panel_type, 0.18)
    total_energy = 0
    
    for hour in range(5, 20):  # 5 AM to 8 PM
        irradiance = calculate_solar_irradiance(latitude, day_of_year, hour)
        irradiance *= cloud_factor
        
        output = calculate_panel_output(panel_watts, efficiency, temperature, 
                                        irradiance, panel_type)
        total_energy += output  # Each hour = 1 Wh per W
    
    return total_energy


def calculate_annual_energy(latitude, panel_watts, panel_type='monocrystalline',
                           avg_temperature=30, cloud_factor=0.8):
    """Calculate total annual energy production (kWh)."""
    total = 0
    for day in range(1, 366):
        daily = calculate_daily_energy(latitude, panel_watts, panel_type,
                                       day, avg_temperature, cloud_factor)
        total += daily
    return total / 1000  # Convert to kWh


# =============================================================================
# BATTERY SIZING
# =============================================================================

def calculate_battery_size(daily_consumption_kwh, backup_days=1, 
                          depth_of_discharge=0.8, system_voltage=48):
    """
    Calculate required battery capacity.
    
    Args:
        daily_consumption_kwh: Average daily energy consumption
        backup_days: Days of backup without sun
        depth_of_discharge: How much battery can be used (0.8 = 80%)
        system_voltage: Battery system voltage
    
    Returns:
        Battery capacity in Ah and kWh
    """
    # Total energy needed
    energy_needed = daily_consumption_kwh * backup_days
    
    # Account for DoD
    usable_capacity = energy_needed / depth_of_discharge
    
    # Convert to Ah
    capacity_ah = (usable_capacity * 1000) / system_voltage
    
    return {
        'capacity_kwh': usable_capacity,
        'capacity_ah': capacity_ah,
        'voltage': system_voltage
    }


def calculate_payback_period(system_cost, annual_savings, annual_degradation=0.5):
    """
    Calculate payback period for solar investment.
    
    Args:
        system_cost: Total installation cost
        annual_savings: Yearly electricity bill savings
        annual_degradation: Panel efficiency loss per year (%)
    """
    if annual_savings <= 0:
        return float('inf')
    
    cumulative_savings = 0
    year = 0
    degradation_factor = 1.0
    
    while cumulative_savings < system_cost and year < 50:
        year += 1
        cumulative_savings += annual_savings * degradation_factor
        degradation_factor *= (1 - annual_degradation / 100)
    
    return year


# =============================================================================
# OPTIMIZATION RECOMMENDATIONS
# =============================================================================

def get_optimization_recommendations(latitude, current_tilt=None, 
                                     current_azimuth=None):
    """Generate optimization recommendations."""
    recommendations = []
    
    optimal_annual_tilt = calculate_optimal_tilt(latitude)
    
    recommendations.append({
        'category': 'TILT ANGLE',
        'title': 'Optimal Annual Tilt',
        'value': f'{optimal_annual_tilt:.1f}°',
        'detail': 'For fixed panels, set tilt equal to your latitude'
    })
    
    # Seasonal tilts
    summer_tilt = calculate_optimal_tilt(latitude, 172)  # June 21
    winter_tilt = calculate_optimal_tilt(latitude, 355)  # Dec 21
    
    recommendations.append({
        'category': 'SEASONAL ADJUSTMENT',
        'title': 'Summer Tilt (if adjustable)',
        'value': f'{summer_tilt:.1f}°',
        'detail': 'Reduce tilt in summer for higher sun'
    })
    
    recommendations.append({
        'category': 'SEASONAL ADJUSTMENT',
        'title': 'Winter Tilt (if adjustable)',
        'value': f'{winter_tilt:.1f}°',
        'detail': 'Increase tilt in winter for lower sun'
    })
    
    recommendations.append({
        'category': 'AZIMUTH',
        'title': 'Optimal Orientation',
        'value': '180° (True South)' if latitude > 0 else '0° (True North)',
        'detail': 'Face panels toward the equator'
    })
    
    recommendations.append({
        'category': 'TRACKING',
        'title': 'Single-axis Tracking',
        'value': '+25-35% energy',
        'detail': 'East-West tracking throughout day'
    })
    
    recommendations.append({
        'category': 'TRACKING',
        'title': 'Dual-axis Tracking',
        'value': '+35-45% energy',
        'detail': 'Follows sun in both axes (more expensive)'
    })
    
    recommendations.append({
        'category': 'BIFACIAL PANELS',
        'title': 'Bifacial Installation',
        'value': '+10-30% energy',
        'detail': 'Collect reflected light from ground'
    })
    
    recommendations.append({
        'category': 'COOLING',
        'title': 'Panel Cooling',
        'value': '+5-10% energy',
        'detail': 'Water cooling or good ventilation reduces heat loss'
    })
    
    recommendations.append({
        'category': 'CLEANING',
        'title': 'Regular Cleaning',
        'value': '+3-5% energy',
        'detail': 'Clean panels monthly in dusty areas'
    })
    
    return recommendations


# =============================================================================
# MAIN ANALYSIS
# =============================================================================

def analyze_solar_potential(latitude, panel_watts=400, num_panels=10,
                           panel_type='monocrystalline', 
                           avg_temperature=30, cloud_factor=0.8):
    """Complete solar potential analysis."""
    
    print("=" * 70)
    print("☀️ SOLAR POTENTIAL ANALYSIS")
    print("=" * 70)
    print(f"\nLocation: {abs(latitude)}° {'N' if latitude > 0 else 'S'}")
    print(f"System: {num_panels} × {panel_watts}W = {num_panels * panel_watts / 1000:.1f} kW")
    print(f"Panel Type: {panel_type}")
    print(f"Average Temperature: {avg_temperature}°C")
    print(f"Cloud Factor: {cloud_factor * 100:.0f}%")
    
    # Optimal angles
    print("\n📐 OPTIMAL ANGLES")
    print("-" * 40)
    
    annual_tilt = calculate_optimal_tilt(latitude)
    print(f"Annual Optimal Tilt: {annual_tilt:.1f}°")
    
    summer_tilt = calculate_optimal_tilt(latitude, 172)
    print(f"Summer Optimal Tilt: {summer_tilt:.1f}°")
    
    winter_tilt = calculate_optimal_tilt(latitude, 355)
    print(f"Winter Optimal Tilt: {winter_tilt:.1f}°")
    
    # Energy production
    print("\n⚡ ENERGY PRODUCTION")
    print("-" * 40)
    
    total_watts = panel_watts * num_panels
    
    # Summer day (June 21)
    summer_daily = calculate_daily_energy(latitude, total_watts, panel_type,
                                         172, avg_temperature, cloud_factor)
    print(f"Best Summer Day: {summer_daily / 1000:.2f} kWh")
    
    # Winter day (Dec 21)
    winter_daily = calculate_daily_energy(latitude, total_watts, panel_type,
                                         355, avg_temperature, cloud_factor)
    print(f"Worst Winter Day: {winter_daily / 1000:.2f} kWh")
    
    # Annual
    annual = calculate_annual_energy(latitude, total_watts, panel_type,
                                    avg_temperature, cloud_factor)
    print(f"Annual Production: {annual:.0f} kWh")
    print(f"Daily Average: {annual / 365:.2f} kWh")
    
    # Peak sun hours
    print("\n🌞 PEAK SUN HOURS")
    print("-" * 40)
    
    summer_psh = calculate_peak_sun_hours(latitude, 172, cloud_factor)
    winter_psh = calculate_peak_sun_hours(latitude, 355, cloud_factor)
    avg_psh = (summer_psh + winter_psh) / 2
    
    print(f"Summer Peak Sun Hours: {summer_psh:.1f} hours")
    print(f"Winter Peak Sun Hours: {winter_psh:.1f} hours")
    print(f"Average Peak Sun Hours: {avg_psh:.1f} hours")
    
    # Efficiency analysis
    print("\n📊 EFFICIENCY COMPARISON")
    print("-" * 40)
    print(f"{'Technology':<25} {'Efficiency':>10} {'Annual kWh':>12}")
    print("-" * 47)
    
    for tech, eff in sorted(PANEL_EFFICIENCY.items(), key=lambda x: -x[1]):
        tech_annual = calculate_annual_energy(latitude, total_watts * (eff / 0.20),
                                             'monocrystalline', avg_temperature, cloud_factor)
        print(f"{tech:<25} {eff*100:>9.0f}% {tech_annual:>12,.0f}")
    
    # Recommendations
    print("\n💡 OPTIMIZATION RECOMMENDATIONS")
    print("-" * 40)
    
    recs = get_optimization_recommendations(latitude)
    for rec in recs:
        print(f"\n{rec['category']}: {rec['title']}")
        print(f"  Value: {rec['value']}")
        print(f"  Note: {rec['detail']}")
    
    # Battery sizing example
    print("\n🔋 BATTERY SIZING (Example: 10 kWh/day consumption)")
    print("-" * 40)
    
    battery = calculate_battery_size(10, backup_days=1)
    print(f"Recommended Capacity: {battery['capacity_kwh']:.1f} kWh")
    print(f"At {battery['voltage']}V: {battery['capacity_ah']:.0f} Ah")
    
    # ROI
    print("\n💰 RETURN ON INVESTMENT (Example)")
    print("-" * 40)
    
    system_cost = num_panels * panel_watts * 1.5  # $1.5 per watt installed
    electricity_rate = 0.12  # $/kWh
    annual_savings = annual * electricity_rate
    payback = calculate_payback_period(system_cost, annual_savings)
    
    print(f"Estimated System Cost: ${system_cost:,.0f}")
    print(f"Annual Savings (at $0.12/kWh): ${annual_savings:,.0f}")
    print(f"Payback Period: {payback:.1f} years")
    
    print("\n" + "=" * 70)
    print("🙏 ॐ सूर्याय नमः — Salutations to the Sun")
    print("=" * 70)


def main():
    # Default: New Delhi latitude
    latitude = 28.6
    
    if len(sys.argv) >= 2:
        try:
            latitude = float(sys.argv[1])
        except:
            print(f"Invalid latitude: {sys.argv[1]}")
            print("Usage: python solar_optimizer.py [latitude]")
            print("Example: python solar_optimizer.py 28.6")
            return
    
    analyze_solar_potential(latitude)


if __name__ == "__main__":
    main()

