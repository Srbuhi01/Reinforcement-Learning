# n-Step Temporal Difference (TD) Learning Simulation

This project implements **n-step Temporal Difference (TD) learning** for a simple random walk environment. It explores how different values of **n** (number of steps) and **α** (step-size parameter) affect the learning of state-value estimates.

---

## Project Structure

random-walk-ntd/
│
├── .idea/
├── book_images/
│ └── Example_6_2_top.PNG
│ └── Figure_7_2.PNG
├── generated_images/
│ └── figure_7_2.png
├── notebooks/
│ └── random_walk.ipynb # Main notebook to run simulations and generate plots
├── src/
│ └── __init__.py
│ └── random_walk.py # Contains n-step TD function and hyper-parameters
├── requirements.txt # Python dependencies
└── README.md # This file

---

## Objective
To explore how different **n-step sizes (n)** and **step-size parameters (α)** affect the accuracy of state-value estimates. We measure this using **RMS error** between estimated and true state values.

---

## Problem Description
We simulate a **random walk** with 19 non-terminal states and 2 terminal states:

- Start state: 10 (middle of the walk)  
- Actions: move left or right with equal probability (0.5 each)  
- Rewards:
  - Left terminal state: -1  
  - Right terminal state: +1  
  - All other states: 0  

The goal is to estimate the **value of each non-terminal state** using n-step TD updates.

---

## n-Step TD Learning
- **n-step TD** updates the value of a state based on the sum of rewards for the next n steps, plus the estimated value of the state reached after n steps.  
- As n increases:
  - Updates consider more future rewards (less noisy than 1-step TD)  
  - Convergence may become slower  

---

## Experimental Setup
- **Episodes per run:** 10  
- **Independent runs:** 100  
- **Step-sizes (α):** 0.0 to 1.0 (increments of 0.1)  
- **n-steps:** 1, 2, 4, 8, …, 512  
- **Initial state-value estimates:** 0 for all states  
- **Metric:** RMS error between estimated and true state values  

---

## Results
- RMS errors are averaged over runs and episodes.  
- Observations:
  - Small n: faster updates but more variance in value estimates  
  - Large n: smoother updates, closer to true values, but slower convergence  
- The generated plot ![`figure_7_2.png`](generated_images/figure_7_2.png) shows RMS error vs step-size (α) for each n-step value.  

---

