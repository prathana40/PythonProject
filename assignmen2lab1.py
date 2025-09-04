#Write a program that asks a fisher the length of a zander in centimeters. If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake and notifies the user of how many centimeters below the size limit the caught fish was. A zander must be 42 centimeters or longer to meet the size limit.
length = float(input("Enter the length of the zander (in cm): "))


size_limit = 42

if length < size_limit:
    difference = size_limit - length
    print(f"The zander is too small. Release it back into the lake!")
    print(f"It was {difference:.1f} cm below the size limit.")
else:
    print("The zander meets the size limit. You can keep it!")