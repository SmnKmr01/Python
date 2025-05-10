#            S W G
#computer =  0 1 2
#player= S 0 D W L
#        W 1 L D W
#        G 2 W L D

print("Welcome to the Snake Water Gun game!")
import random
l = ["S", "W", "G"]
a = int(input("Enter 1 for Snake, 2 for Water, 3 for Gun: "))
if a == 1:
    player = "S"
elif a == 2:
    player = "W"
elif a == 3:
    player = "G"
else:
    print("Invalid input!")
    exit(0)
computer = random.choice(l)
print("Computer chose: ", computer)
if player == computer:
    print("It's a tie!")
elif player == "S":
    if computer == "W":
        print("You win!")
    else:
        print("You lose!")
elif player == "W":
    if computer == "G":
        print("You win!")
    else:
        print("You lose!")
elif player == "G":
    if computer == "S":
        print("You win!")
    else:
        print("You lose!")
else:
    print("Invalid input!")
    exit(0)
print("Thanks for playing!")
print("Goodbye!")
print("End of the game!")
print("End of the program!")

