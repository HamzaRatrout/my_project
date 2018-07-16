# exercise 1
def exercise_1():
	numbers=[5,10,15,20,25]
	x=numbers[0]
	y=numbers[-1]
	new=[x,y]
	print new
def exercise_2():
	a=[1,6,2,3,5,7,9,89,2.1,109]
	b=[]
	i=0
	for x in range (len(a)):
		if a[i] < 5:
			b.append(a[i])
		i=i+1
	print b
def exercise_3():
	a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	answer = []
	i=[0]
	for i in a:
		if i in b:
			answer.append(i)
	print answer
def exercise_4(x):
	if x%2 ==0:
		print False 
	else:
		print True
