from turtle import Screen
from paddle import Paddle
from ball import Ball
from net import Net
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # When turned off. Turtle requires update() later in awhile-loop to show animation
game_net=Net()

ball=Ball()

l_paddle_scoreboard=Scoreboard((-100,270))
r_paddle_scoreboard=Scoreboard((100,270))

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


y_direction=-1
x_direction=-1
l_paddle_scoreboard.show()
r_paddle_scoreboard.show()
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
		l_paddle_scoreboard.increase()
		l_paddle_scoreboard.show()
		print(f"showing score : {l_paddle_scoreboard.score}")
		ball.goto(0, 0)
		x_direction=random.choice([1])
		y_direction=random.choice([-1,1])
		print(f"random{x_direction,y_direction}")
	elif ball.xcor() <=-360:
		print("1 point for LEFT Paddle")
		r_paddle_scoreboard.increase()
		r_paddle_scoreboard.show()
		print(f"showing score : {r_paddle_scoreboard.score}")
		ball.goto(0,0)
		x_direction=random.choice([-1])
		y_direction=random.choice([-1,1])
		print(f"random{x_direction,y_direction}")





screen.exitonclick()
