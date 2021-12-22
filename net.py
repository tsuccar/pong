from turtle import Turtle

class Net(Turtle):
	def __init__(self):
		super().__init__()
		self.pong_net = []
		self.net_setup()
	def net_setup(self):
		for index in range(23):
			new_dot = Turtle("square")
			new_dot.color("white")
			new_dot.speed("fastest")
			new_dot.shapesize(1, 0.2, 1)
			new_dot.penup()
			new_dot.goto (0,-305 +index*30)
		self.pong_net.append(new_dot)
