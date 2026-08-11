import random

choices = ["rock", "paper", "scissor"]
computer = random.choice(choices)
player = str(input("Enter rock, paper, scissor: ")).lower()
print("Computer: ", computer)
print("You:", player)

if player == computer:
    print("It's a tie.")

elif player == "rock" and computer == "scissor":
    print("You Win!")

elif player == "paper" and computer == "rock":
    print("You Win!")

elif player == "scissor" and computer == "paper":
    print("You Win!")

else:
    print("Computer Win!")