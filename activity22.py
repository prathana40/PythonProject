#Write a program that asks the user to enter numbers until they input an empty string to quit.
numbers = []

while True:
    entry = input("Enter a number (or press Enter to quit): ")
    if entry == "":
        break
    try:
        num = float(entry)  # allows integers and decimals
        numbers.append(num)
    except ValueError:
        print("That’s not a valid number. Try again.")

# Sort numbers in descending order
numbers.sort(reverse=True)

if numbers:
    print("The five greatest numbers are:")
    for n in numbers[:5]:
        print(n)
else:
    print("No numbers were entered.")
