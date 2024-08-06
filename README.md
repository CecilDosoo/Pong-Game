# Pong-Game

Developed a Python program based on the Pong game, utilizing multiple classes along with the Turtle and Time modules. The Turtle module is used to create and manage all game elements, from the screen and paddles to the ball, ensuring an interactive and engaging gameplay experience.

# Ball Class
- The Ball class models the ball in the Pong game. When initialized, the ball is configured with a circular shape, white color, and initial movement speeds for both the x and y directions. The move method updates the ball's position based on these movement speeds

- The bounce_y method reverses the ball's vertical direction, while the bounce_x method reverses the horizontal direction and slightly increases the ball's speed to enhance game difficulty.

- The reset_position method centers the ball at the origin and resets its speed, preparing it for a new round of play.

# Paddle Class
- The Paddle class models a paddle in the Pong game, extending the Turtle class to create a graphical paddle. When initialized, the paddle is given a square shape, white color, and a vertical stretch to define its size. It is positioned at a specified location on the screen.

- The class includes two methods for movement: up and down. The up method moves the paddle upward by increasing its y-coordinate, while the down method moves it downward by decreasing the y-coordinate.

# Scoreboard Class
- The Scoreboard class models the score display for the Pong game, extending the Turtle class to manage and show scores. Upon initialization, the scoreboard is set up with a white color, and it is configured to be hidden when not in use. It initializes with scores for both the left and right players set to zero and updates the scoreboard display accordingly.

- The update_scoreboard method clears the previous scores and redraws the updated scores for both players

- The l_point and r_point methods increment the scores for the left and right players, respectively, and then call update_scoreboard to reflect these changes on the screen.
