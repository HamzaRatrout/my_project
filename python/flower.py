import turtle
turtle.shape("turtle")
turtle.pensize(1)
def draw_circle (color,radius):
	turtle.fillcolor(color)
	turtle.begin_fill()
	turtle.circle(radius)
	turtle.end_fill()
	turtle.left(60)
def draw_flower():
	draw_circle("red",100)
	draw_circle("orange",100)
	draw_circle("yellow",100)
	draw_circle("green",100)
	draw_circle("blue",100)
	draw_circle("black",100)
turtle.penup()
turtle.backward(400)
turtle.pendown()
draw_flower()
turtle.penup()
turtle.forward(400)
turtle.pendown
draw_flower()
turtle.penup()
turtle.forward(400)
turtle.pendown
draw_flower()
turtle.exitonclick()