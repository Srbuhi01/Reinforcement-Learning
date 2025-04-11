Reinforcement Learning Projects

Overview

This repository contains a collection of Reinforcement Learning (RL) projects developed as part of the Reinforcement Learning course at the National Polytechnic University of Armenia (NPUA).

The projects apply fundamental RL algorithms to solve classic problems, combining theoretical foundations with practical implementation.
They are inspired by Reinforcement Learning: An Introduction by Richard S. Sutton and Andrew G. Barto.
---

Repository Structure

Each project is organized into its own subdirectory and typically contains:

code/ – Source code

results/ – Plots, visualizations, and experiment outputs

README.md – Project-specific documentation

---

Projects

1. Tic-Tac-Toe

Description:
Trains an RL agent to play Tic-Tac-Toe through self-play.

Features:

Human vs AI mode

Early detection of win/tie states

Strategy improvement over time


Main File: tic-tac-toe.py

---

2. Ten-Armed Testbed (Multi-Armed Bandit)

Description:
Simulates the multi-armed bandit problem to demonstrate the exploration-exploitation trade-off.

Implemented Strategies:

ε-greedy

Upper Confidence Bound (UCB)

Gradient Bandits


Key Concepts:

Action-value estimation

Optimistic vs realistic initial values


Main File: ten-armed-testbed.ipynb

---

3. Gridworld – Dynamic Programming (DP)

Description:
Solves a 4x4 Gridworld problem using Dynamic Programming techniques.

Algorithms:

Policy evaluation

Policy improvement

In-place vs out-of-place updates


Main File: gridworld-dp.ipynb

---

4. Gridworld – Markov Decision Process (MDP)

Description:
Uses MDP principles to solve a 5x5 Gridworld environment.

Techniques:

Value iteration

Bellman equations

Visualizations of policy and value convergence


Main File: gridworld-mdp.ipynb

---

5. Gambler’s Problem

Description:
Implements the classic Gambler’s Problem using value iteration within a finite MDP setting.

Objective:
Learn the optimal policy to maximize the probability of reaching a goal state.

Focus:

Bellman optimality equation

Convergence of value functions and policies


Main File: gambler-problem.ipynb

---

Installation

 Make sure you have Python 3.x installed.


