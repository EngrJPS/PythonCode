#This game generates random numbers to guess the users from the computer

#Import random function to generate computer a random number
import random


def guess(x):
    randomNum = random.randint(1,x)
    guess = 0
    while guess != randomNum:
        guess = int(input(f"Guess number between 1 to {x} :"))
        if guess >= randomNum:
            print("Guess again! The number is too high")
        elif guess <= randomNum:
            print("Guess again! The number is too low")

    print(f"Yay! You got it! {randomNum}")

somNum = int(input("Enter the range to guess: "))

guess(somNum)