# Pong Game

This project is a Python program that recreates the classic Pong game using the Turtle and Time modules. The game features multiple classes that handle different aspects of gameplay, including the ball, paddles, and scoreboard, providing an interactive and engaging experience.

## Game Overview

The Pong game consists of two paddles and a ball. Players control the paddles to hit the ball back and forth, aiming to score points by getting the ball past their opponent’s paddle. The game features classic Pong mechanics, including ball movement, paddle control, and score tracking.

## Screenshots

https://github.com/user-attachments/assets/7ed7c7b3-7df3-4c77-ace3-9d0f5f3b40a2

![Game Screenshot 1](https://github.com/user-attachments/assets/e6e224f5-673a-4f56-81f8-a71d17d6c925)
![Game Screenshot 2](https://github.com/user-attachments/assets/61b452d4-03a0-4c54-a843-d353c301e183)
![Game Screenshot 3](https://github.com/user-attachments/assets/fdd9d86f-878b-44f2-8c6a-0b323d9294a0)

## Components

### Ball Class

The `Ball` class models the ball in the Pong game.

- **Initialization**: Configures the ball with a circular shape, white color, and initial movement speeds for both the x and y directions.
  
- **`move()`**: Updates the ball's position based on its current movement speeds.
  
- **`bounce_y()`**: Reverses the ball's vertical direction.
  
- **`bounce_x()`**: Reverses the ball's horizontal direction and slightly increases its speed to enhance difficulty.
  
- **`reset_position()`**: Centers the ball at the origin and resets its speed for a new round.

### Paddle Class

The `Paddle` class models a paddle in the Pong game.

- **Initialization**: Creates a paddle with a square shape, white color, and vertical stretch for size. Positions it at a specified location on the screen.
  
- **`up()`**: Moves the paddle upward by increasing its y-coordinate.
  
- **`down()`**: Moves the paddle downward by decreasing its y-coordinate.

### Scoreboard Class

The `Scoreboard` class handles the score display for the game.

- **Initialization**: Sets up the scoreboard with a white color and hidden turtle cursor. Initializes scores for both left and right players at zero.
  
- **`update_scoreboard()`**: Clears the previous scores and redraws the updated scores for both players.
  
- **`l_point()`**: Increments the score for the left player and updates the scoreboard.
  
- **`r_point()`**: Increments the score for the right player and updates the scoreboard.

## How to Run

To run the game, ensure you have Python installed on your system. Execute the main Python script that initializes and runs the game.
