#Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
total_sum = num1 + num2 + num3
product = num1 * num2 * num3
average = total_sum / 3
print("\n--- Results ---")
print(f"Sum: {total_sum}")
print(f"Product: {product}")
print(f"Average: {average}")