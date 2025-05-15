# Cliff Walking

## Overview 

This project implements the Cliff Walking environment and compares three temporal-difference (TD) learning methods:

> SARSA (on-policy)

> Expected SARSA

> Q-Learning (off-policy)


- The environment is a 4×12 grid with a dangerous "cliff" section. Stepping into the cliff resets the agent to the start and gives a heavy penalty (-100). The goal is to reach the terminal state with minimal total penalty, learning either a safer or faster path depending on the algorithm.

---

## Files

 * cliff_walking.py

   - Defines the environment and transition logic.

   > Implements:

       * sarsa() – for SARSA and Expected SARSA (expected=True)

       * q_learning() – for Q-learning

       * Uses an ε-greedy strategy for exploration.

       * Includes print_optimal_policy() to display learned policies.


* cliff_walking.ipynb

       * Compares SARSA and Q-learning by plotting episode rewards.

       * Visualizes optimal policies learned by each method.

       * Evaluates both interim and long-term performance across different step sizes (α).


### Actions: Up, Down, Left, Right

> The cliff is the bottom row between start and goal – falling in gives −100 and resets to start.
> Each step otherwise gives a −1 reward to encourage shorter and safer paths.


## Learning Methods

* SARSA (On-Policy)
  - Updates value using the actual action taken: Q(s, a) ← Q(s, a) + α [r + γ Q(s', a') − Q(s, a)]

* Expected SARSA
  - Uses the expected value over the action distribution: Q(s, a) ← Q(s, a) + α [r + γ E_a'[Q(s', a')] − Q(s, a)]

* Q-Learning (Off-Policy)
  - Uses the maximum estimated value for the next state: Q(s, a) ← Q(s, a) + α [r + γ max_a' Q(s', a') − Q(s, a)]

## Outputs

 * Optimal policy visualization: Shows learned paths using directional arrows.

 * SARSA tends to choose safer paths avoiding the cliff.

 * Q-learning finds shorter but riskier paths near the edge.