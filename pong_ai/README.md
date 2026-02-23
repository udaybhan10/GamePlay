# Pong AI

A classic Human vs. AI Pong game built using Python and Pygame.
The left paddle is controlled by a human player, while the right paddle is an automated AI opponent that tracks the vertical position of the ball.

## Prerequisites

- **Python 3.x**
- **Pygame**

## Installation

1. Navigate to the project directory:
   ```bash
   cd "pong_ai"
   ```
2. Set up a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install Pygame:
   ```bash
   pip install pygame
   ```

## How to Play

1. Run the game from your terminal:
   ```bash
   python main.py
   ```
2. A Pygame window will open.
3. **Controls**:
   - Use the **`W`** key to move your paddle (left side) **UP**.
   - Use the **`S`** key to move your paddle (left side) **DOWN**.
4. The goal is to bounce the ball past the AI paddle (right side) to score a point. If the ball passes your paddle, the AI scores a point.
5. The game will continue tracking scores indefinitely at the top of the screen.
6. To quit the game, close the window or press the **`X`** key.

## Architecture

- `main.py`: Handles the display initialization, the main game loop, tracking the score, and collision logic between the ball and the paddles.
- `sprites.py`: Contains the game entities.
  - `Paddle`: Used for both the Player and the AI. The AI variant has an `update_ai()` method to automatically follow the ball.
  - `Ball`: Stores its velocity and handles bouncing mechanics when it collides with screen edges or paddles.
