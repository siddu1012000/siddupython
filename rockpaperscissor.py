import random
rps={1:'r',2:'p',3:'s'}
a=0
b=0
while a<3 and b<3:
	
	r=rps[random.randint(1,3)]
	x=input("enter rock,paper or scissor")
	print("u chose",x,"comp chose",r)
	if x==r:
		print("draw")
	elif x=='r':
		if r=='p':
			print("u lose")
			b=b+1 
		else:	
			print("u win")
			a=a+1	
	elif x=='p':
		if r=='s':
			print("u lose")
			b=b+1
		else:
			print("u win")
			a=a+1
	elif x=='s':
		if r=='r':
			print("u lose")
			b=b+1
		else:
			print("u win")
			a=a+1
	if a==3:
			print("u won the game")
	elif b==3:
			print("comp won the game")