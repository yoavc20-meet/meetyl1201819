import turtle
import time
import random
import math
from ball import Ball
turtle.tracer(0,0)
turtle.hideturtle()
turtle.penup()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
MY_BALL = Ball(40,0 ,0, 5 , 50, "pink")
NUMBERS_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []
for i in range(NUMBERS_OF_BALLS):
	x = random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(),random.random())
	MY_BALL2 = Ball(x, y, dx, dy, radius, color)
	BALLS.append(MY_BALL2)


def collide(ball_a,ball_b): 
	if ball_a == ball_b:
		return False
	else: #ball_a != ball_b
		return True
	x1 = ball_a.xcor()
	x2 = ball_b.xcor()
	y1 = ball_a.ycor()
	y2 = ball_b.ycor()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if ((D+ 10) <= ball_a.r+ball_b.r):
		return True
		
		turtle.update()
	else: 
		return False

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b) == True:
				r1 = ball_a.r 
				r2 = ball_b.r

				if ball_a.r> ball_b.r:
					ball_a.r += 1
					ball_a.shapesize((r1+1)/10)

					new_x_cor = random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
					new_y_cor = random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
					x_speed =random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					y_speed =random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)	
					new_radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
					new_color = (random.random(), random.random(),random.random())
					while x_speed == 0 :
						x_speed =random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					while y_speed == 0 :
						y_speed =random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
					ball_b.goto(new_x_cor, new_y_cor)
					ball_b.dx =x_speed
					ball_b.dy =y_speed
					ball_b.r= new_radius
					ball_b.color(new_color)
					ball_b.shapesize(new_radius/10)

turtle.pu()

while RUNNING:
	turtle.pu()
	turtle.update()
	# MY_BALL2.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	# for MY_BALL2 in BALLS:
	# 	MY_BALL2.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	time.sleep(SLEEP)
	check_all_balls_collision() 