#Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.
smallest = None
largest = None

while True:
    num = input("Enter a number (or press Enter to quit): ")
    if num == "":
        break
    num = float(num)  # convert input to number
    if smallest is None or num < smallest:
        smallest = num
    if largest is None or num > largest:
        largest = num

if smallest is not None and largest is not None:
    print("Smallest:", smallest)
    print("Largest:", largest)
else:
    print("No numbers were entered.")
