#Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until they guess the right numbe
import random

secret_number = random.randint(1, 10)

while True:
    guess = input("Guess a number between 1 and 10: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! 🎉")
        break
