# Gridworld via Dynamic Programming

This project implements **policy evaluation**, **policy improvement**, and **policy iteration** for a simple 4×4 gridworld environment, based on **Example 4.1** from *"Reinforcement Learning: An Introduction"* (Sutton & Barto, 2nd Edition).

---

## Overview

We consider a 4×4 Gridworld with 14 non-terminal states and 1 terminal state.  
The agent can choose from **four actions** at each state: **up**, **down**, **left**, **right**.  
Actions deterministically cause state transitions unless they would take the agent off the grid, in which case the state remains unchanged.

- **Reward**:  
  - \(-1\) on all transitions until reaching the terminal state.
- **Terminal State**:  
  - Shaded in the figure (formally one state, shown twice for convenience).
- **Policy**:  
  - **Equiprobable random policy** — all actions are equally likely.

The task is **episodic** and **undiscounted**.

---

##  Problem Setup

- **States**: \( S = \{1, 2, \ldots, 14\} \)
- **Actions**: \( A = \{\text{up}, \text{down}, \text{left}, \text{right}\} \)
- **Transitions**:
  - Valid movements correspond to action directions.
  - If an action would take the agent off the grid, the state remains unchanged.
- **Expected Reward Function**:
  \[
  r(s,a,s') = -1 \quad \text{for all } s, a, s'
  \]

---

##  Objectives

- **Policy Evaluation**:
  Estimate the state-value function \( v_{\pi}(s) \) under the equiprobable random policy.

- **Policy Improvement**:
  Derive a greedy policy based on the estimated value function.

- **Policy Iteration**:
  Repeatedly apply policy evaluation and policy improvement to find the optimal policy.

---

## Visuals

### Environment Visualization

<img src="../book_images/Example_4_1.PNG" alt="Gridworld" width="400"/>

### Iterative Policy Evaluation and Improvement

<img src="../book_images/Figure_4_1.PNG" alt="Policy Evaluation and Improvement" width="600"/>

- **Left Column**: Sequence of value function approximations for the random policy.
- **Right Column**: Sequence of greedy policies derived from the value function approximations.

The final policy is **optimal**, reaching the terminal state in a minimal number of steps.

---

## Implementation

The main computations are done using functions from `src/grid_world.py`:
---
## Results
Policy iteration converged extremely quickly, discovering the optimal policy after just 1 iteration in this simple example.

The optimal policy proceeds to the terminal state in the minimum number of steps.
---
## References
Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning: An Introduction (2nd Edition), Example 4.1.
