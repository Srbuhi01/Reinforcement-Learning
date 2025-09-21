# Expectation vs Sample Models in Reinforcement Learning

This project reproduces Figure 8.7 from “Reinforcement Learning: An Introduction (2nd Edition)” by Sutton & Barto. It illustrates how the error in value estimates decreases when using sample models compared to the true expectation (distribution model), depending on the branching factor
b.
---
## Project Structure

updates-comparison/        
 ├── .idea/             
 ├── book_images/        
 ├── generated_images/  
 ├── notebooks/
 │   └── expectation_vs_sample.ipynb
 ├── src/                
 │   └── __init__.py
 ├── expectation_vs_sample.py       
 └── README.md  

---
## Problem Description

- We simulate a state with b possible next states.

- Each next state has a reward drawn from a normal distribution.

- The true value of the current state = mean of all next-state values (distribution model).

- The sample estimate is obtained by repeatedly sampling one of the next states and computing the running average.

- We track the error between the running estimate and the true value.

---

***Expectation vs Sample Models***

* Distribution model (expectation): computes exact mean over all possible outcomes.

* Sample model: estimates the mean by sampling outcomes randomly.

* Larger branching factors make exact expectation harder, but sampling remains practical.

---
## Experimental Setup

- Runs: 100 independent simulations

- Branching factors (b): 2, 10, 100, 1000

- Samples per run: 2 × b

- Metric: RMS error between sample-based estimate and true value

---

## Results

- Errors decrease as the number of samples grows.

- Larger branching factors converge more slowly.

- The generated plot corresponds to Sutton & Barto Figure 8.7:

      > X-axis: computations per branching factor (0, b, 2b)
      > Y-axis: RMS error in value estimate
---

![`figure_8_7.png`](generated_images/figure_8_7.png)