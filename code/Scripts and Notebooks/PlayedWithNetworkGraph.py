import requests, json, pandas as pd
import os
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
import time

BASE_URL = "https://americas.api.riotgames.com/"
API_KEY = os.getenv("TFTRIVALS_API_KEY", None)
if API_KEY is None:
    raise Exception("Please set the TFTRIVALS_API_KEY environment variable.")

def rate_limit(requests_per_second, requests_per_two_minutes):
    def decorator(func):
        last_called = [0]  # To store the last call time
        call_times = []  # To store timestamps of recent calls

        def wrapper(*args, **kwargs):
            current_time = time.time()

            # Remove timestamps older than 2 minutes
            call_times[:] = [t for t in call_times if current_time - t < 120]

            # Check if we exceed the 2-minute limit
            if len(call_times) >= requests_per_two_minutes:
                sleep_time = 120 - (current_time - call_times[0])
                time.sleep(sleep_time)

            # Check if we exceed the per-second limit
            if current_time - last_called[0] < 1 / requests_per_second:
                time.sleep(1 / requests_per_second - (current_time - last_called[0]))

            # Update the last call time and add to call_times
            last_called[0] = time.time()
            call_times.append(last_called[0])

            return func(*args, **kwargs)

        return wrapper

    return decorator

@rate_limit(requests_per_second=20, requests_per_two_minutes=100)
def get_account_puuid(summoner_name, tagline):
    url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tagline}?api_key={API_KEY}"
    query = requests.get(url)
    if query.status_code == 200:
        data = query.json()
        return data.get('puuid', 'NA')
    else:
        raise Exception("Error getting puuid", query.status_code)
        return None

@rate_limit(requests_per_second=20, requests_per_two_minutes=100)
def get_tft_match_ids(puuid, num_matches = 1):
    url = f"{BASE_URL}tft/match/v1/matches/by-puuid/{puuid}/ids?count={num_matches}&api_key={API_KEY}"
    query = requests.get(url)
    if query.status_code == 200:
        return query.json()
    else:
        raise Exception("Error getting matches", query.status_code)
        return None

@rate_limit(requests_per_second=20, requests_per_two_minutes=100)
def get_match_data(match_id_list):
    all_matches = []
    for matchid in match_id_list:
        url = f"{BASE_URL}tft/match/v1/matches/{matchid}?api_key={API_KEY}"
        match_data = requests.get(url).json()
        all_matches.append(match_data)

    return all_matches

@rate_limit(requests_per_second=20, requests_per_two_minutes=100)
def get_summoner_name_from_puuid(puuid):
    url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("gameName"), data.get("tagLine")
    else:
        print(f"Error fetching summoner name for PUUID {puuid}: {response.status_code}")
        return None, None

def create_network_graph(center_name, participants):
    # Count occurrences of each participant
    name_counts = Counter(participants)

    # Remove the center name from the participants list if it exists
    if center_name in name_counts:
        del name_counts[center_name]

    # Create a graph
    G = nx.Graph()

    # Add the center node
    G.add_node(center_name, size=3000, color='red')

    # Add nodes and edges for participants
    for name, count in name_counts.items():
        G.add_node(name, size=1000 + count * 100, color='blue')
        G.add_edge(center_name, name, weight=count)

    # Count co-occurrences between participants
    co_occurrence_counts = Counter()
    for i, player1 in enumerate(participants):
        for player2 in participants[i + 1:]:
            if player1 != player2:
                co_occurrence_counts[(player1, player2)] += 1

    # Add edges between participants based on co-occurrence counts
    for (player1, player2), count in co_occurrence_counts.items():
        if not G.has_edge(player1, player2):
            G.add_edge(player1, player2, weight=count)

    # Draw the graph
    pos = nx.spring_layout(G)
    sizes = [G.nodes[node]['size'] for node in G.nodes]
    colors = [G.nodes[node]['color'] for node in G.nodes]
    weights = [G[u][v]['weight'] for u, v in G.edges]

    nx.draw(
        G, pos, with_labels=True, node_size=sizes, node_color=colors,
        width=[weight * 0.8 for weight in weights], edge_color=weights, edge_cmap=plt.cm.Blues
    )
    plt.show()

def main():
    summoner_name = input("Enter Summoner Name: ") or "LunaLush"
    tagline = input("Enter Tagline: ") or "Heyyy"
    num_matches_input = input("Enter number of matches to retrieve: ")
    num_matches = int(num_matches_input) if num_matches_input else 1

    if summoner_name and tagline:
        puuid = get_account_puuid(summoner_name, tagline)
        print(f"PUUID: {puuid}")

        if num_matches > 0:
            matches = get_tft_match_ids(puuid, num_matches)

            if len(matches) > 0:
                match_data = get_match_data(matches)

                # Extract participants and fetch their summoner names
                all_participants = []
                for match in match_data:
                    participants = match.get("metadata", {}).get("participants", [])
                    for participant_puuid in participants:
                        name, _ = get_summoner_name_from_puuid(participant_puuid)
                        if name:
                            all_participants.append(name)

                # Create the network graph
                create_network_graph(summoner_name, all_participants)

if __name__ == "__main__":
    main()


