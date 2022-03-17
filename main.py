from turtle import Screen
from paddle import Paddle, Net
from ball import Ball
from score import Score
import time

END_GAME_SCORE = 10

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Score()
net = Net()
net.draw_net()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce:
        ball.bounce_y()

    # Detect collision with paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when r_paddle misses:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        if scoreboard.l_score == END_GAME_SCORE:
            game_is_on = False
            net.clear()
            scoreboard.left_wins()

    # Detect when l_paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        if scoreboard.r_score == END_GAME_SCORE:
            game_is_on = False
            net.clear()
            scoreboard.right_wins()

screen.exitonclick()
