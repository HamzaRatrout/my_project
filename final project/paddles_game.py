 #imports
import pygame
import sys
import time
import random
from pygame.locals import *
#variables
play_song = True
score1=0
score2=0
final_score1=0
final_score2=0
WHITE = (255, 255, 255)
RED=(255,0,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
final_score1_color=WHITE
final_score2_color=WHITE
score1_color=BLUE
score2_color=RED
ball_color=GREEN
result_y=250
ball_radius=25
paddle1_y=225
paddle2_y=225
paddle1_x=12
paddle2_x=868
new_paddle1_y=225
new_paddle2_y=225
new_paddle1_x=12
new_paddle2_x=868
xdirection="forward"
ydirection="upward"
x=450
y=300
first_x=450
first_y=300
running=False
score_running=False
screen_width=900
screen_height=600
x_velocity=random.randint(1,2)
y_velocity=random.randint(1,2)
#SCREEN
pygame.display.set_caption("paddles game")
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(BLACK)
 
#FUNCTIONS

def draw_rectangle(x, y, width, height, color):
	pygame.draw.rect(screen, color, (x, y, width, height))
def draw_circle(x, y, radius, color):
	pygame.draw.circle(screen, color, (int(x), int(y)), radius)
def final_result():
	myfont = pygame.font.SysFont("monospace", 100)
	label = myfont.render(str(final_score1),1,final_score1_color)
	screen.blit(label, (20, 30))
	myfont = pygame.font.SysFont("monospace", 100)
	label = myfont.render(str(final_score2),1,final_score2_color)
	screen.blit(label, (830, 30))
def result():
	myfont = pygame.font.SysFont("monospace", 100)
	label = myfont.render(str(score1),1,score1_color)
	screen.blit(label, (300, result_y))
	myfont = pygame.font.SysFont("monospace", 100)
	label = myfont.render(str(score2),1,score2_color)
	screen.blit(label, (550, result_y))
def return_ball(x,y,running):
	if x >= screen_width+ball_radius :
		x = first_x
		y = first_y
		running = False
		draw_circle(first_x,first_y,ball_radius,ball_color)
	if x <= 0-ball_radius:
		x = first_x
		y = first_y
		running=False
		draw_circle(first_x,first_y,ball_radius,ball_color)
	return x,y,running

pygame.init()

while True:
	keys = pygame.key.get_pressed()
	screen.fill(BLACK)
	#PADDLE1
	paddle1=draw_rectangle(paddle1_x,paddle1_y,20,150,BLUE)
	#PADDLE2
	paddle2=draw_rectangle(paddle2_x,paddle2_y,20,150,RED)
	#BALL
	if keys[pygame.K_o]:
		running=True
	if keys[pygame.K_i]:
		running=False
	if running==True:
		draw_circle(x,y,ball_radius,ball_color)
		#ball bouncing
		if (ydirection=="upward"):
			y=y-y_velocity
			if (y<=ball_radius):
				ydirection="downward"
		if (ydirection=="downward"):
			y=y+y_velocity
			
			if (y>=screen_height-ball_radius):
				ydirection="upward"
		if (xdirection=="forward"):
			x=x+x_velocity
		
			if y>=paddle2_y and y<=paddle2_y+150 and x==paddle2_x:
				xdirection="backward"
				y_velocity = random.randint(1,2)
				x_velocity = random.randint(1,2)
				c_sound = pygame.mixer.music.load("POP.WAV")
				pygame.mixer.music.play()
		if (xdirection=="backward"):
			x=x-x_velocity	
			#paddle_bouncing
			if y>=paddle1_y and y<=paddle1_y+150 and x==paddle1_x+20:
				xdirection="forward"
				y_velocity = random.randint(1,2)
				x_velocity = random.randint(1,2)
				c_sound = pygame.mixer.music.load("POP.WAV")
				pygame.mixer.music.play()
		x,y,running=return_ball(x,y,running)
		
		#scoring
	if x== screen_width:
		score1+=1
		v_sound = pygame.mixer.Sound("applause2.wav")
		pygame.mixer.Sound.play(v_sound)

	if x== 0:
		score2+=1
		v_sound = pygame.mixer.Sound("applause2.wav")
		pygame.mixer.Sound.play(v_sound)
	if score1 ==3:

		final_score1+=1
		score1=0
		score2=0

	if score2 == 3:
		
		final_score2 +=1
		score1=0
		score2=0
	

	draw_circle(x,y,ball_radius,ball_color)
	#paddle movement
	if keys[pygame.K_w]:
		if paddle1_y >= 10:
			paddle1_y -=2

	if keys[pygame.K_s]:
		if paddle1_y <= 440:
			paddle1_y +=2
	if keys[pygame.K_UP]:
		if paddle2_y >= 10:
			paddle2_y -=2
	if keys[pygame.K_DOWN]:
		if paddle2_y <= 440:
			paddle2_y +=2
		
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	if final_score1 >= 3:
		final_score1_color=BLUE
		final_score2_color=BLUE
		score2_color=BLUE
		ball_color=BLUE
		screen.fill(BLUE)
		myfont = pygame.font.SysFont("monospace", 100)
		label = myfont.render("BLUE WINS!",1,WHITE)
		screen.blit(label, (175, 250))
		if play_song:
			s_sound = pygame.mixer.Sound("VICTORY.WAV")
			pygame.mixer.Sound.play(s_sound)
			play_song = False
	elif final_score2 >= 3:
		final_score1_color=RED
		final_score2_color=RED
		score1_color=RED
		ball_color=RED
		screen.fill(RED)
		myfont = pygame.font.SysFont("monospace", 100)
		label = myfont.render("RED WINS!",1,WHITE)
		screen.blit(label, (210, 250))
		if play_song:
			s_sound = pygame.mixer.Sound("VICTORY.WAV")
			pygame.mixer.Sound.play(s_sound)
			play_song = False
	#### Make animations
	
	#restart
	if keys[pygame.K_r]:
		score_running=True
		score1=0
		score2=0
		final_score1=0
		final_score2=0
		final_score1_color=WHITE
		final_score2_color=WHITE
		ball_color=GREEN
		score1_color=BLUE
		score2_color=RED
		paddle1_y=new_paddle1_y
		paddle2_y=new_paddle2_y
		paddle1_x=new_paddle1_x
		paddle2_x=new_paddle2_x
	#hiding the score
	if score_running==True:
		result()
		final_result()
	#reducing the ball_radius
	if final_score1 == 1 or final_score2 ==1:
		ball_radius=20
	elif final_score1 == 2 or final_score2 ==2:
		ball_radius=15
	else:
		ball_radius=25
	
	
	if play_song == True:
		result()
		final_result()
	pygame.display.update()
	time.sleep(0.001)
	

