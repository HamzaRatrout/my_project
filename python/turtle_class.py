import turtle
from turtle import Turtle
class Ball(Turtle):
	def __init__(self,size,color,x,y):
			Turtle.__init__(self)
			self.color(color)
			self.shapesize(size)
			self.shape("circle")
class ball2(Ball):
	def ball(self,pen_color,x,y):
		self.pencolor(pen_color)
class ball3(Ball):
	def ball(self,pen_color,x,y):
		self.pencolor(pen_color)
circle1 = ball2(3,"black",40,8)
circle2 = ball3(3,"black",90,100)
circle1.ball("blue",400,8)
circle2.ball("black",60,80)
turtle.fd(100)
turtle.exitonclick()