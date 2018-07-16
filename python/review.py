import turtle
turtle.shape("turtle")
length = 200
width = 100
for x in range(2):
	turtle.forward(length)
	turtle.left(90)
	turtle.forward(width)
	turtle.left(90)
turtle.exitonclick()