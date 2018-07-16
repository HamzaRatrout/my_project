import turtle
turtle.shape("turtle")
#variables
length=50
angle=45
turtle.penup()
turtle.backward(300)
turtle.pendown()
for x in range(6):
	if((x > 2)==0):
		#draw valley
		turtle.right(angle)
		turtle.forward(length)
		turtle.left(2*angle)
		turtle.forward(length)
		turtle.right(angle)
	else:
		#draw mountain
		turtle.left(angle)
		turtle.forward(length)
		turtle.right(2*angle)
		turtle.forward(length)
		turtle.left(angle)
turtle.exitonclick()