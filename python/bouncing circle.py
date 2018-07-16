import pygame
import sys
import time
from pygame.locals import*
pygame.init()
pygame.display.set_caption("Basics")
screen = pygame.display.set_mode((500,400))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
x=40
y=175
xdirection="forward"
ydirection="upward"
pygame.draw.circle(screen,RED,(x,y),40,0)
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	screen.fill(BLACK)
	if (ydirection=="upward"):
		y=y-5
		if (y<=40):
			ydirection="downward"
	if (ydirection=="downward"):
		y=y+5
		if (y>=360):
			ydirection="upward"
	if (xdirection=="forward"):
		x=x+5
		if (x>=460):
			xdirection="backward"
	if (xdirection=="backward"):
		x=x-5
		if (x<=40):
			xdirection="forward"

	pygame.draw.circle(screen,RED,(x,y),40,0)
	pygame.display.update()
	time.sleep(0.01)