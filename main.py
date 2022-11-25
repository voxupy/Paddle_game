from turtle import Screen
from line import Line
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping pong game")
screen.tracer(0)

#class games
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()
line = Line()


#sterowanie postacia
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Colision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()

    #collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    #if we lost ball r_paddle
    if ball.xcor() > 390:
        ball.reset_position()
        score.increase_score_l()
        score.update_scoreboard_l()

    #if we lost ball l_paddle
    if ball.xcor() < -390:
        ball.reset_position()
        score.increase_score_r()
        score.update_scoreboard_r()
screen.exitonclick()



