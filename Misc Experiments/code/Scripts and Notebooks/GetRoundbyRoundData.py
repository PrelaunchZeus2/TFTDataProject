import requests

TEST_KEY = "RGAPI-1ad6daf9-b235-4af1-b35b-4112501c1ca7"

def get_puuid(summoner_name, tagline):
    url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tagline}?api_key={TEST_KEY}"
    response = requests.get(url)
    data = response.json()
    return data['puuid']

def spectate_api(puuid):
    url = f"https://na1.api.riotgames.com/lol/spectator/tft/v5/active-games/by-puuid/{puuid}?api_key={TEST_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Error getting spectate data: {response.status_code}, {response.text}")