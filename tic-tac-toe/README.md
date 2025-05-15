# Tic-Tac-Toe

## Overview
This project explores a classic example of Reinforcement Learning (RL) through the simple yet strategic game of Tic-Tac-Toe. It serves as an educational demonstration of how intelligent agents can learn optimal decision-making behaviors by interacting with an environment—in this case, a 3x3 game board.

The implemented RL agents use a value-based learning approach, where each possible board configuration (or "state") is assigned a value representing the estimated probability of winning from that state. These values are refined over time by playing thousands of games against each other, gradually improving their strategies through experience.

Unlike traditional game-solving techniques (like minimax), this approach doesn’t rely on perfect foresight or a complete model of the opponent. Instead, the agent learns solely from the outcomes of its own moves and gradually adapts to maximize rewards (wins).

Key goals of this project:

Demonstrate how reinforcement learning can be applied to discrete, episodic environments like board games.

Compare performance between self-trained agents using value functions.

Enable a human player to challenge a trained AI to observe and evaluate learned behavior.

Highlight the importance of exploration vs. exploitation and temporal-difference learning.

This project is a hands-on application of RL concepts from foundational texts like Sutton & Barto's Reinforcement Learning: An Introduction, making it a great starting point for anyone learning about machine learning, artificial intelligence, or autonomous agents.

## Features

- **Train RL players**: Two RL agents learn to play Tic-Tac-Toe using self-play.
- **Compete**: The trained agents can compete against each other with optimal strategies.
- **Human vs AI**: A human player can challenge the trained AI.

## Dependencies
Ensure you have the following Python packages installed:
```bash
pip install numpy
```

## Files & Modules
- `state.py`: Defines board configurations and game states.
- `player.py`: Implements RL and Human players.
- `judge.py`: Handles game rules and matches between players.
- `main.py`: Contains training, competition, and gameplay logic.

## Usage
### Train RL Players
Run the following command to train two RL agents:
```python
python main.py
```
This trains the players for `100,000` epochs and saves their learned policies.

### Compete Between Trained RL Players
Modify `main.py` and call:
```python
compete(turns=1000)
```
This lets the trained players compete and evaluates their performance.

### Play Against AI
To play against the trained RL agent, modify `main.py` and call:
```python
play()
```
You will play as the first player against the RL agent playing second.

## Expected Outputs
- During training, intermediate win rates of both RL agents are printed.
- During competition, the win rates of both RL players are displayed.
- When playing against AI, the game announces if you win, lose, or draw.



