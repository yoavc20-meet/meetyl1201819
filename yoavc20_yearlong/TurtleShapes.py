import turtle
#exercise 1
#turtle.right(45)
#turtle.forward(60)
#turtle.left(150)
#turtle.forward(60)
#def CopyPaste():
#	turtle.right(78)
#	turtle.left(150)
#	turtle.forward(60)
#CopyPaste()
#CopyPaste()
#CopyPaste()
#CopyPaste()
angle = 145
length = 100
def draw_star(angle, length):
	for i in range(5):
		turtle.left(angle)
		turtle.forward(length)

draw_star(angle, length)












turtle.mainloop()
