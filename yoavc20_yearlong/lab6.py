import turtle
from turtle import Turtle
import random

turtle.colormode(255)
'''
R = 0
B = 0
G = 0
'''
class Square(Turtle):
	def __init__(self, size):
		Turtle. __init__(self)
		self.shapesize(size)
		self.shape("square")
	def change_color(self):
#		self.random_color = random_color
		R = random.randint(0, 255)
		B = random.randint(0, 255)
		G = random.randint(0, 255)
		self.color(R, B, G)	
		#turtle.color(R, B, G)

	'''
	def pick_color():
		self.random_color = random_color	
		return choice(["red", "yellow", "blue"])
'''
#print(random.random())
square1 = Square(25)
square1.change_color()




'''
class Hexagon(Turtle):
	def __init__(self,size):
		Turtle. __init__(self)
		self.size(size)
'''



turtle.mainloop()