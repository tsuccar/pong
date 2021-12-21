from turtle import Turtle, Screen


# SCREEN
# This could be a separate file just for the screen
#

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)   #  when tracer is turned off. Turtle requires that it be followed by update()
pong_net = []

for index in range(23):
	new_dot = Turtle("square")
	new_dot.color("white")
	new_dot.speed("fastest")
	new_dot.shapesize(1, 0.2, 1)
	new_dot.penup()
	new_dot.goto (0,-305 +index*30)
	pong_net.append(new_dot)

screen.update()




















screen.exitonclick()