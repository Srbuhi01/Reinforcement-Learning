# Multi-Armed Bandit Simulation

## Overview
This project is an implementation and exploration of the Ten-Armed Testbed, a classic benchmark for evaluating action selection strategies in reinforcement learning, based on Chapter 2 of Sutton and Barto’s Reinforcement Learning: An Introduction.

The testbed simulates a 10-armed bandit problem where each arm provides stochastic rewards sampled from a stationary normal distribution. Through thousands of runs and time steps, various action selection algorithms are tested and compared based on their average reward and percentage of optimal actions taken. This gives insight into the trade-off between exploration and exploitation in reinforcement learning.

The project focuses on:

- Reproducing Figures 2.1 to 2.5 from the textbook.

- Comparing strategies like ε-greedy, UCB, optimistic initial values, and gradient bandits.

- Gaining intuition into how these methods behave in practice over time.


## Features
* ε-Greedy Action Selection: Explore the impact of varying epsilon values (0, 0.1, 0.01).

* Optimistic Initial Values: Encourages early exploration by initializing action values optimistically.

* Upper Confidence Bound (UCB): Balances exploration and exploitation using uncertainty estimates.

* Gradient Bandit Algorithm: Uses a preference-based approach with optional reward baselines.

* Extensive Visualization: Reproduces all major plots from Chapter 2 (Figures 2.1–2.5).

* Scalable Simulation: Easily configurable number of runs, steps, and algorithms.
---

## Dependencies
 - To run this project, you will need:

 - Python 3.X

 - numpy

 - matplotlib

 - tqdm – for visual progress bars


## Files and Modules
* bandit.py	- Core implementation of the Bandit class, supporting all algorithms.
* ten_armed_testbed.ipynb - Jupyter notebook that runs all simulations and generates plots.
* generated_images - Folder where all output figures (Figures 2.1 to 2.5) are saved as PNGs.
* README.md	- This documentation file.

## Expected Outputs
- Upon running the simulation, the following visualizations will be saved in the generated_images/ directory:

#### Figure	Description
> figure_2_1.png	Reward distributions of the 10 actions (used to illustrate variance).
> figure_2_2.png	Comparison of ε-greedy algorithms (ε = 0, 0.1, 0.01). Shows average reward and % optimal action.
> figure_2_3.png	Performance of optimistic initial values vs ε-greedy with normal values.
> figure_2_4.png	UCB action selection compared with ε-greedy.
> figure_2_5.png	Gradient bandit algorithm with different step sizes and baseline usage.

---

## Notes
- The `Bandit` class should be defined in `src/bandit.py`.
- The code uses `matplotlib.use('Agg')` to avoid GUI issues when running on a headless server.


