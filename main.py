from turtle import Screen, Turtle
from random import randint
from paddles import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
s=Screen()
s.listen()
s.setup(width=800,height=600)
s.tracer(0)
s.bgcolor("black")
s.title("PONG")
lpaddle=Paddle((-350,0))
rpaddle=Paddle((350,0))
b=Ball()
b.move()
r=ScoreBoard((200,250))
l=ScoreBoard((-200,250))
s.onkey(rpaddle.move_up,"Up")
s.onkey(rpaddle.move_down,"Down")
s.onkey(lpaddle.move_up,"w")
s.onkey(lpaddle.move_down,"s")
game_is_on=True
while game_is_on:
	s.update()
	b.move()
	time.sleep(0.05)
	if b.ycor()>290 or b.ycor()<-290:
		b.bounce()
	elif (b.distance(lpaddle)<50 and b.xcor()<-330):
		l.inc_score()
		b.bounce_paddle()
	elif (b.distance(rpaddle)<50 and b.xcor()>330):
		r.inc_score()
		b.bounce_paddle()
	elif b.xcor()>380 or b.xcor()<-380:
		game_is_on=False
		
l.gameover()


		


s.exitonclick()
