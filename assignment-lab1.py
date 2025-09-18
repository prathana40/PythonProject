#Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program. We can define each season to last three months, December being the first month of winter.# Store seasons in a tuple
seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter the number of the month (1-12): "))

if month in (12, 1, 2):
    season = seasons[0]  
elif month in (3, 4, 5):
    season = seasons[1]
elif month in (6, 7, 8):
    season = seasons[2]
elif month in (9, 10, 11):
    season = seasons[3]
else:
    season = "Invalid month number!"

print("The season is:", season)
