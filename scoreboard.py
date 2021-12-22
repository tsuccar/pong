from turtle import Turtle
FONT_SIZE = 20
FONT=("Arial", FONT_SIZE, "normal")
class Scoreboard(Turtle):
	
	def __init__(self,position):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.color('white')
		self.goto(position)
		self.score=0
	
	
	def increase(self):
		self.score += 1
		self.clear()
		self.write(self.score, font=FONT)
	def show (self):
		self.clear()
		self.write(self.score, font=FONT)


#self.l_pad_score}:{self.r_pad_score}