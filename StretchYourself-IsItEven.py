#Create a script that prompts user for a number,
#then tells user if it is even

#Prompt user for number
number = int(input("Give a number"))

#Check if the value is even or odd
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is false!")