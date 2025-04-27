# Gridworld MDP

This project implements a **Gridworld Markov Decision Process (MDP)** where an agent navigates a \(5 \times 5\) grid, receiving rewards based on its actions.  
Special states **A** and **B** provide additional rewards and transition the agent to **A'** and **B'**, respectively.

---

## Features

- MDP environment with state transitions and rewards
- Bellman equation for state-value computation
- Value iteration for optimal policy determination
- Visualization of state-values and policies

---

## Gridworld as Finite MDP

**Figure 3.2 (left)** shows a rectangular gridworld representation of a simple finite MDP.

- Each cell corresponds to a state of the environment.
- At each cell, four actions are possible: **north (up)**, **south (down)**, **east (right)**, and **west (left)**.
- Actions deterministically move the agent one cell in the respective direction.
- Actions that would take the agent off the grid leave the location unchanged but result in a reward of **-1**.
- Other actions result in a reward of **0**, except those from special states **A** and **B**:
  - From **state A**, all actions yield a reward of **+10** and move the agent to **A'**.
  - From **state B**, all actions yield a reward of **+5** and move the agent to **B'**.

---

### Random Policy Setup

Suppose the agent selects all four actions with equal probability in all states.  
Thus, the probability of each action is:

\[
\text{action\_probability} = 0.25
\]

The discount rate is:

\[
\gamma = 0.9
\]

---

## Visualization

**Environment layout (Figure 3.2):**

![Gridworld Layout](../book_images/Figure_3_2.PNG)

---

## State-Value Computation with Random Policy

The value function \(v_\pi\) for the random policy (with discount factor \(\gamma=0.9\)) is computed by solving the Bellman equation:

## ✅  Result:

-Notice negative values near the lower edge.

-State A is the best state to be in under this random policy.

-Expected return from A is less than immediate reward (+10) because from A' it may hit the grid edge.

-State B is valued more than its immediate reward (+5) because from B' the agent might find better paths.

## 📚 References
Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning: An Introduction (2nd Edition), Chapter 3.
