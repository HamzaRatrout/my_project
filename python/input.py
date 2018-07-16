import turtle
turtle.shape("turtle")
input=1234
if(input==1):
	#draw a square
	for x in range(4):
	     turtle.forward(100)
	     turtle.left(90)
elif(input==2):
	#draw a circle
	turtle.circle(100)
elif(input==3):
	#draw a triangle
	for x in range(3):
		turtle.forward(100)
		turtle.left(120)
else:
	#draw a green flag
	turtle.left(90)
	turtle.penup()
	turtle.backward(100)
	turtle.pendown()
	turtle.forward(300)
	turtle.right(90)
	turtle.fillcolor("green")
	turtle.begin_fill()
	turtle.forward(150)
	turtle.right(90)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(150)
	turtle.end_fill()
turtle.exitonclick()