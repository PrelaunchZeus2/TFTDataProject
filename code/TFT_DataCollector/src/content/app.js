const { getGameInfo, getPlayerData } = require('../utils/dataRecorder');

let gameData = [];
let isGameActive = false;

function startGameTracking() {
    isGameActive = true;
    gameData = [];
    // Add event listeners for game state changes
    overwolf.games.onGameInfoUpdated.addListener(handleGameInfoUpdate);
}

function stopGameTracking() {
    isGameActive = false;
    // Save game data to CSV
    saveGameDataToCSV();
}

function handleGameInfoUpdate(info) {
    if (info && info.gameInfo && info.gameInfo.isRunning) {
        if (!isGameActive) {
            startGameTracking();
        }
        // Collect data for each round
        collectRoundData();
    } else if (isGameActive) {
        stopGameTracking();
    }
}

function collectRoundData() {
    const playerData = getPlayerData();
    if (playerData) {
        gameData.push(playerData);
    }
}

function saveGameDataToCSV() {
    const csvData = gameData.map(row => Object.values(row).join(',')).join('\n');
    const filePath = 'path/to/your/csv/file.csv'; // Update this path as needed
    overwolf.io.writeFile(filePath, csvData, (result) => {
        if (result.status === 'success') {
            console.log('Data saved successfully to CSV.');
        } else {
            console.error('Error saving data to CSV:', result);
        }
    });
}

overwolf.games.onGameInfoUpdated.addListener(handleGameInfoUpdate);