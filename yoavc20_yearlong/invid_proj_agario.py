import turtle 
from turtle import Turtle
import random
import math
turtle.penup()
class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r, color ): # r = radius
		self.turtle = turtle.Turtle()
		#Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.r = r 
		self.color(color)
		#self.speed(speed)
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
	def move(self, screen_width, screen_height):
		current_x = self.xcor()
		new_x = current_x + dx
		current_y= self.ycor()
		new_y = current_y + dy
		right_side_ball = new_x + r
		left_side_ball = new_x - r
		upper_side_ball = new_y + r
		down_side_ball = new_y - r
		if new_x >= screen_width or new_x <= -screen_width:
			self.dx=-self.dx
			new_x=current_x+self.dx
		if new_y >= screen_height or new_y <= -screen_height:
			self.dy=-self.dy
			new_y=current_y+self.dy
		self.goto(new_x, new_y)

ball = Ball(0,0 ,5, 5 , 100, "red")
ball.move(100,100)

while True:
	ball1.move(300,300)
	ball2.move(300,300)




#turtle.mainloop()