import turtle 
from turtle import Turtle
from turtle import *
import random
colormode(255)
class Square(Rectangle):
	def __init__(self,size):
			Turtle.__init__(self)
			register_shape("square",((0,0),(size,0),(size,size),(0,size)))
			self.shape("square")
	def random_color(self):
		r=random.randint(0,255)
		g=random.randint(0,255)
		b=random.randint(0,255)
		self.color(r,g,b)
square = Square(200)
square.random_color()

class Hexagon(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
	for i in range(5):
		turtle.begin_poly()
		turtle.fd(100)
		turtle.left(60)
	turtle.end_poly()
	shape=turtle.get_poly()
	register_shape("hexagon",shape)
	turtle.shape("hexagon")
hexa=Hexagon(100)

turtle.exitonclick()