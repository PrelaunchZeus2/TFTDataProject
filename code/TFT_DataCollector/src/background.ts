import DataRecorder from './utils/dataRecorder';

const dataRecorder = new DataRecorder('game_data.csv');

function onNewEvents(events) {
    // Process new events and update gameData
    events.forEach(event => {
        // Example: Record units played, items slammed, etc.
        if (event.name === 'unit_played') {
            dataRecorder.recordRoundData({
                round: event.data.round,
                unitsPlayed: event.data.unitsPlayed,
                itemsSlammed: event.data.itemsSlammed,
                unitsPurchased: event.data.unitsPurchased,
                unitPositions: event.data.unitPositions,
                activeTraits: event.data.activeTraits,
                unitsInShop: event.data.unitsInShop
            });
        }
        // Add more event handling as needed
    });
}

function onInfoUpdates(info) {
    // Process info updates and update gameData
    if (info.info) {
        dataRecorder.recordRoundData({
            round: info.info.round,
            unitsPlayed: info.info.unitsPlayed,
            itemsSlammed: info.info.itemsSlammed,
            unitsPurchased: info.info.unitsPurchased,
            unitPositions: info.info.unitPositions,
            activeTraits: info.info.activeTraits,
            unitsInShop: info.info.unitsInShop
        });
    }
}

function saveGameData() {
    dataRecorder.saveData();
}

overwolf.games.events.onNewEvents.addListener(onNewEvents);
overwolf.games.events.onInfoUpdates2.addListener(onInfoUpdates);
overwolf.games.onGameInfoUpdated.addListener((info) => {
    if (info && info.gameInfo && info.gameInfo.id === 5426 && !info.gameInfo.isRunning) {
        saveGameData();
    }
});