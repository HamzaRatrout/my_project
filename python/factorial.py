# def factorial(n):
# 	if n == 1:
# 		return 1
# 	else:
# 		return n * factorial(n-1)
# def F(n):
# 	if n == 0:
# 		return 0
# 	elif n == 1:
# 		return 1
# 	else:
# 		return F(n-1) + F(n-2)
# print F(10)
import turtle as t
t.shape("circle")
t.speed(110)
t.fd(100)
t.left(90)
t.circle(100)
t.right(90)
t.fd(100)
t.left(90)
t.circle(200)
t.goto(0,0)
t.right(90)
def triangle():
	for x in range (10):
		t.color("Red")
		t.fd(200)
		t.left(153)
		t.fd(138)
		t.left(27)
		t.goto(0,0)
		t.right(140)

triangle()
t.mainloop()