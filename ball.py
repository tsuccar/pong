from turtle import Turtle
FORWARD_DISTANCE=15

class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("white")
		self.penup()

	def move(self,x_direction,y_direction):
			new_x = self.xcor() + (FORWARD_DISTANCE*x_direction)
			new_y = self.ycor() + (FORWARD_DISTANCE*y_direction)
			self.setx(new_x)
			self.sety(new_y)


	
	
	
