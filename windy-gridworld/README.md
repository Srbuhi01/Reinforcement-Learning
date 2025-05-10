
# Windy Gridworld with SARSA (On-policy TD Control)

This project is an implementation of the SARSA algorithm (on-policy TD control) applied to the Windy Gridworld environment, based on Example 6.5 from "Reinforcement Learning: An Introduction" by Sutton and Barto.

## Theoretical Background

### SARSA (State-Action-Reward-State-Action)

SARSA is an on-policy temporal-difference (TD) learning method used to estimate the action-value function
Q(s,a) while following the same policy being improved. The update rule for SARSA is:
𝑄(𝑆𝑡 , 𝐴𝑡)← 𝑄(𝑆𝑡 , 𝐴𝑡) + 𝛼[𝑅𝑡+ 1+ 𝛾𝑄(𝑆𝑡 + 1 , 𝐴𝑡 + 1) − 𝑄(𝑆𝑡 , 𝐴𝑡)]

Here:

- 𝑆𝑡 is the current state
- 𝐴𝑡 is the action taken
- 𝑅𝑡 + 1 is the reward received
- 𝑆𝑡 + 1 is the next state
- 𝐴𝑡 + 1 is the next action
- 𝛼 is the learning rate
- 𝛾 is the discount factor

### SARSA uses the full quintuple 
(𝑆𝑡, 𝐴𝑡, 𝑅𝑡 + 1, 𝑆𝑡 + 1, 𝐴𝑡 + 1), which is why it is named SARSA.

- This approach is particularly well-suited for problems where termination is not guaranteed, as is the case in Windy Gridworld. It learns online and adjusts behavior during the episode.

## Windy Gridworld

- Windy Gridworld is a 7x10 grid with start and goal positions. A wind, varying in strength by column, pushes the agent upward. The challenge is to find an optimal policy that reaches the goal as fast as possible despite the wind.

### Key details:

Actions: Up, Down, Left, Right

Wind strength: Specified per column

Rewards: -1 per step

Discount: γ = 1

Exploration: ε-greedy with ε = 0.1

Learning rate: α = 0.5

##  Algorithm Used
We use ε-greedy SARSA to learn an optimal policy over 500 episodes. At each step:

- An action is selected using ε-greedy policy.

- A transition occurs based on action and wind.

- The Q-table is updated using the SARSA update rule.

Performance improves over episodes, as shown in the learning curve (time steps vs. episodes).

## Results
Q-table converged to an optimal policy in less than 500 episodes.

The optimal policy successfully guides the agent to the goal with minimal steps.

Cumulative time steps decreased consistently as the agent learned.

Final policy example (G = goal):

## References
Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning: An Introduction. Chapter 6: Temporal-Difference Learning.

Example 6.5: Windy Gridworld

