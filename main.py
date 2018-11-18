import random
import time
import sys

diceNumber = random.randint(1,6)



print("Guess a number to see who wins!")

play1 = input("Player 1 name?")
play2 = input("Player 2 name?")
prize = input("What does the loser have to do?")

print("Hi " + play1 + " & " + play2 + ", let's roll the dice.")

play1Num = input(play1 + " choose a number 1-6.")
play2Num = input(play2 + " choose a number 1-6.")

play1Num = int(play1Num)
play2Num = int(play2Num)

def rollDice():asdr
    print("The Dice rolled...")
    print(diceNumber)

while diceNumber != play1Num or play2Num:
    diceNumber = random.randint(1,6)


    if play1Num == diceNumber:
        rollDice()
        print(play1.upper() + " WINS!")
        print(play2 + " must: " + prize)
        sys.exit()

    if play2Num == diceNumber:
        rollDice()
        print(play2.upper() + " WINS!")
        print(play1 + " must: " + prize)
        sys.exit()
