# Random Walk with Monte Carlo and Temporal Difference Methods

This project implements the classic **Random Walk** example from Reinforcement Learning, as described in Sutton and Barto's book *"Reinforcement Learning: An Introduction"*. It compares the **Monte Carlo (MC)** and **Temporal Difference (TD)** methods for policy evaluation in a simple environment.

##  Problem Description

- There are 7 states:  
  - `0` - Left terminal  
  - `1` to `5` - Non-terminal states (A to E)  
  - `6` - Right terminal
- All episodes start at the center state `3` (C).
- At each step, the agent moves left or right with equal probability (0.5).
- The episode terminates when a terminal state is reached.
- Rewards:
  - `+1` if terminated at state `6`
  - `0` if terminated at state `0`
  - `0` otherwise

## Implemented Methods

- **Monte Carlo (MC)**: Updates state-values at the end of the episode using full returns.
- **Temporal Difference (TD)**: Updates values incrementally using one-step bootstrapping.
- **Batch Updating**: Uses all previously observed episodes to update values until convergence.


## Output
 - The script computes RMSE (Root Mean Square Error) between the true values and estimated values over time.

 - RMSEs are averaged over 100 independent runs.

