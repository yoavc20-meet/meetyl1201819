import turtle 
from turtle import Turtle
import random
import math
import time


turtle.penup()

class Ball(turtle.Turtle):
	def __init__(self, x, y, dx, dy, r, color ): # r = radius
		#self.turtle = turtle.Turtle()
		turtle.Turtle.__init__(self)
		self.pu()
		#self.my_turtle = turtle.clone()
		#Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(r/10)
		self.r = r 
		self.color(color)
		self.showturtle()
		#self.speed(speed)
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
	def move(self, screen_width, screen_height):
		turtle.pu()
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y= self.ycor()
		new_y = current_y + self.dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		upper_side_ball = new_y + self.r
		down_side_ball = new_y - self.r
		if new_x >= screen_width or new_x <= -screen_width:
			self.dx=-self.dx
			new_x=current_x+self.dx
		if new_y >= screen_height or new_y <= -screen_height:
			self.dy=-self.dy
			new_y=current_y+self.dy
		self.goto(new_x, new_y)

# ball = Ball(0,0 ,5, 5 , 100, "red")

# turtle.mainloop()
#ball.move(100,100)

#while True:
#	ball1.move(300,300)
#	ball2.move(300,300)




#turtle.mainloop()