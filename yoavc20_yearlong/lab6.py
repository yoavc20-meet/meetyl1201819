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

		R = random.randint(0, 255)
		B = random.randint(0, 255)
		G = random.randint(0, 255)
		self.color(R, B, G)	
		
square1 = Square(25)
square1.change_color()





class Hexagon(Turtle):
	def __init__(self,size):
		Turtle. __init__(self)
		#self.size(size)
		turtle.home()
		turtle.penup()
		turtle.hideturtle()
		turtle.begin_poly()
		turtle.fd(size)
		turtle.left(60)
		turtle.fd(size)
		turtle.left(60)		
		turtle.fd(size)
		turtle.left(60)		
		turtle.fd(size)
		turtle.left(60)		
		turtle.fd(size)
		turtle.left(60)
		turtle.fd(size)
		turtle.end_poly()
		p = turtle.get_poly()
		turtle.register_shape("Hexagon" , p)
		self.penup()
		self.shape("Hexagon")

	def jump(self):
		self.left(90)
		self.fd(100)

a = Hexagon(20)
a.jump()









turtle.mainloop()