#Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again
USERNAME = "python"
PASSWORD = "rules"

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    if user == USERNAME and pwd == PASSWORD:
        print("Welcome")
        break
    else:
        print("Wrong username or password. Try again.")
        attempts += 1

if attempts == max_attempts:
    print("Access denied")

