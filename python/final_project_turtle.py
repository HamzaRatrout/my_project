import turtle
from random import randint
turtle.speed(100)
turtle.shape("turtle")
turtle.bgcolor("black")
turtle.listen()
turtle.speed(0)
radius=60
length=70
def random_pen_color():
	r = randint(0, 255) 
	g = randint(0, 255)
	b = randint(0, 255)
	turtle.colormode(255)
	turtle.pencolor(r,g,b)
def squares (x,y):
	turtle.speed(0)
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	random_pen_color()
	for i in range(10):
		for i in range(4):
			turtle.forward(40)
			turtle.left(90)
		turtle.left(36)
def circles (z,y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	random_pen_color
	for m in range(36):
		turtle.circle(40)
		turtle.left(10)
def random_shape():
	s = randint(0, 10)
	if (s%2==0):
		squares
	else:
		circles
def clear_screen():
	turtle.clear()
turtle.onscreenclick(squares)  
turtle.onkey(clear_screen, "c")	 
print "como estas"  
turtle.done()