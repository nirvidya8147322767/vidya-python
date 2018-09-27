import random
def Roll dice():
	return random.randint(1,6)
def Mov(player,value,player1,player2):
	snake squares ={8:37,13:34,40:68,52:81,76:97}
	ladder squares ={11:2,25:4,38:9,65:48,89:70,93:64}
	Throw = Roll_dice()
    if Player == 1:
    	score = value + Throw
    	print(player1,"throw a die,u get a value": score)
    if player == 2:
    	score= value + throw
    	print(player2,"throw a die,u get a value": score)
    if score in snake squares:
    	print("if you bitten by snake come back to square")
    	score=snake score
    elif score in ladder squares:
    	print("if you get ladder climb up")
       