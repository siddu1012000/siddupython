import random
while True:
	a=input("enter r to rooll dice or q to quit")
	if(a=='r'):
		r=random.randint(1,6)
		print(r)
	else:
		break