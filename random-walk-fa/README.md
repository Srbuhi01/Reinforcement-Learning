#  Random Walk with Function Approximation

This project implements several **function approximation methods** for the **Random Walk** problem, as introduced in *Reinforcement Learning: An Introduction (Sutton & Barto, 2nd Edition)*.  
The goal is to study how different approximation techniques—such as **State Aggregation**, **Bootstrapping**, **Polynomial & Fourier Bases**, and **Tile Coding**—affect the accuracy of value estimation in reinforcement learning.


---

##  Implemented Components

### **1. `src/random_walk.py`**

This module contains the main logic for the random walk environment and value function approximation.

**Key elements:**
- `compute_true_value()`: Calculates the true value function for the 1000-state random walk.
- `ValueFunction`: Class that stores and updates value estimates for grouped states.
- `gradient_monte_carlo()`: Performs the Monte Carlo updates to estimate state values.
- Constants:
  - `states_number = 1000`
  - `states = np.arange(1, 1001)`

---

### **2. `notebooks/state_aggregation.ipynb`**

Demonstrates **State Aggregation** — a simple form of function approximation.

####  Description
States are grouped together (here into 10 groups of 100 states).  
Each group shares one estimated value; updates affect only that group’s weight.

####  Procedure
1. Compute the true values with `compute_true_value()`
2. Initialize a `ValueFunction` with 10 groups
3. Run **100,000 episodes** of Gradient Monte Carlo
4. Record state distribution and approximate values
5. Plot and save:
   - Approximate vs True value function
   - State visitation distribution

####  Output
Saved as:
- `generated_images/figure_9_1.png` — Approximate vs True Value Function  
- `generated_images/figure_9_2.png` — State Distribution  

####  Key Takeaways
- 1000 states → 10 groups of 100  
- Produces a “staircase” approximation of the true value curve  
- Edge biases occur due to asymmetric visit probabilities  

---

### **3. `notebooks/bootstrapping.ipynb`**

Implements **Bootstrapping** techniques to estimate the value function using partial updates from previous estimates.

####  Procedure
1. Use the same 1000-state random walk setup
2. Apply bootstrapped value updates (e.g., TD(0) or λ-returns)
3. Compare learning curves and approximation errors with Monte Carlo

####  Output
- `generated_images/figure_9_2.png` — Comparison of bootstrapping results
- Plots show how bootstrapping accelerates convergence compared to pure Monte Carlo

####  Key Takeaways
- Bootstrapping balances bias and variance  
- More efficient in long-horizon tasks  
- Demonstrates core difference between **Monte Carlo** and **TD learning**

---

### **4. `notebooks/polynomials_vs_fourier.ipynb`**

Demonstrates **Polynomial vs Fourier Basis** function approximation for the 1000-state random walk.

#### Description
Compares the performance of polynomial and Fourier bases for value function approximation. Fourier bases are generally more stable for online learning.

#### Procedure
1. Compute true values with `compute_true_value()`.
2. Initialize `BasesValueFunction` with different orders (5, 10, 20) for both polynomial and Fourier bases.
3. Apply Gradient Monte Carlo for **5000 episodes**.
4. Track state values and root-mean-squared error (RMSE) for each episode.
5. Plot learning curves comparing the bases.
6. Save the plot to `generated_images/figure_9_5.png`.

#### Output
- `generated_images/figure_9_5.png` — Learning curves comparing polynomial vs Fourier bases

#### Key Takeaways
- Polynomial bases may be unstable for online learning, especially with higher orders.
- Fourier bases provide smoother approximations and better generalization.
- RMSE curves illustrate differences in convergence speed and accuracy between the two bases.

---

### **5. `notebooks/tile_coding.ipynb`**

Implements **Tile Coding** for function approximation of the 1000-state random walk.

#### Description
Tile coding helps approximate large or continuous state spaces more precisely compared to simple state aggregation.

#### Procedure
1. Compute true values with `compute_true_value()`.
2. Initialize `TilingsValueFunction` with 50 tilings and 200 states per tile.
3. Apply Gradient Monte Carlo for **5000 episodes**, using a changing step-size per episode.
4. Track RMSE for each episode and compare tile coding vs single tiling (state aggregation).
5. Plot error curves and save to `generated_images/figure_9_10.png`.

#### Output
- `generated_images/figure_9_10.png` — Learning curves comparing Tile Coding vs Single Tiling

#### Key Takeaways
- Multiple tilings provide more accurate and faster convergence.
- Single tiling produces staircase-like approximation and slower learning.
- Varying step-size improves asymptotic performance for high-parameter approximations.

---

##  Concept Overview

### **State Aggregation**
> Groups states and shares one parameter among them. Simplifies computation but limits precision.

### **Bootstrapping**
> Updates estimates using other estimates — a core principle behind **Temporal-Difference (TD)** learning.

### **Polynomial & Fourier Bases**
> Represent states as features using polynomial or Fourier functions. Fourier bases are generally more stable for online learning.

### **Tile Coding**
> Uses overlapping tilings to provide richer feature representation for large or continuous state spaces.

Together, these methods demonstrate how function approximation allows reinforcement learning to scale beyond tabular problems.

---

##  Requirements

```bash
  pip install numpy matplotlib tqdm
