from turtle import Turtle
class Paddle(Turtle):
	def __init__(self,coord):
		super().__init__()
		self.shape("square")
		self.left(90)
		self.goto(coord)
		self.resizemode("user")
		self.shapesize(stretch_wid=1,stretch_len=5)
		self.color("white")
		self.penup()
		
	def move_up(self):
		self.forward(20)
	
	def move_down(self):
		self.backward(20)
