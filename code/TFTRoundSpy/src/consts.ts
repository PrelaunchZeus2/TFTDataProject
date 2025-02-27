export const kGamesFeatures = new Map<number, string[]>([
  // League of Legends
  [
    5426,
    [
      'live_client_data',
      'matchState',
      'match_info',
      'roster',
      'me',
      'roster',
      'store',
      'board',
      'bench',
      'carousel',
      'augments',
      'game_info',
    ]
  ]
]);

export const kGameClassIds = Array.from(kGamesFeatures.keys());

export const kWindowNames = {
  inGame: 'in_game',
  desktop: 'desktop'
};

export const kHotkeys = {
  toggle: 'sample_app_ts_showhide'
};
