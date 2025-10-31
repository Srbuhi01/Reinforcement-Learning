# On-policy Control with Approximation — Mountain Car Example

This project demonstrates **semi-gradient on-policy control** with **function approximation** using the *Mountain Car* task from Sutton & Barto (Chapter 10).  
The goal is to learn an optimal policy for driving an underpowered car up a steep hill using **n-step semi-gradient Sarsa** with **tile coding**.

---

## Description

This example illustrates how **bootstrapping depth** (`n`) and **step-size** (α) affect learning and generalization when combining reinforcement learning with function approximation.

We apply **semi-gradient Sarsa** and its **n-step variant** to the **Mountain Car** control problem:

- **Environment:** continuous 2D state space (position, velocity)  
- **Actions:** 3 discrete throttle settings — reverse (-1), neutral (0), forward (+1)  
- **Reward:** -1 per step until the goal (position ≥ 0.5) is reached  
- **Objective:** minimize the number of steps per episode (reach the goal faster)

The function approximation uses **tile coding** with 8 overlapping tilings, each covering 1/8th of the state space with asymmetric offsets.

Each feature vector `x(s,a)` is a sparse binary encoding of active tiles, and the action-value function is approximated linearly as:

---

## Methodology

**Algorithm:**  
- Episodic semi-gradient Sarsa (1-step and n-step versions)  
- ε-greedy policy for on-policy control  
- Tile-coded feature representation  

**Parameters:**  
- Number of tilings: 8  
- Step sizes (α): tested from 0.25 to 1.5 (scaled by number of tilings)  
- n-step values: [1, 2, 4, 8, 16]  
- Runs: 5  
- Episodes: 50–10,000  

**Experiments:**
1. Compare 1-step vs 8-step Sarsa learning speeds (Figure 10.3).  
2. Study the effect of α × n on early performance (Figure 10.4).  

---

## Files Overview

### `src/mountain_car.py`
Implements the Mountain Car environment and physics:
- Position/velocity update equations  
- Reward and termination conditions  
- Action handling


### `notebooks/mountain_car.ipynb`
Main experiment notebook:
- Initializes value functions with tile-coded features  
- Trains semi-gradient Sarsa agents  
- Compares 1-step and n-step performance  
- Generates learning curves (Figures 10.3, 10.4)

---

## Results

### Figure 10.1 — Cost-to-Go Function
Shows the evolution of the learned value surface.  
Initially, the agent explores extensively due to optimistic initialization (all action values = 0).  
Over time, the learned value function captures the basin shape of the valley, leading the agent to discover the correct “swing back then accelerate” strategy.

### Figure 10.2 — Learning Curves (Step-size Comparison)
Demonstrates how different α values affect convergence speed.  
Moderate step sizes yield faster and more stable learning than very small or large values.

### Figure 10.3 — 1-step vs 8-step Semi-gradient Sarsa
Compares single-step and multi-step bootstrapping.  
The 8-step variant learns significantly faster and achieves better asymptotic performance than the 1-step version.

### Figure 10.4 — Effect of α and n on Learning Rate
Plots average steps per episode vs. α × number of tilings for multiple n-step configurations.  
Intermediate bootstrapping levels (n ≈ 4–8) achieve the best balance between bias and variance, confirming the tradeoff predicted by theory.

---

## Generated Figures
All plots are automatically saved to the `generated_images/` directory:

