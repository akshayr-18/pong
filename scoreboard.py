from turtle import Turtle
class ScoreBoard(Turtle):
	def __init__(self,coordinates):
		super().__init__()
		self.color("white")
		self.penup()
		self.score=0
		self.goto(coordinates)
		self.hideturtle()
		self.updatescoreboard()
	
	def updatescoreboard(self):
		self.write(f"{self.score}",align="center",font=("Courier",20,"normal"))
	
	def inc_score(self):
		self.score+=1
		self.clear()
		self.updatescoreboard()
	
	def gameover(self):
		self.goto(0,0)
		self.write(f"GAME OVER.",align="center",font=("Courier",50,"normal"))
