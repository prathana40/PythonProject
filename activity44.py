# Program to read names of five cities and display them
cities = []

# Use a for loop to read 5 city names
for i in range(5):
    city = input(f"Enter the name of city {i+1}: ")
    cities.append(city)

# Print the names of the cities one by one using a for/in loop
print("\nThe cities you entered are:")
for city in cities:
    print(city)
