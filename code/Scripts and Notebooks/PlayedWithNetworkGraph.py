import requests, json, pandas as pd
import os

BASE_URL = "https://americas.api.riotgames.com/"
API_KEY = os.getenv("TFTRIVALS_API_KEY", None)
if API_KEY is None:
    raise Exception("Please set the TFTRIVALS_API_KEY environment variable.")

def get_account_puuid(summoner_name, tagline):
    puuid = 'NA'
    url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tagline}?api_key={API_KEY}"
    query = requests.get(url)
    if query.status_code == 200:
        data = query.json()
        puuid = data.get('puuid', 'NA')
    else:
        raise Exception("Error getting puuid", query.status_code)
        puuid = None
        
    return puuid

def get_tft_match_ids(puuid, num_matches = 1):
    url = f"{BASE_URL}tft/match/v1/matches/by-puuid/{puuid}/ids?count={num_matches}&api_key={API_KEY}"
    data = []
    query = requests.get(url)
    if query.status_code == 200:
        data = query.json()
        return data
    else:
        raise Exception("Error getting matches", query.status_code)
        data = None
    return data

def get_match_data(match_id_list):
    all_matches = []
    for matchid in match_id_list:
        url = f"{BASE_URL}tft/match/v1/matches/{matchid}?api_key={API_KEY}"
        match_data = requests.get(url).json()
        all_matches.append(match_data)

    return all_matches

def main():

    
    summoner_name = input("Enter Summoner Name: ")
    tagline = input("Enter Tagline (no #): ")
    num_matches = int(input("Enter number of matches to retrieve: "))
    
    if summoner_name and tagline:
        puuid = get_account_puuid(summoner_name, tagline)
        print(f"PUUID: {puuid}")
        
        if num_matches > 0:
            matches = get_tft_match_ids(puuid, num_matches)
            
            if len(matches) > 0:
                match_data = get_match_data(matches)
                print(f"Match Data: {match_data}")
                
if __name__ == "__main__":
    main()  


        