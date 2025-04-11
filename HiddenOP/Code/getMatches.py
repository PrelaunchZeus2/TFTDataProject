import requests, os, json
import pandas as pd #maybe try polars later

with open("API_KEY.txt", "r") as f:
    API_KEY = f.read().strip()


def getPuuid(name: str, tagline: str):
    """
    This function retrieves the puuid of a player using their in game name and tagline.
    """
    url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tagline}?api_key={API_KEY}"
    request = requests.get(url)
    if request.status_code == 200:
        puuid = json.loads(request.content)["puuid"]
        return puuid
    else:
        print(f"Error: {request.status_code}")
        return None
    
def getTFTMatches(puuid: str, start: int = 0, count: int = 20):
    """
    This function retrieves the TFT matches of a player using their puuid.
    """
    url = "https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?start={start}&count={count}"
    request = requests.get(url)
    if request.status_code == 200:
        matches = json.loads(request.content)
        return matches
    else:
        print(f"Error: {request.status_code}")
        return None
    
    
def main():
    SummonerName = "LunaLush"
    tagline = "Heyyy"
    
    
    puuid = getPuuid(SummonerName, tagline)
    print(f"PUUID: {puuid}")
    
if __name__ == "__main__":
    main()