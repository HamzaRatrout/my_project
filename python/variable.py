import turtle 
turtle.shape("turtle")
side_length=100
angle=90
for x in range(4):
	turtle.forward(side_length)
	turtle.left(angle)
turtle.exitonclick()