import random
while True:
	a=input("enter r to roll dice or q to quit")
	if(a=='r'):
		r=random.randint(1,6)
		print(r)
	else:
		break