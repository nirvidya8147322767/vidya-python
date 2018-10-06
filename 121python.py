import random

print("Hello! Welcome to the Rock Paper Scissors Program!")

Win = False

while Win == False:
    print("enter 1 for Rock.")
    print("enter 2 for Paper.")
    print("enter 3 for Scissors.")

    p = int(input("What would you like to play?"))
    c = random.randrange(1,3)

    if (p == 1) and (c == 1):
        Win = False
        print("It's a draw; you both played Rock!")
        
    if (p == 2) and (c == 1):
        Win == True
        print("You win! The computer played Rock!")

    if (p == 3) and (c == 1):
        Win == True
        print("You lose! The computer played Rock!")
        
    if (p == 1) and (c == 2):
        Win = True
        print("You lose! The computer played Paper!")
        
    if (p == 2) and (c == 2):
        Win == False
        print("It's a draw; the computer played Paper!")

    if (p == 3) and (c == 2):
        Win == True
        print("You win! The computer played Paper!")
        
    if (p == 1) and (c == 3):
        Win = True
        print("You win! The computer played Scissors!")
        
    if (p == 2) and (c == 3):
        Win == True
        print("You lose! The computer played Scissors!")

    if (p == 3) and (c == 3):
        Win == False
        print("It's a draw; the computer played Scissors!")
