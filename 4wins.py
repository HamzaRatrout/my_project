import turtle , time
from turtle import Turtle
import math
turtle.terminator()
running=True
SCREEM_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

ROW_NUMBER=7
COLUMN_NUMBER=6
# x=660
# y=275
turtle.tracer(0)

turtle.bgcolor("Black")
# turtle.setup(width=SCREEM_WIDTH, height =SCREEN_HEIGHT , startx=0 , starty=0)
turtle.hideturtle()
# turtle.tracer(0)


HOLES=[]
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
for p in range(21):
	coin= coins ("circle" , 50 , "WHITE",0,0,0)
	coin.xy(-500,0,"RED")
	coin.followmouse()
for k in range(21):
	coin= coins ("circle" , 50 , "WHITE",0,0,0)
	coin.xy(500,0,"BLUE")
	coin.followmouse()
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
hole_circles=hole_circles(SCREEM_WIDTH,SCREEN_HEIGHT)


for p in range(21): 
	coin= coins ("circle" , 50 , "WHITE",0,0,0)
	coin.xy(-500,0,"RED")
	coin.followmouse()
for k in range(21):
	coin= coins ("circle" , 50 , "WHITE",0,0,0)
	coin.xy(500,0,"BLUE")
	coin.followmouse()
for hole13 in (HOLES):
		hole13.onclick(coin.goto)
# class coins(Circles):
# 	def xy(self,x,new_y,color):
# 		self.pu()
# 		self.goto(x,new_y)
# 		self.color(color)
# 	def followmouse(self):
# 		turtle.pu()
# 		coin.ondrag(coin.goto)


coin2= coins ("circle" , 50 , "YELLOW",0,0,0)
coin2.xy(-590,300,"YELLOW")
# for k in range(21):
# 	coin= coins ("circle" , 50 , "WHITE",0,0,0)
# 	coin.xy(500,0,"BLUE")
# 	coin.followmouse()
# for p in range(21):
# 	coin= coins ("circle" , 50 , "WHITE",0,0,0)
# 	coin.xy(-500,0,"RED")
# 	coin.followmouse()
while running== True:
	turtle.getscreen().update()
	time.sleep(0.02)
print "hi"
turtle.exitonclick()