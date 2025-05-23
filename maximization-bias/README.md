# Q-learning vs. Double Q-learning: Addressing Maximization Bias

This project illustrates how **maximization bias** can distort Q-learning and how **Double Q-learning** can mitigate it. The implementation is based on Example 6.7 and Figure 6.5 from *"Reinforcement Learning: An Introduction"* by Sutton and Barto (2nd edition).

##  Objective

To demonstrate that Q-learning tends to overestimate action values due to maximization bias, often leading to suboptimal action choices. Double Q-learning reduces this bias by using independent value estimates for selection and evaluation.

##  Problem Description

We simulate a small MDP:

- **State A** (initial state) has two actions:
  - `right`: transitions directly to a terminal state with **reward 0**
  - `left`: transitions to **State B** with **reward 0**
- **State B**: all actions lead to termination with reward drawn from **𝒩(0.1, 1.0)**

Thus, the expected return for choosing `left` in state A is 0.1, and 0 for `right`. Hence, under ε-greedy with ε=0.1, the optimal policy should choose `left` only 5% of the time. However, Q-learning often overestimates the value of B and chooses `left` more frequently.


### Maximization Bias

Maximization bias occurs when the **maximum of estimated values** is used as an estimate of the **maximum true value**, leading to a **positive bias**. This affects both Q-learning and Sarsa.

### Double Q-learning

Double Q-learning maintains two independent Q-value tables (`Q1` and `Q2`). On each step, one is used to determine the maximizing action, and the other is used to evaluate its value. This avoids using the same sample both for selection and estimation, which helps reduce bias.

##  Algorithms Implemented

- **Q-learning** — classic TD control algorithm
- **Double Q-learning** — alternating updates on two independent Q-value functions

## Experimental Setup

- **Episodes per run:** 300
- **Independent runs:** 1000
- **Initial Q-values:** 0
- **ε (exploration rate):** 0.1
- **α (learning rate):** 0.1
- **γ (discount factor):** 1.0

We track how often each algorithm chooses the `left` action from state A, averaged across runs.

##  Results

![Q vs Double Q](../generated_images/figure_6_5.png)

- **Q-learning**: tends to select the `left` action significantly more often than the optimal 5%.
- **Double Q-learning**: closely matches the optimal selection frequency, effectively eliminating maximization bias.


