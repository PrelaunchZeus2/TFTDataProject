import requests, os, json, random, time
import polars as pl  #Trying polars since its supposed to be a bit quicker
SLEEP_TIME = 120

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
        print("Rate limit exceeded while getting account puuid. Waiting...")
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
        print("Rate limit exceeded while getting match list. Waiting...")
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
        print("Rate limit exceeded while getting match data. Waiting...")
        for remaining in range(SLEEP_TIME, 0, -1):
            print(f"Retrying in {remaining} seconds...", end="\r")
            time.sleep(1)
        return getMatchData(match_id)
    else:
        print(f"Error Getting Match Data: {request.status_code}")
        

def coreLoop(puuid: str, layers: int = 20):
    """
    This function retrieves matches for a player and iteratively retrieves matches for random players
    from those matches for the specified number of layers.
    """
    match_data_list = []
    loop_puuid = puuid

    for _ in range(layers):
        # Get the last 20 matches for the current player
        matches = getTFTMatches(loop_puuid, start=0, count=20)
        if not matches:
            print("No matches found or an error occurred.")
            continue

        # Retrieve and append match data for each match
        for match_id in matches:
            match_data = getMatchData(match_id)
            if match_data:
                match_data_list.append(match_data)

        # Select a random match and a random participant from that match
        random_match = random.choice(match_data_list)
        participants = random_match.get("metadata", {}).get("participants", [])
        if not participants:
            print("No participants found in the match.")
            break

        loop_puuid = random.choice(participants).strip()
        print("Layers left:", layers - _ - 1, end = "\r")

    return match_data_list

def extract_information(match_jsons):
    for match in match_jsons:
        match_id = None
        
        
def main():
    correct_name = False
    while not correct_name:
        starting_player = input("Please enter the account name and tagline of the player to start with, (format: Name#Tagline):\n")
        try:
            SummonerName, tagline = starting_player.split("#")
            correct_name = True  # Exit the loop if the input is valid
        except ValueError:
            print("Incorrect format. Please use Name#Tagline.")

    layers = 20  # The number of other players to get 20 matches from.
    
    starting_puuid = getPuuid(SummonerName, tagline)
    print(f"PUUID: {starting_puuid}")
   
    match_jsons = coreLoop(starting_puuid, layers)

    data_frame = extract_information(match_jsons)
    
    data_frame.write_csv("../Data/match_data.csv")
    
    
    
if __name__ == "__main__":
    main()