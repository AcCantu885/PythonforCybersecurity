#Prompt the user with the question "Is today a good day?"
answer = input("Is today a good day? (y/n): ")

#Checking the user's input and print the appropriate answer
if answer.lower() == 'y':
    for _ in range (10):
     print("Yes it is")