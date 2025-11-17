# Baird’s Counterexample — Semi-Gradient TD Divergence

This project demonstrates the divergence of **semi-gradient TD methods** in an **off-policy** setting, using the classical **Baird’s counterexample**.  
The goal is to reproduce the behavior shown in **Sutton & Barto (Figure 11.2)** and illustrate why **function approximation + bootstrapping + off-policy learning** can become unstable.

---

## Description

This example highlights the fundamental instability that arises when using **linear function approximation with off-policy TD(0)**.

Baird’s counterexample is a 7-state MDP designed so that:

- The **behavior policy** visits all states nearly uniformly  
- The **target policy** always selects one action  
- **Rewards are zero**, yet  
- **Semi-gradient TD(0) diverges anyway**

The experiment compares two update schemes:

- **Standard semi-gradient off-policy TD(0)**
- **Semi-gradient DP update** (a synchronous version)

Both methods exhibit the same behavior: **the weights grow without bound**.

---

## Methodology

- **Algorithm:** Semi-gradient TD(0) + linear function approximation  
- **Policies:**  
  - Behavior policy: selects the dashed action with probability **6/7**  
  - Target policy: always chooses the solid action  
- **Discount:** γ = 0.99  
- **Rewards:** 0 (deterministic)  
- **Features:** 8-dimensional feature vectors as specified in Figure 11.1  
- **Visualization:** Plots of the **weight norms** through time (Figure 11.2 reproduction)

---

## Source Files Overview

### `src/counter_example.py`

Defines:

- The **Baird MDP** structure (states, actions, transitions)
- **Feature vectors** used for linear approximation
- Semi-gradient TD algorithms:
  - `semi_gradient_off_policy_TD`
  - `semi_gradient_DP`
- Utility functions:
  - Behavior / target policies  
  - RMS errors  
  - Sampling logic  

---

### `notebooks/bairds_counterexample.ipynb`

The notebook performs the main experiment:

- Loads helper modules from `src/`
- Runs semi-gradient TD(0) under **off-policy sampling**
- Repeats the experiment with a **synchronous DP update**
- Tracks the **weight vector norm** over thousands of updates
- Plots the curves that demonstrate **divergence**

> The output plot is saved as:  
> `generated_images/figure_11_2.png`

