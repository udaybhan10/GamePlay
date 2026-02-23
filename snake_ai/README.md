# AI Plays Snake with Deep Q-Learning

An AI agent trained to play the classic game of Snake using Reinforcement Learning (Deep Q-Learning / DQN). 
The agent observes the environment state and learns to maximize its score over time entirely through self-play and a reward system.

## Tech Stack
- **Python**: Core language.
- **PyTorch**: Used to build and train the Deep Q-Network (Neural Network).
- **Pygame**: Used for rendering the Snake game environment.
- **Matplotlib** & **IPython**: For plotting and visualizing the agent's performance in real-time during training.

## Architecture & Logic
The project relies on three primary interconnected components:

1. **Environment (`game.py`)**: 
   The Pygame implementation of Snake. It handles the game state, collision detection, and food placement. Crucially, it exposes an API for the AI (`play_step(action)`) that applies an action, computes the reward, and checks if the game is over.

2. **Agent (`agent.py`)**:
   The RL Agent handling the Q-Learning logic.
   - **State**: Converts the complex game screen into an 11-variable boolean array (e.g., Is there danger straight ahead? Is food to the left? What is my current direction?).
   - **Experience Replay**: Remembers past states, actions, rewards, and next states in a `deque` memory buffer. It samples from this memory to train the model, dramatically improving stability and learning speed.
   - **Exploration vs. Exploitation**: Uses an epsilon-greedy strategy. Initially, it makes random moves to explore the environment. Gradually, as `epsilon` decays, it relies on the Neural Network's predictions (exploits what it learned).

3. **Neural Network (`model.py`)**:
   A feed-forward network with one generic hidden layer (`Linear_QNet`). It takes the 11-state array as input and predicts the Q-value (expected future reward) for the 3 possible actions: [Go Straight, Turn Right, Turn Left].

## Rewards System
- **+10**: Eating food.
- **-10**: Game over (colliding with a wall or itself).
- **0**: Every other step.

## Installation & Setup

1. **Clone or Download the repository.**
2. **Navigate to the project directory:**
   ```bash
   cd snake_ai
   ```
3. **Set up a Python Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install Dependencies:**
   ```bash
   pip install torch torchvision torchaudio pygame matplotlib ipython
   ```

## How to Run & Train the AI

To start the training process and watch the agent play:

```bash
python agent.py
```

- A Pygame window will open showing the game.
- A Matplotlib live-chart will pop up to show the agent's `Score` and `Mean Score` over epochs.
- The model (weights) will automatically save to `model/model.pth` every time the agent hits a new high score.
