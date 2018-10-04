import random
rps={1:'rock',2:'paper',3:'scissor'}

while True:
	r=rps[random.randint(1,3)]
	x=input("enter rock,paper or scissor")
	print("u chose",x,"comp chose",r)
	
	if x==r:
		print("draw")
	elif x=='rock':
		if r=='paper':
			print("u lose")
		elif r=='scissor':	
			print("u win")	
	elif x=='paper':
		if r=='scissor':
			print("u lose")
		elif r=='rock':
			print("u win")
	elif x=='scissor':
		if r=='rock':
			print("u lose")
		elif r=='paper':
			print("u win")