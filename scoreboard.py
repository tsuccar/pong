from turtle import Turtle
FONT_SIZE = 20

class Scoreboard(Turtle):
	
	def __init__(self):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.color('white')
		self.goto(0,0)
		self.l_pad_score=0
		self.r_pad_score=0
	
	def show_value(self, r_pad=0,l_pad=0):
		self.l_pad_score += l_pad
		self.r_pad_score += r_pad
		self.write(f"test", font=("Arial", FONT_SIZE, "normal"))



#self.l_pad_score}:{self.r_pad_score}