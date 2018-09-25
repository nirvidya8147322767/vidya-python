while True:
	a=(input("click r to print banglore temp: "))
	if(a=="r"):
		import random
		r=random.randint(25,30)
		print("banglore temp =",r)
	else:
		print("bye")
		break	