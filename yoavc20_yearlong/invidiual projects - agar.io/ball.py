import turtle 
# from turtle import Turtle
import random
import math
import time


turtle.penup()
class Ball():
	def __init__(self, x, y, dx, dy, r, color ): # r = radius
		#self.turtle = turtle.Turtle()
		self.my_turtle = turtle.clone()
		#Turtle.__init__(self)
		self.my_turtle.shape("circle")
		self.my_turtle.shapesize(r/10)
		self.r = r 
		self.my_turtle.color(color)
		self.my_turtle.showturtle()
		#self.speed(speed)
		self.my_turtle.goto(x,y)
		self.dx = dx
		self.dy = dy
	def move(self, screen_width, screen_height):
		current_x = self.my_turtle.xcor()
		new_x = current_x + self.dx
		current_y= self.my_turtle.ycor()
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
		self.my_turtle.goto(new_x, new_y)

#ball = Ball(0,0 ,5, 5 , 100, "red")
#ball.move(100,100)

#while True:
#	ball1.move(300,300)
#	ball2.move(300,300)




#turtle.mainloop()