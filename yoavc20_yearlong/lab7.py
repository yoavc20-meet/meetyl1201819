import turtle
from turtle import Turtle
import random
import math
turtle.colormode(255)

z = 300
turtle.speed(10)
turtle.penup()
turtle.goto(-z,-z)
turtle.pendown()
turtle.goto(z,-z)
turtle.goto(z,z)
turtle.goto(-z,z)
turtle.goto(-z,-z)

turtle.penup()
turtle.goto(0,0)
class Ball(Turtle):
	def __init__(self, x, y, dx, dy, radius, color, speed ):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
	def move(self, width, height):
		oldx=self.xcor()
		oldy=self.ycor()
		newx=oldx+self.dx
		newy=oldy+self.dy
		if newx >= width or newx <= -width:
			self.dx=-self.dx
			newx=oldx+self.dx
		if newy >= height or newy <= -height:
			self.dy=-self.dy
			newy=oldy+self.dy
		self.goto(newx, newy)

ball1 = Ball(50, 30, 35, 30, 35, "red", 10)
ball2 = Ball(50, 14, 25,20, 30, "yellow", 7)

#ball1.move(300,300)
#ball2.move(300,300)
def check_collision( ball2, ball1):
	x1 = ball1.xcor()
	x2 = ball2.xcor()
	y1 = ball1.ycor()
	y2 = ball2.ycor()
	#r1 = ball1.radius()
	#r2 = ball2.radius()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if (D< ball1.radius+ball2.radius):
		return True
	else: 
		return False


while True:
	ball1.move(300,300)
	ball2.move(300,300)
	if check_collision( ball1, ball2) == True :
		R = random.randint(0, 255)
		G = random.randint(0, 255)
		B = random.randint(0, 255)
		turtle.bgcolor(R, B, G)	
		R = random.randint(0, 255)
		G = random.randint(0, 255)
		B = random.randint(0, 255)
		ball1.color(R, B, G)
		R = random.randint(0, 255)
		G = random.randint(0, 255)
		B = random.randint(0, 255)
		ball2.color(R, B, G)

balls = [ball1, ball2]
if balls[0] < balls[1]:
	balls[0].randint()








turtle.mainloop()