## Multi-Armed Bandit Simulation

### Overview
This project simulates and analyzes different action selection strategies in a multi-armed bandit problem. The main focus is on comparing greedy and ε-greedy strategies, as well as exploring the impact of optimistic versus realistic initial values on learning performance.

### Dependencies
Ensure you have the following Python libraries installed before running the script:
- `numpy`
- `matplotlib`
- `tqdm`
- `fontTools`
- `src.bandit` (Custom implementation of the Bandit class)

To install missing dependencies, run:
```bash
pip install numpy matplotlib tqdm fonttools
```

### Project Structure
- `simulate(runs, times, bandits)`: Main function to run the bandit simulation.
- `Bandit`: A custom class representing a multi-armed bandit environment.
- `generated_images/`: Stores generated plots.

### Usage
1. **Reward Distribution (Figure 2.1)**
   - A violin plot is generated to show the distribution of rewards for different actions.

2. **Greedy vs. ε-Greedy Action Selection (Figure 2.2)**
   - Runs simulations with different ε values (0, 0.1, 0.01) to analyze the impact of exploration.
   - Plots:
     - Average reward over time.
     - Percentage of optimal actions taken.

3. **Optimistic vs. Realistic Initial Values (Figure 2.3)**
   - Compares two settings:
     - `ε = 0, Q1 = 5, α = 0.1`
     - `ε = 0.1, Q1 = 0, α = 0.1`
   - Evaluates the effect of initial action-value estimates on learning.

### Running the Script
Execute the script using:

python script.py

Output
- The generated figures will be saved in the `generated_images/` directory as:
  - `figure_2_1.png`
  - `figure_2_2.png`
  - `figure_2_3.png`

Notes
- The `Bandit` class should be defined in `src/bandit.py`.
- The code uses `matplotlib.use('Agg')` to avoid GUI issues when running on a headless server.


