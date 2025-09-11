#Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.
import random

num_dice = int(input("How many dice do you want to roll? "))

total = 0
for i in range(num_dice):
    roll = random.randint(1, 6)  # roll one die
    total += roll

print("The sum of the dice is:", total)
