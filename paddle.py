from turtle import Turtle

MOVE_DISTANCE=40
UP=90
DOWN=270

class Paddle(Turtle):
	def __init__(self,starting_point):
		super().__init__()
		self.shape("square")
		self.color("white")
		self.speed("fastest")
		self.shapesize(1,5,1)
		self.penup()
		self.goto(starting_point)
		self.setheading(UP)

	def up (self):
		self.forward(MOVE_DISTANCE)

	def down (self):
		self.backward(MOVE_DISTANCE)
