# 💻 SRC — Simulation Source Code

> *"The running implementation of the engine."*

---

## 📁 Structure

```
src/
├── main/
│   ├── java/com/shunya/       ← Java implementation
│   │   ├── core/                Constants, Guna, FractalNode
│   │   ├── entities/            Jiva, Level
│   │   └── simulation/          RealityCalculator, Simulation
│   │
│   ├── python/                ← Visualization tools
│   │   ├── individual_pralaya_calculator.py
│   │   ├── rendering_visualization.py
│   │   ├── sound_3d_visualization.py
│   │   └── vedic_sound_synthesis.py
│   │
│   └── resources/levels/      ← JSON configurations
│       ├── N_MINUS_6_QUANTUM.json
│       ├── ... (13 levels)
│       └── N_PLUS_6_BRAHMAN.json
│
└── test/java/                 ← Test cases
```

---

## ☕ Java Classes

| Class | Package | Purpose |
|-------|---------|---------|
| `Constants` | core | Universal constants |
| `Guna` | core | Three qualities + activation |
| `FractalNode` | core | Base entity class |
| `Level` | entities | 13 fractal levels enum |
| `Jiva` | entities | Conscious entity |
| `RealityCalculator` | simulation | Time dilation, age, sync |
| `Simulation` | simulation | Main orchestrator |

---

## 📊 JSON Configs

13 level configurations (N-6 to N+6):

| Level | File | Scale |
|-------|------|-------|
| N-6 | `N_MINUS_6_QUANTUM.json` | 10⁻³⁵ m |
| N | `N_HUMAN.json` | 1 m |
| N+6 | `N_PLUS_6_BRAHMAN.json` | ∞ |

---

## 🐍 Python Tools

| Script | Purpose |
|--------|---------|
| `individual_pralaya_calculator.py` | Personal time analysis |
| `rendering_visualization.py` | Visual output |
| `sound_3d_visualization.py` | Sound visualization |
| `vedic_sound_synthesis.py` | Sound generation |

---

**[← Back to Engine](../README.md)**

