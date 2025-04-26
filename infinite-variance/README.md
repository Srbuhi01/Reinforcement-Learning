Overview

Infinite-Variance implements off-policy first-visit Monte Carlo evaluation using ordinary importance sampling on a simple one-state MDP.
This is based on Example 5.5 from "Reinforcement Learning: An Introduction" (Sutton & Barto, 2nd Edition).

The project shows how ordinary importance sampling can lead to infinite variance, resulting in extremely unstable value estimates, despite being theoretically unbiased.

Problem Setup
Environment: One state (S) with two possible actions: left and right.

Target Policy π: Always selects left.

Behavior Policy b: Selects left or right with equal probability (50% each).

Rewards:

Choosing right: 
 R=0 and episode ends immediately.
Choosing left:
 90% probability: stay in the same state with R=0,
 10% probability: move to terminal state with R=+1.

Goal
Estimate the expected return V𝜋(S)Nusing episodes generated under the behavior policy b with ordinary importance sampling and observe the effect of infinite variance.

Results
The learning curve demonstrates the characteristic instability caused by infinite variance, replicating the behavior seen in the reference book.

<p align="center"> <img src="book_images/Figure_5_4_2.PNG" alt="Learning Curve" width="600"/> </p>

References:
Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning: An Introduction (2nd Edition), Example 5.5.


