# Reinforcement Learning Projects

## Overview

 This repository contains a collection of Reinforcement Learning (RL) projects developed as part of the Reinforcement Learning course at the National Polytechnic University of Armenia (NPUA).

> The projects apply fundamental RL algorithms to solve classic problems, combining theoretical foundations with practical implementation.
  They are inspired by Reinforcement Learning: An Introduction by Richard S. Sutton and Andrew G. Barto.

---

## Repository Structure

##### Each project is organized into its own subdirectory and typically contains:

- code/ – Source code, notebooks

- results/ – Plots, visualizations, and experiment outputs

- README.md – Project-specific documentation

---

## Projects

* [1. Tic-Tac-Toe](https://github.com/Srbuhi01/Reinforcement-Learning/tree/main/tic-tac-toe)
    >This project trains a Reinforcement Learning (RL) agent to play Tic-Tac-Toe through self-play, enabling it to learn optimal strategies over time. It features a Human vs AI mode for interactive gameplay, incorporates early detection of win or tie conditions to improve efficiency, and demonstrates continuous strategy improvement as the agent gains experience. The main implementation can be found in the tic-tac-toe.py file.
   
* [2. Ten-Armed Testbed (Multi-Armed Bandit)](https://github.com/Srbuhi01/Reinforcement-Learning/tree/main/ten-armed-testbed)
    >This project simulates the multi-armed bandit problem to illustrate the exploration-exploitation trade-off, a core concept in Reinforcement Learning. It implements several action-selection strategies, including ε-greedy, Upper Confidence Bound (UCB), and Gradient Bandits. Key concepts demonstrated include action-value estimation and the impact of optimistic versus realistic initial value assumptions. The main implementation is provided in the `ten-armed-testbed.ipynb` notebook.
   
* [3. Gridworld – Dynamic Programming (DP)](https://github.com/Srbuhi01/Reinforcement-Learning/tree/main/gridworld-dp)
    > This project solves a 4x4 Gridworld problem using Dynamic Programming techniques to evaluate and improve policies in a deterministic environment. It implements key algorithms such as policy evaluation and policy improvement, with a focus on comparing in-place versus out-of-place updates for value function computation. The main implementation is available in the `grid_world.ipynb` notebook.

* [4. Gridworld – Markov Decision Process (MDP)](https://github.com/Srbuhi01/Reinforcement-Learning/tree/main/gridworld-mdp)
    > This project applies Markov Decision Process (MDP) principles to solve a 5x5 Gridworld environment, focusing on optimal policy discovery through dynamic programming. It utilizes techniques such as value iteration and Bellman equations, and includes visualizations that illustrate the convergence of both the value function and the policy over time. The main implementation is found in the grid_world.ipynb notebook.

* [5. Gambler’s Problem](https://github.com/Srbuhi01/Reinforcement-Learning/tree/main/gambler-problem)
    > This project implements the classic Gambler’s Problem using value iteration within a finite Markov Decision Process (MDP) framework. The objective is to learn the optimal policy that maximizes the probability of reaching a target capital. It emphasizes the use of the Bellman optimality equation and demonstrates the convergence of value functions and policies through iterative updates. The main implementation is located in the `gamblers_problem.ipynb` notebook.

* [6. Blackjack](https://github.com/Srbuhi01/Reinforcement-Learning/tree/main/blackjack)
    > This project simulates the game of Blackjack as an episodic finite Markov Decision Process (MDP) and applies Monte Carlo Exploring Starts (MC ES) to learn optimal playing strategies. It models the game's dynamics using simplified rules and defines states based on the player's sum, dealer’s visible card, and the presence of a usable ace. The project also includes an extension using off-policy evaluation with ordinary and weighted importance sampling to estimate state values under different policies. Key visualizations illustrate the progression from a random to an optimal policy. The main implementation is located in the `black_jack.ipynb` notebook.

* [7. Infinite-Variance](https://github.com/Srbuhi01/Reinforcement-Learning/tree/main/infinite-variance)
    > This project explores off-policy first-visit Monte Carlo evaluation using ordinary importance sampling on a simple one-state MDP, inspired by Example 5.5 from *Reinforcement Learning: An Introduction* by Sutton and Barto. It highlights how ordinary importance sampling, while theoretically unbiased, can suffer from infinite variance, leading to highly unstable value estimates. The environment consists of a single state with two actions—left and right—where the target policy always chooses left, and the behavior policy selects actions uniformly at random. Through this setup, the project demonstrates the challenges of off-policy evaluation in scenarios prone to high variance. The main implementation is located in the `infinite_variance.ipynb` notebook.

* [8. Random Walk](https://github.com/Srbuhi01/Reinforcement-Learning/tree/main/random-walk)
    > This project implements the classic Random Walk example to compare Monte Carlo (MC) and Temporal Difference (TD) methods for policy evaluation. The environment has 7 states, with episodes starting at the center and ending at either terminal state. MC updates state values based on full returns at episode end, while TD uses one-step bootstrapping for incremental updates. The project also applies batch updating to observe convergence behavior across both methods. The main implementation is located in the `random_walk.ipynb` notebook.

* [9. Windy Gridworld](https://github.com/Srbuhi01/Reinforcement-Learning/tree/main/windy-gridworld)
    > This project implements the SARSA algorithm—an on-policy temporal-difference (TD) control method—on the Windy Gridworld environment. The environment is a 7x10 grid where varying wind strengths push the agent upward, challenging it to find an optimal path from start to goal. Using an ε-greedy policy with ε=0.1, a learning rate α=0.5, and discount factor γ=1, the agent updates its action-value estimates online through SARSA’s update rule over 500 episodes. The project demonstrates how SARSA learns to navigate the wind and improves performance as training progresses.  The main implementation is located in the `windy_grid_world.ipynb` notebook.

* [10. Cliff Walking](https://github.com/Srbuhi01/Reinforcement-Learning/tree/main/cliff-walking)
    > This project compares three reinforcement learning algorithms—SARSA, Expected SARSA, and Q-Learning—on the classic Cliff Walking environment. The agent navigates a 4×12 grid from start to goal while avoiding a cliff that gives a −100 penalty. SARSA learns safer paths through on-policy updates, Q-Learning aims for the optimal but riskier path via off-policy learning, and Expected SARSA balances both using expected values. The implementation is split between cliff_walking.py for core logic and cliff_walking.ipynb for training and visualization.
  
* [11. Maximization-Bias](https://github.com/Srbuhi01/Reinforcement-Learning/tree/main/maximization-bias)
   > This project illustrates how Q-learning can overestimate action values due to maximization bias and demonstrates how Double Q-learning mitigates this effect. It simulates a small MDP where the optimal policy is rarely chosen by standard Q-learning. Experimental results show that Double Q-learning aligns closely with the optimal action selection frequency. Implementation is provided in the maximization_bias.ipynb notebook.

* [12. Random Walk-FA](https://github.com/Srbuhi01/Reinforcement-Learning/tree/main/random-walk-fa)
   > This project implements several function approximation methods for the Random Walk problem, including State Aggregation, Bootstrapping, Polynomial & Fourier Bases, and Tile Coding. The experiments compare approximation accuracy, convergence speed, and RMSE, demonstrating how different techniques affect generalization and learning efficiency. Main notebooks include state_aggregation.ipynb, bootstrapping.ipynb, polynomials_vs_fourier.ipynb, and tile_coding.ipynb.

* [13. Random Walk-NTD](https://github.com/Srbuhi01/Reinforcement-Learning/tree/main/random-walk-ntd)
   > This project implements n-step Temporal Difference (TD) learning on a 19-state random walk. It investigates how varying n (number of steps) and α (step-size) affect the accuracy of state-value estimates. RMS error is tracked across episodes and runs, illustrating trade-offs between update variance and convergence speed. Implementation is provided in the random_walk.ipynb notebook.

* [14. Mazes](https://github.com/Srbuhi01/Reinforcement-Learning/tree/main/mazes)
   > This project compares Dyna-Q, Dyna-Q+, and Prioritized Sweeping algorithms in maze environments. It studies adaptation to non-stationary and increasingly complex mazes, showing how planning and prioritization accelerate learning. Experiments demonstrate faster convergence and effective adaptation to changing paths. Implementations are provided in dyna_maze.ipynb, changing_maze.ipynb, and prioritized_sweeping.ipynb. 

* [15. Trajectory Sampling](https://github.com/Srbuhi01/Reinforcement-Learning/tree/main/trajectory-sampling)
   > This project reproduces Figure 8.8 from Sutton & Barto, comparing uniform vs on-policy trajectory sampling in tabular expected updates for randomly generated MDPs. It evaluates state-action value estimates and tracks start-state value under a greedy policy. Experiments show faster initial learning with on-policy sampling but slower long-term convergence, especially for smaller branching factors. Implementation is provided in trajectory_sampling.ipynb.

* [16. Coarse Coding](https://github.com/Srbuhi01/Reinforcement-Learning/tree/main/coarse-coding)
   > This project demonstrates coarse coding with linear function approximation on a 1D square-wave target function. It investigates how receptive field width affects learning and generalization. Experiments compare narrow, medium, and broad features across multiple sample sizes, showing trade-offs between smoothness, convergence speed, and approximation fidelity. Implementation is provided in square_wave.ipynb.

* [17. Update Comparison](https://github.com/Srbuhi01/Reinforcement-Learning/tree/main/updates-comparison)
   > This project reproduces Figure 8.7 from Sutton & Barto, comparing expectation (distribution) vs sample models in value estimation. It tracks RMS error between sample-based estimates and true values across different branching factors. Results show that sample-based estimates converge slower for larger branching factors but remain practical, while expectation-based models compute exact means. Implementation is provided in expectation_vs_sample.ipynb.

  
---

## Installation

1. Make sure you have **Python 3.x** installed. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone this repository:
   ```bash
   git clone https://github.com/Srbuhi01/Reinforcement-Learning.git
   cd Reinforcement-Learning



