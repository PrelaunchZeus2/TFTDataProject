import requests, json, pandas as pd

base_url = "https://americas.api.riotgames.com/"

API_KEY = "RGAPI-fcdceb6f-ef17-48fe-8849-c5465527ddcd" #Its expired L scrapers

LUNALUSHPUUID = "zFV662s0sKxQ_vy1ItsTNKV3vl-iFUo92BUFaG18EPGy57qVZaQrmnCYl7a5Sd-CS1ghhIdLPYQ1dw"

def get_account_puuid(summoner_name, tagline):
    puuid = 'NA'
    url = f"{base_url}riot/account/v1/accounts/by-riot-id/{summoner_name}/{tagline}?api_key={API_KEY}"
    query = requests.get(url)
    if query.status_code == 200:
        data = query.json()
        puuid = data.get('puuid', 'NA')
    else:
        raise Exception("Error getting puuid", query.status_code)
        puuid = None
    
    return puuid
    
def get_tft_match_ids(puuid, num_matches = 1):
    url = f"{base_url}tft/match/v1/matches/by-puuid/{puuid}/ids?count={num_matches}&api_key={API_KEY}"
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
        url = f"{base_url}tft/match/v1/matches/{matchid}?api_key={API_KEY}"
        match_data = requests.get(url).json()
        all_matches.append(match_data)

    return all_matches

def puuid_to_summoner_id(puuid):
    url = f"https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-puuid/{puuid}?api_key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get('id')  # Returns summonerId
    else:
        raise Exception(f"Error getting summonerId: {response.status_code}, {response.text}")
    
def get_player_rank(summoner_id):
    url = f"https://na1.api.riotgames.com/tft/league/v1/entries/by-summoner/{summoner_id}?api_key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Error getting rank: {response.status_code}, {response.text}")
    

def main():
    summoner_name = "LunaLush"
    tagline = "Heyyy"
    
    # Get PUUID
    puuid = get_account_puuid(summoner_name, tagline)
    print(f"PUUID: {puuid}")
    
    if puuid:
        # Get match IDs
        summoner_id = puuid_to_summoner_id(puuid)
        print(f"Summoner ID: {summoner_id}")
        
        if summoner_id:
            # Get rank
            rank = get_player_rank(summoner_id)
            print(f"Rank: {rank}")
            
    

if __name__ == "__main__":
    main()


    

