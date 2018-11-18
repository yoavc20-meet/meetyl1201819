import turtle
from turtle import Turtle

class Square(Turtle):
	def __init__(self, size, random_color):
		Turtle. __init__(self)
		self.size(size)
		self.shape("Square")
		self.random_color(random_color)
		