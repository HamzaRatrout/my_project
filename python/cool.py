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
pygame.draw.filled_trigon(screen,10,20,60,80,200,340,RED)
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	time.sleep(0.001)