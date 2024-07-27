#Asking the user the questions for writing files
name = input("What is your name? ")
favorite_color = input("What is your favorite color? ")
first_pet = input("What was your first pet's name? ")
mother_maiden_name = input("What is your mother's maiden name? ")
elementary_school = input("What elementary school did you attend? ")

#Print the user's answers to verify
print("\nHere are your answers:")
print(f"Name: {name}")
print(f"Favorite color: {favorite_color}")
print(f"First pet's name: {first_pet}")
print(f"Mother's maiden name: {mother_maiden_name}")
print(f"Elementary school: {elementary_school}")

#Collect the information into a string
info = (
    f"Name: {name}\n"
    f"Favorite color: {favorite_color}\n"
    f"First pet's name: {first_pet}\n"
    f"Mother's maiden name: {mother_maiden_name}\n"
    f"Elementary school: {elementary_school}\n"
)

#We save the information to a file called "hackme.txt"
with open("hackme.txt", "w") as file:
    file.write(info)
print("Information saved to hackme.txt")