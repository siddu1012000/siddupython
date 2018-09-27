import random
print("welcome to snake and ladder")
n=0
while (n<=100):
	a=input("enter r to roll dice or any char to quit")
	if(a=='r'):
		r=random.randint(1,6)
		print("u got",r)
		n=n+r
		print("ur score is",n)
		if(n>=100):
			
			if(n==100):
				print("u won the game")
				break
			n=n-r
		if(n==8):
			n=37
			print("u got a ladder u are now",n)
		elif(n==11):
			n=2
			print("u were eaten by a snake u are now",n)
		elif(n==13):
			n=34
			print("u got a ladder u are now",n)
		elif(n==25):
			n=4
			print("u were eaten by a snake u are now",n)
		elif(n==38):
			n=9
			print("u were eaten by a snake u are now",n)
		elif(n==40):
			n=68
			print("u got a ladder u are now",n)
		elif(n==52):
			n=81
			print("u got a ladder u are now",n)
		elif(n==65):
			n=46
			print("u were eaten by a snake u are now",n)
		elif(n==76):
			n=97
			print("u got a ladder u are now",n)
		elif(n==89):
			n=70
			print("u were eaten by a snake u are now",n)
		elif(n==93):
			n=64
			print("u were eaten by a snake u are now",n)
