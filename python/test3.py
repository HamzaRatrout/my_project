import turtle 
from turtle import Turtle
from turtle import *
import random
colormode(255)
# turtle.speed(100)
class Hexagon(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
	turtle.begin_poly()
	turtle.penup()
	turtle.fd(100)
	turtle.right(60)
	turtle.fd(100)
	turtle.right(60)
	turtle.fd(100)
	turtle.right(60)
	turtle.fd(100)
	turtle.right(60)
	turtle.fd(100)
	turtle.right(60)
	turtle.fd(100)
	turtle.right(60)
	turtle.end_poly()
	shape=turtle.get_poly()
	register_shape("hexagon",shape)
	turtle.shape("hexagon")
	def random_color(self):
		r=random.randint(0,255)
		g=random.randint(0,255)
		b=random.randint(0,255)
		self.color(r,g,b)

hexa=Hexagon(100)
hexa.random_color()
while True:
	turtle.fd(500)
	turtle.bk(500)
turtle.exitonclick()