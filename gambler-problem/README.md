#  Gambler's Problem — Value Iteration in Reinforcement Learning

This project implements the **Gambler's Problem** using **Value Iteration**, based on the example from *Sutton and Barto's "Reinforcement Learning: An Introduction"*.

---

## 📌 Problem Overview

A gambler aims to reach a goal of `$100` by betting on the outcome of a biased coin (with probability `p_h = 0.4` of heads).  
At each state (capital), the gambler can choose a stake and transitions to a new state depending on the result of the coin toss.

**Goal:** Maximize the probability of reaching the goal (capital = 100).

---

## Algorithm Used

- **Value Iteration**:
  - Iteratively updates state-value function `V(s)`.
  - Chooses actions that yield the maximum expected return.
  - Stops when the maximum value change in a sweep is below a small threshold ε (`1e-9`).

---

## 📈 Output

- **Value Estimates per Sweep**: How the value function evolves with each iteration.
- **Final Policy**: Optimal stake to bet at each capital level.

The output is saved as a high-resolution image:

