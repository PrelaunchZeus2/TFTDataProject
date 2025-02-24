const gameId = 5426; // Game ID for League of Legends
let isGameRunning = false;

function init() {
    overwolf.games.onGameInfoUpdated.addListener(onGameInfoUpdated);
    overwolf.games.getRunningGameInfo((result) => {
        if (result && result.gameInfo && result.gameInfo.id === gameId) {
            isGameRunning = true;
            startDataCollection();
        }
    });
}

function onGameInfoUpdated(info) {
    if (info && info.gameInfo && info.gameInfo.id === gameId) {
        if (!isGameRunning && info.gameInfo.isRunning) {
            isGameRunning = true;
            startDataCollection();
        } else if (isGameRunning && !info.gameInfo.isRunning) {
            isGameRunning = false;
            stopDataCollection();
        }
    }
}

function startDataCollection() {
    // Logic to start collecting data from the game
    console.log('Game started, beginning data collection...');
    overwolf.games.events.onNewEvents.addListener(onNewEvents);
    overwolf.games.events.onInfoUpdates2.addListener(onInfoUpdates);
}

function stopDataCollection() {
    // Logic to stop collecting data and save to CSV
    console.log('Game ended, stopping data collection...');
    overwolf.games.events.onNewEvents.removeListener(onNewEvents);
    overwolf.games.events.onInfoUpdates2.removeListener(onInfoUpdates);
}

function onNewEvents(events) {
    // Handle new events from the game
    console.log('New events:', events);
}

function onInfoUpdates(info) {
    // Handle info updates from the game
    console.log('Info updates:', info);
}

init();