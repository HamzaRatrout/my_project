import turtle 
from turtle import Turtle
from turtle import *
import random
class Polygon(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		sides=random.randint(3,15)
		turtle.begin_poly()
		for x in range(sides):
			turtle.penup()
			turtle.fd(100)
			turtle.left(360/sides)
		turtle.end_poly()
		poly=turtle.get_poly()
		register_shape("polygon",poly)
		turtle.shape("polygon")
p = Polygon(4)
turtle.exitonclick()