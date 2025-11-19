# Baird’s Counterexample — Reproduction and Analysis

This project reproduces and visualizes the classical Baird’s Counterexample from Sutton & Barto’s Reinforcement Learning: An Introduction (2nd Edition). The goal is to illustrate why the combination of **function approximation, bootstrapping,** and **off‑policy learning** can lead to **instability and divergence.**

---

## Overview 

Baird’s counterexample is a simple Markov Decision Process specifically constructed to show that **semi-gradient TD(0)** can diverge under off-policy training, even when the value function is linear and the environment is deterministic.

- A clean Python implementation of the counterexample.

- Jupyter notebooks reproducing Figures 11.2, 11.5, and 11.6 from Sutton’s book.

- Visualizations showing divergence of TD(0) and stability of Gradient TD and Emphatic TD methods.

---

## Why Does Baird’s Counterexample Matter?

In Chapter 11, Sutton & Barto show that combining:

- Function approximation (linear value function),

- Bootstrapping (TD targets), and

- Off-policy updates (different behavior and target policies)

can cause divergence, even in very small and simple environments.

This is known as the **"deadly triad"**.

Baird’s example is the most famous demonstration of this problem.

---

## Algorithms Included
1. Semi-gradient TD(0) — Diverges

Implements the update:

> θ ← θ + α (R + γ v(S') − v(S)) x(S)

This method is shown to diverge exactly as in Figure 11.2 of the book.

2. Gradient TD (TDC / GTD2) — Converges

Based on Chapter 11.3. These methods perform true gradient descent on the MSPBE objective and remain stable.

3. Emphatic TD — Converges

Based on Chapter 11.4. Uses “followon” weights and emphatic weighting to correct off-policy instability.

---

## Results

The generated images replicate the book’s illustrations:

- figure_11_2.png — Divergence of TD(0)

- figure_11_5.png — Stable learning of GTD methods

- figure_11_6.png — Emphatic TD convergence

They demonstrate the contrast between unstable and stable learning dynamics under off-policy training.

---

## Notebooks

Each notebook contains a complete, reproducible setup:

- Construction of Baird’s MDP

- Feature definitions

- Algorithm implementations

- Plots equivalent to the book’s figures

They can be run independently to explore different update rules.

---

## Code (src/counter_example.py)

The core file includes:

- Implementation of the MDP transitions

- Feature encodings

- TD(0), TDC, and Emphatic TD update rules

- Experiment loops for plotting stability or divergence

The code is organized so algorithms can be compared easily.

---

## Summary

This project serves as a minimal, faithful reproduction of Baird’s Counterexample from Sutton & Barto. It clearly demonstrates:

- The divergence of semi-gradient TD under off-policy learning,

- The stability provided by gradient-correct algorithms,

- The theoretical insights behind the “deadly triad”.
