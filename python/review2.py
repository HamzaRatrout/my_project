# list1=["can","we","mix","value
import turtle
turtle.speed(100)
for x in range(8):
	for i in range(8):
		if x%2==0:
			if i%2==0:
				color='white'
			else:
				color='black'
		else:
			if i%2==0:
				color='black'
			else:
				color='white'

		turtle.fillcolor(color)
		turtle.begin_fill()
		for m in range (4):
			turtle.forward(30)
			turtle.right(90)
		turtle.end_fill()
		turtle.fd(30)
	turtle.right(90)
	turtle.fd(30)
	turtle.right(90)
	turtle.fd(30*8)
	turtle.right(180)
turtle.exitonclick()
x=25
y=13
z=9
def cool(x,y,z):
	print x
	return y+z
cool(x,y,z)