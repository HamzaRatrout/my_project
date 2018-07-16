from turtle import *


class Circles(Turtle):
	def __init__(self,shape,r,color,dx,dy,y):
		Turtle.__init__(self)
		self.shape("circle")
		self.r = r
		self.shapesize(r/10)
	
		self.color(color)
		self.dx=dx
		self.dy=dy
		self.y=y
	
class holes(Circles):
	def xy(self,x,y):
		self.pu()
		self.goto(x,y)

class coins(Circles):
	def xy(self,x,new_y,color):
		self.pu()
		self.goto(x,new_y)
		self.color(color)
	def followmouse(self):
		turtle.pu()
		coin.ondrag(coin.goto)
def hole_circles(x,y):
	for i in range (ROW_NUMBER):
		x=i*-110+SCREEM_WIDTH-10
		hole= holes ("circle" , 49.5 , "WHITE",0,0,0)
		for d in range (COLUMN_NUMBER):
			y=d*-110+SCREEN_HEIGHT
			hole13= holes ("circle" , 49.5 , "WHITE",0,0,0)
			hole13.xy(x,y)
			HOLES.append(hole13)
	for hole13 in (HOLES):
		hole13.onclick(coin.goto)