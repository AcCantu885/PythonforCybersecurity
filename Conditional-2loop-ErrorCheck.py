#Defined the function to print message based on user's input
def send_message(response):
   message = "Yes it is" if response == 'y' else "No, it is not"
   for _ in range(10):
      print(message)

#Prompt the user with the question "Is today a good day?"
answer = input("Is today a good day? (y/n): ")

#Checking the user's input and print the appropriate answer
if answer.lower() == 'y':
    for _ in range (10):
     print("Yes it is")
elif answer.lower() == 'n':
   for _ in range (10):
      print("No, it is not")
else:
   print("Invalid answer. Please enter 'y' or 'n'.")