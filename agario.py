import turtle
import time
import random
from ball import Ball
turtle.tracer(0)
turtle.ht()
# needed variables
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
# myball variables
INIT_MYBALL_X = 0
INIT_MYBALL_Y = 0
INIT_MYBALL_DX = 0
INIT_MYBALL_DY = 0
INIT_MYBALL_RADIUS = 5
INIT_MYBALL_COLOR = 'BLUE'
# other balls 
NUMBER_OF_BALLS = 1
MINIMUM_BALL_RADIUS = 2
MAXIMUM_BALL_RADIUS = 20
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
# Creating my ball
MY_BALL = Ball(INIT_MYBALL_X,INIT_MYBALL_Y,INIT_MYBALL_DX,INIT_MYBALL_DY,INIT_MYBALL_RADIUS,INIT_MYBALL_RADIUS)
# others
BALLS = []