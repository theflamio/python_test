import streamlit as st
import numpy as np
from math import comb

st.title("Flames of war Combat Calculator (Binomial Chain)")

# --- Helpers ---
def binom_pmf(n, k, p):
    return comb(n, k) * (p**k) * ((1-p)**(n-k))

def to_prob(label):
    return {
        "1+": 1.0,
        "2+": 5/6,
        "3+": 4/6,
        "4+": 3/6,
        "5+": 2/6,
        "6+": 1/6
    }[label]

# --- Inputs ---
shots = st.slider("Number of shots", 1, 50, 20)

to_hit = st.selectbox("To hit", ["2+", "3+", "4+", "5+", "6+"])
to_save = st.selectbox("Save (armor / bulletproof)", ["1+", "2+", "3+", "4+", "5+", "6+"])
to_fire_power = st.selectbox("Fire power", ["1+", "2+", "3+", "4+", "5+", "6+"])

p_hit = to_prob(to_hit)
p_fire_power = to_prob(to_fire_power)
p_fail_save = 1 - to_prob(to_save)

# --- Monte Carlo (simple + robust) ---
TRIALS = 50000

hits = np.random.binomial(shots, p_hit, TRIALS)
failed_saves = np.random.binomial(hits, p_fail_save)
if (to_save == "1+"):
    kills = np.zeros(TRIALS, dtype=int)
else:
    kills = np.random.binomial(failed_saves, p_fire_power)

# --- Outputs ---
st.subheader("Results hits")

st.metric("Expected hits", round(np.mean(hits), 2))
st.metric("Max seen (simulation)", int(np.max(hits)))
st.metric("Min seen (simulation)", int(np.min(hits)))

st.subheader("Probability distribution (hits)")

hist_hits = np.bincount(hits, minlength=shots+1) / TRIALS
st.bar_chart(hist_hits)

# --- Key stats ---
st.subheader("Key probabilities")

st.write("Pinned threshold (infantry platoon): 5+ hits")
st.write("Pinned threshold (big infantry platoon): 8+ hits")

st.write("Chance of 5+ hits:", round(hist_hits[5:].sum()*100, 2), "%")
st.write("Chance of 8+ hits:", round(hist_hits[8:].sum()*100, 2), "%")

# --- Outputs ---
st.subheader("Results kills")

st.metric("Expected kills", round(np.mean(kills), 2))
st.metric("Max seen (simulation)", int(np.max(kills)))
st.metric("Min seen (simulation)", int(np.min(kills)))

st.subheader("Probability distribution (kills)")

hist_kills = np.bincount(kills, minlength=shots+1) / TRIALS
st.bar_chart(hist_kills)

# --- Key stats ---
st.subheader("Key probabilities")

st.write("Chance of 2+ kills:", round(hist_kills[2:].sum()*100, 2), "%")
st.write("Chance of 5+ kills:", round(hist_kills[5:].sum()*100, 2), "%")