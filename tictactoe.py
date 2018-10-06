x=[1,2,3,4,5,6,7,8,9]

def prtboard():
	print(x[0],'|',x[1],'|',x[2])
	print('.........')
	print(x[3],'|',x[4],'|',x[5])	
	print('.........')
	print(x[6],'|',x[7],'|',x[8])
'''prtboard()'''

playeroneturn=True

while True:
	prtboard()
	p=int(input("choose ur place  "))
	if(p in x):
		if playeroneturn:
			#p=input("choose ur place player 1")
			print("player 1 chose",p)
			x[p-1]='X'
			playeroneturn = not playeroneturn
			
		else:
			#p=input("choose ur place player 2")
			print("player 2 chose",p)
			x[p-1]='O'
			playeroneturn = not playeroneturn

		for i in(0,3,6):
			if(x[i]==x[i+1]and x[i]==x[i+2]):
				if x[i]=='X':
					print('player 1 wins')
					exit()
				else:
					print('player 2 wins')
					exit()	

		for i in range(3):
			if(x[i]==x[i+3]and x[i]==x[i+6]):
				if x[i]=='X':
					print('player 1 wins')
					exit()
				else:
					print('player 2 wins')
					exit()			

		
		if(x[i]==x[i+4]and x[i]==x[i+8]):
			if x[i]=='X':
				print('player 1 wins')
				exit()
			else:
				print('player 2 wins')
				exit()					


		if(x[i+2]==x[i+4]and x[i+2]==x[i+6]):
			if x[i]=='X':
				print('player 1 wins')
				exit()
			else:
				print('player 2 wins')
				exit()			