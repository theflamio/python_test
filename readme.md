# Flames of War Combat Calculator (Binomial Chain)

A Streamlit-based probabilistic combat simulator for tabletop wargaming, designed for Flames of War-style mechanics.  
It models combat using a simplified hit → save → firepower (kill) probability chain and Monte Carlo simulation.

---

## Features

- Simulates combat outcomes based on:
  - Number of shots
  - To Hit value (2+ to 6+)
  - Save/Armor value (1+ to 6+)
  - Firepower value (1+ to 6+)
- Monte Carlo simulation (50,000 trials)
- Visual probability distributions for:
  - Hits
  - Kills
- Key tactical statistics:
  - Expected hits and kills
  - Chance of threshold outcomes (e.g. 5+ hits, 8+ hits, 2+ kills, 5+ kills)

---

## Combat Model

The simulation follows this sequence:

1. Hit Roll  
   Each shot is resolved with a probability based on the To Hit value.

2. Save Roll  
   Successful hits may be negated by armor or save rolls.

3. Firepower Roll  
   Remaining unsaved hits are tested for kills.

Final kills are computed using Monte Carlo sampling.

---
