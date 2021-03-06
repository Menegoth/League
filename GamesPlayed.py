import requests
import json
import os

user = input("What is your account name? ")
url = "https://na1.api.riotgames.com/lol"
endpoints = {
  'accountData': f'{url}/summoner/v4/summoners/by-name/{user}'
}

apiKey = os.getenv("RIOT_API_KEY", "REPLACE_WITH_YOUR_API_KEY")
parameters = {"api_key": apiKey}

response = requests.get(endpoints["accountData"], params=parameters)

if response.status_code == 200:

    accountData = json.loads(response.content)
    accountID = accountData["accountId"]

    endpoints["matchesData"] = f"{url}/match/v4/matchlists/by-account/{accountID}"

    response = requests.get(endpoints["matchesData"], params=parameters)

    if response.status_code == 200:
        matchesData = json.loads(response.content)

        print(f"You have played {matchesData['totalGames']} games in the last week.")

    elif response.status_code == 401:

        print("Authentication failed.")

elif response.status_code == 401:

    print("Authentication failed.")

elif response.status_code == 404:

    print(f"Unable to find user by the name of {user}.")
