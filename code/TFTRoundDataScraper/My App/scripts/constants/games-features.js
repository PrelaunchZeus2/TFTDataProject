export const kGamesFeatures = new Map([
  
  // League of Legends
  [
    54261,
    [
      'live_client_data',
      'matchState',
      'match_info',
      'death',
      'respawn',
      'abilities',
      'kill',
      'assist',
      'gold',
      'minions',
      'summoner_info',
      'gameMode',
      'teams',
      'level',
      'announcer',
      'counters',
      'damage',
      'heal'
    ]
  ],
]);

export const kGameClassIds = Array.from(kGamesFeatures.keys());
