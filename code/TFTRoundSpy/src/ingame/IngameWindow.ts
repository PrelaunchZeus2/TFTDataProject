export class IngameWindow {
    private playerUnits: Array<any>;
    private benchUnits: Array<any>;
    private availableUnits: Array<any>;
    private items: Array<any>;
    private boardPositions: Array<any>;

    constructor() {
        this.playerUnits = [];
        this.benchUnits = [];
        this.availableUnits = [];
        this.items = [];
        this.boardPositions = [];
    }

    public trackGameData(gameState: any): void {
        this.playerUnits = gameState.playerUnits;
        this.benchUnits = gameState.benchUnits;
        this.availableUnits = gameState.availableUnits;
        this.items = gameState.items;
        this.boardPositions = gameState.boardPositions;

        this.updateDisplay();
        this.saveDataToCSV();
    }

    private updateDisplay(): void {
        // Logic to update the in-game log window with the current game state
    }

    private saveDataToCSV(): void {
        // Logic to save the tracked game data to a CSV file
    }
}