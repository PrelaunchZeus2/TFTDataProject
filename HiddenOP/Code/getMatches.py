import requests, os, json, random, time
import pandas as pd #maybe try polars later

SLEEP_TIME = 30

try:
    with open("API_KEY.txt", "r") as f:
        API_KEY = f.read().strip()
    if API_KEY == "":
        raise ValueError("API_KEY is empty. Please provide a valid API key in API_KEY.txt.")
except FileNotFoundError:
    API_KEY = os.getenv("TFTRIVALS_API_KEY")
    if API_KEY is None:
        raise ValueError("API_KEY is not set. Please provide a valid API key in API_KEY.txt or as the TFTRIVALS_API_KEY environment variable.")

def getPuuid(name: str, tagline: str):
    """
    This function retrieves the puuid of a player using their in-game name and tagline.
    """
    url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tagline}?api_key={API_KEY}"
    request = requests.get(url)
    if request.status_code == 200:
        return json.loads(request.content)["puuid"]
    elif request.status_code == 429:
        print("Rate limit exceeded. Waiting...")
        for remaining in range(SLEEP_TIME, 0, -1):
            print(f"Retrying in {remaining} seconds...", end="\r")
            time.sleep(1)
        return getPuuid(name, tagline)
    else:
        print(f"Error Getting Puuid: {request.status_code}")
        return None

def getTFTMatches(puuid: str, start: int = 0, count: int = 20):
    """
    This function retrieves the TFT matches of a player using their puuid.
    """
    url = f"https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?start={start}&count={count}&api_key={API_KEY}"
    request = requests.get(url)
    if request.status_code == 200:
        return json.loads(request.content)
    elif request.status_code == 429:
        print("Rate limit exceeded. Waiting...")
        for remaining in range(SLEEP_TIME, 0, -1):
            print(f"Retrying in {remaining} seconds...", end="\r")
            time.sleep(1)
        return getTFTMatches(puuid, start, count)
    else:
        print(f"Error Getting Match List: {request.status_code}")
        return None

def getMatchData(match_id: str):
    """
    This function gets the match data for a specific match id.
    """
    url = f"https://americas.api.riotgames.com/tft/match/v1/matches/{match_id}?api_key={API_KEY}"
    request = requests.get(url)
    if request.status_code == 200:
        return json.loads(request.content)
    elif request.status_code == 429:
        print("Rate limit exceeded. Waiting...")
        for remaining in range(SLEEP_TIME, 0, -1):
            print(f"Retrying in {remaining} seconds...", end="\r")
            time.sleep(1)
        return getMatchData(match_id)
    else:
        print(f"Error Getting Match Data: {request.status_code}")
        return None

def coreLoop(puuid: str, layers: int = 20):
    match_data_list = []
    loop_puuid = puuid
    i = 0
    while i < layers:
        i += 1
        matches = getTFTMatches(loop_puuid, 0, layers)    
        for match_id in matches:
            match = getMatchData(match_id)
            match_data_list.append(match)
        random_match = random.choice(match_data_list)
        participants = random_match.get("metadata", {}).get("participants", [])
        loop_puuid = random.choice(participants).strip()
    return match_data_list

def extract_information(match_jsons):
    match_info = {}
        
def main():
    SummonerName = "LunaLush"
    tagline = "Heyyy"
    layers = 20 #The number of other players to get 20 matches from.
    
    starting_puuid = getPuuid(SummonerName, tagline)
    print(f"PUUID: {starting_puuid}")
   
    match_jsons = coreLoop(starting_puuid, layers)
    print(f"Matches: {match_jsons}") 
    
    #data = extract_information(match_jsons)
    
    
    
if __name__ == "__main__":
    main()