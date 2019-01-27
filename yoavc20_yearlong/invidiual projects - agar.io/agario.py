import turtle
import time
import random
import math
from ball import Ball
from food import Food
turtle.tracer(0,0)
turtle.setup(1500,1000)
turtle.hideturtle()
turtle.penup()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
MY_BALL = Ball(40,0 ,0, 0 , 10, "pink")
NUMBERS_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 20
MINIMUM_BALL_DX = -0.5
MAXIMUM_BALL_DX = 0.5
MINIMUM_BALL_DY = -0.5
MAXIMUM_BALL_DY = 0.5
NUMBERS_OF_FOODS = 20
FOOD = []
BALLS = []
for i in range(NUMBERS_OF_BALLS):
	x = random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.uniform(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.uniform(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(),random.random())
	MY_BALL2 = Ball(x, y, dx, dy, radius, color)
	BALLS.append(MY_BALL2)

for i in range(NUMBERS_OF_FOODS):
	x_cor = random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	y_cor = random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(),random.random())
	#food.eat(new_x_cor,new_y_cor, new_color, 4)= 
	new_Food = Food(x_cor, y_cor, color, 4)
	FOOD.append(new_Food)
def collide(ball_a,ball_b): 
	if ball_a == ball_b:
		return False
	
	x1 = ball_a.xcor()
	x2 = ball_b.xcor()
	y1 = ball_a.ycor()
	y2 = ball_b.ycor()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if ((D) <= ball_a.r+ball_b.r):
		return True
		
		#turtle.update()
	else: 
		return False

def check_all_balls_collision(): # creates a funtion that checks all the balls collision
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b) == True:
				r1 = ball_a.r 
				r2 = ball_b.r
				new_x_cor = random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				new_y_cor = random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				while new_x_cor== MY_BALL.xcor() and new_y_cor== MY_BALL.ycor():
					new_x_cor = random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
					new_y_cor = random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				
				x_speed =random.uniform(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				y_speed =random.uniform(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)	
				new_radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				new_color = (random.random(), random.random(),random.random())
				while x_speed == 0 :
					x_speed =random.uniform(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				while y_speed == 0 :
					y_speed =random.uniform(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				if ball_a.r> ball_b.r:
					ball_a.r +=1
					ball_a.shapesize((r1+1)/10)
					ball_b.goto(new_x_cor, new_y_cor)
					ball_b.dx =x_speed
					ball_b.dy =y_speed
					ball_b.r= new_radius
					ball_b.color(new_color)
					ball_b.shapesize(new_radius/10)
				elif ball_a.r < ball_b.r : 
					ball_b.r += 1
					ball_b.shapesize((r2+1)/10)
					ball_a.goto(new_x_cor, new_y_cor)
					ball_a.dx =x_speed
					ball_a.dy =y_speed
					ball_a.r= new_radius
					ball_a.color(new_color)
					ball_a.shapesize(new_radius/10)
def food_collision():
	for food in FOOD:
		for ball in BALLS:
			if(collide(ball, food)):
				new_x_cor = random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				new_y_cor = random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				new_color = (random.random(), random.random(),random.random())
				food.eat(new_x_cor,new_y_cor, new_color, 4)
				ball.r += 1
				ball.shapesize(MY_BALL.r/10)

def check_my_food():
	for food in FOOD:
		if(collide(MY_BALL, food)):
			new_x_cor = random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			new_y_cor = random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			new_color = (random.random(), random.random(),random.random())
			food.eat(new_x_cor,new_y_cor, new_color, 4)
			MY_BALL.r += 1
			MY_BALL.shapesize(MY_BALL.r/10)
'''
def end_game():
	for ball in BALLS:
		ball.hideturtle()
		print("GAME OVER!")
'''
def check_myball_collision():# creates a function that checks the user's ball collision
	for ball in BALLS:
		if collide(MY_BALL, ball)== True:
			myBall_r = MY_BALL.r
			ball_r = ball.r

			new_x_cor = random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			new_y_cor = random.randint( -SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			x_speed =random.uniform(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
			y_speed =random.uniform(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)	
			new_radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
			new_color = (random.random(), random.random(),random.random())
			while x_speed == 0 :
				x_speed =random.uniform(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
			while y_speed == 0 :
				y_speed =random.uniform(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
			if myBall_r< ball_r:
			#	end_game()
				print('colliding with bigger ball')
				return True
			elif myBall_r > ball_r:
				MY_BALL.r += 2
				MY_BALL.shapesize((myBall_r+2)/10)
				# MY_BALL.r+=4
				ball.goto(new_x_cor, new_y_cor)
				ball.dx =x_speed
				ball.dy =y_speed
				ball.r= new_radius
				ball.color(new_color)
				ball.shapesize(new_radius/10)
	return False

#a function for moving the ball
def movearound(event):
	x = event.x - SCREEN_WIDTH
	y = SCREEN_HEIGHT - event.y
	MY_BALL.goto(x,y)
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()


while RUNNING:
	
	if SCREEN_WIDTH!= turtle.getcanvas().winfo_width()/2:
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
	if SCREEN_HEIGHT!= turtle.getcanvas().winfo_height()/2:
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
	food_collision()
	check_my_food()

	#turtle.pu()
##### the problem is here




	MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	check_all_balls_collision() 
	# check_myball_collision()
	# print(check_myball_collision())

	if check_myball_collision() == True:
		RUNNING = False
		turtle.write("GAME OVER!")
	for MY_BALL2 in BALLS:
	 	MY_BALL2.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	turtle.update()

	# time.sleep(SLEEP)
turtle.mainloop()