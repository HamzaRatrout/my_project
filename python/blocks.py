import turtle , time
from turtle import Turtle
screen_width=285
running=True
turtle.hideturtle()
turtle.tracer(0)
screen_width=285
class shape(Turtle):
	def __init__(self,size,color,shape,x,y):
		Turtle.__init__(self)
		self.shapesize(size)
		self.color(color)
		self.pu()
		# screen.register_shape("rectangle",(0,0),(0,100),(100,0),(100,100)
		self.shape(shape)
		self.x = x
		self.y = y
		self.goto(x,y)
		
class square(shape):
	def moving(self,velocity):
		while running:
			
			

square1 = square(5,"Red","square",0,0)
while running== True:
	turtle.getscreen().update()
	time.sleep(0.02)
# square.moving(3,0)
turtle.exitonclick()
