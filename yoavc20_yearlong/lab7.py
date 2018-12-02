import turtle
from turtle import Turtle
import random

turtle.colormode(255)

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
	def check_collision(self, ball1, ball2):
		R = random.randint(0, 255)
		B = random.randint(0, 255)
		G = random.randint(0, 255)
		turtle.bgcolor(R, B, G)	
ball1 = Ball(50, "red", 10)
ball2 = Ball(40, "yellow", 7)
ball1.check_collision( ball1, ball2)










turtle.mainloop()