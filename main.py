from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detection collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detection collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when r_paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when l_paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()

#############READ ME
# Developed a python program based of the pong game.
# Game uses multiple Classes, the turtle and time module
# The turtle module is used to create everything from the screen to the ball

###Ball Class
# A turtle ball is created with its shape, color, size, speed etc in it's innit
# The move function moves the ball to its xcor and ycor incremented by 10

#We then have the bounce functions for when the ball bounces into the opposite position once it makes contact with any of the paddles
  # its speed goes up by a fixed rate each time the paddle bounces of the left paddles to make it more challenging for users

#The reset_position function sends the ball back to its starting coordinates which was directly in the middle as well as
  #resetting its speed back to normal. It also starts to move the ball back into the direction of the right paddle


#Paddle Class
# Used to create the left and right paddles. Controls the paddle's up and down movements

####ScoreBoard class
#The Scoreboard class, inheriting from Turtle, manages and displays the game scores. It initializes with a score of 0
#for both players and updates the scoreboard each time a point is scored.
# The update_scoreboard method refreshes the
#displayed scores, positioning them on the screen.
# The l_point and r_point methods increment the left and right scores
#respectively and update the scoreboard accordingly.
