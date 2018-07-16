import turtle
from random import randint


########### Setup sreen conditions #######################################
turtle.shape("turtle")
turtle.bgcolor("black")
turtle.speed(0)
turtle.listen()


############ Declare global variables ####################################
radius = 50


############ Define funtions #############################################

def random_pen_color():
	r = randint(0, 255) # TODO: lookup how python randint works!
	g = randint(0, 255)
	b = randint(0, 255)
	turtle.colormode(255)
	turtle.pencolor(r,g,b)

def draw_circle(x,y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	
	random_pen_color()
	turtle.circle(radius)


def clear_screen():
	turtle.clear()

# TODO: What other functions do you want?

############ Main ###########################################################

# TODO: Change main however you want! Be creative! 
# Look up documentation to understand how each of these functions work

turtle.onscreenclick(draw_circle)  # if user clicks anywhere on screen, draw_circle() is called
turtle.onkey(clear_screen, "c")	   # if user presses the 'c' key, clear_screen is called


turtle.done()