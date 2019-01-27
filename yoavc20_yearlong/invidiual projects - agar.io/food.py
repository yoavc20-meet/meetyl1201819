import turtle
from turtle import Turtle

class Food(Turtle):
	def __init__(self, x, y, color, r):
		Turtle.__init__(self)
		self.r = r
		self.penup()
		self.shape("circle")
		self.goto(x, y)
		self.color(color)
		self.shapesize(r/10)

	def eat(self, x, y, color, r):
		self.goto(x, y)
		self.color(color)
		self.shapesize(r/10)
				



