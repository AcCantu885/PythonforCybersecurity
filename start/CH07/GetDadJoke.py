import requests

def get_dad_jokes():
    #Defined the url of the API
    url = "https://icanhazdadjoke.com/"
    print("URL defined:", url)


    #Defined the Headers to specify JSON response
    headers = {
        "Accept": "application/json"
    }
    print("Headers defined:", headers)

    
#Send Get Request to API
response = requests.get(url, headers=headers)

#Check if request was successful
if response.status_code == 200:
    #Parse the data JSON Response
    joke_data = response.json()
    # Print joke
    print(joke_data['joke'])
else:
    # Print an error that the message request failed
    print(f"Failed to retrive the joke. Status code: {response.status_code}")


print(get_dad_jokes())
if __name__ == "__main__":
    get_dad_jokes()
