#Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:
talents = int(input("Enter number of talents: "))
pounds = int(input("Enter number of pounds: "))
lots = int(input("Enter number of lots: "))
grams_total = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)
kilograms = int(grams_total // 1000)
grams = grams_total % 1000
print("\n--- Result ---")
print(f"Mass: {kilogra22ms} kilograms and {grams:.2f} grams")