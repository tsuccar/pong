from turtle import Screen
from paddle import Paddle
from ball import Ball
from net import Net
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # When turned off. Turtle requires update() later in awhile-loop to show animation
game_net=Net()

ball=Ball()

scoreboard=Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))



screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


y_direction=-1
x_direction=-1
is_game_on = True
while is_game_on:
	screen.update()
	time.sleep(0.1)
	ball.move(x_direction,y_direction)
	crnt_x = ball.xcor()
	crnt_y = ball.ycor()
	print(crnt_x, crnt_y)
	if crnt_y >= 280:
		y_direction = -1
	elif crnt_y <= -280:
		y_direction =  1
	elif ball.distance(r_paddle) < 38:
		x_direction = -1
	elif ball.distance(l_paddle) < 38:
		x_direction = +1
	elif ball.xcor() >=360:
		print("1 point for RIGHT Paddle")
		scoreboard.show_value(r_pad=1)
		print(f"showing score : {scoreboard.r_pad_score}")
		is_game_on = False
	elif ball.xcor() <=-360:
		print("1 point for LEFT Paddle")
		scoreboard.show_value(l_pad=1)
		print(f"showing score : {scoreboard.l_pad_score}")
		is_game_on = False




screen.exitonclick()
