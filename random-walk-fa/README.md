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

## Upcoming Notebooks

| Notebook | Description | Status |
|-----------|--------------|--------|
| `polynomials_vs_fourier.ipynb` | Comparison between polynomial and Fourier basis for function approximation | ⏳ Planned |
| `tile_coding.ipynb` | Implementation of tile coding for continuous state approximation | ⏳ Planned |

---

##  Concept Overview

### **State Aggregation**
> Groups states and shares one parameter among them. Simplifies computation but limits precision.

### **Bootstrapping**
> Updates estimates using other estimates — a core principle behind **Temporal-Difference (TD)** learning.

Together, these methods demonstrate how function approximation helps reinforcement learning scale beyond tabular problems.

---

##  Requirements

```bash
  pip install numpy matplotlib tqdm
