#We try and read the 'hackme' file in this script
try: 
    with open("hackme.txt", "r") as file:
        content = file.readlines()
except FileNotFoundError: 
 print("The file hackme.txt does not exist. Please make sure ithas been created and try again.")


#Printing the header message
print("Here is someone to hack - information")

#Printing the content of the file
for line in content:
    print(line.strip())