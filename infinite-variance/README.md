# Infinite-Variance Monte Carlo Evaluation

This project implements off-policy first-visit Monte Carlo evaluation using **ordinary importance sampling** on a simple one-state MDP.  
It is based on Example 5.5 from *"Reinforcement Learning: An Introduction"* (Sutton & Barto, 2nd Edition).

---

##  Overview
The project demonstrates how ordinary importance sampling can lead to **infinite variance**, resulting in extremely unstable value estimates, despite being theoretically unbiased.

---

##  Problem Setup

- **Environment**: One state (S) with two possible actions: left and right.

- **Target Policy (π)**: Always selects **left**.

- **Behavior Policy (b)**: Selects **left** or **right** with equal probability (50% each).

### Rewards:
- Choosing **right**:
  - \( R = 0 \) and episode ends immediately.

- Choosing **left**:
  - 90% probability: stay in the same state with  R = 0 ,
  - 10% probability: move to terminal state with  R = +1.

---

## Goal
Estimate the expected return  Vπ(S)  using episodes generated under the behavior policy  b 
with **ordinary importance sampling** and observe the effect of **infinite variance**.

---

## Results

The learning curve demonstrates the characteristic instability caused by infinite variance,  
replicating the behavior seen in the reference book.

![Learning Curve](book_images/Figure_5_4_2.PNG)


