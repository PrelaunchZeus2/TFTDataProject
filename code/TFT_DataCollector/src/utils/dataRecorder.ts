import { writeFileSync } from 'fs';
import { join } from 'path';
import { homedir } from 'os';

interface GameState {
    round: number;
    unitsPlayed: string[];
    itemsSlammed: string[];
    unitsPurchased: string[];
    unitPositions: { [unit: string]: { x: number; y: number } };
    activeTraits: string[];
    unitsInShop: string[];
}

class DataRecorder {
    private data: GameState[] = [];
    private filePath: string;

    constructor(fileName: string) {
        const homeDirectory = homedir();
        this.filePath = join(homeDirectory, 'Documents', 'TFT_Round_Data', fileName);
    }

    public recordRoundData(gameState: GameState) {
        this.data.push(gameState);
    }

    public saveData() {
        const csvContent = this.convertToCSV(this.data);
        writeFileSync(this.filePath, csvContent);
    }

    private convertToCSV(data: GameState[]): string {
        const header = 'Round,Units Played,Items Slammed,Units Purchased,Unit Positions,Active Traits,Units in Shop\n';
        const rows = data.map(gameState => {
            return `${gameState.round},"${gameState.unitsPlayed.join(';')}","${gameState.itemsSlammed.join(';')}","${gameState.unitsPurchased.join(';')}",${JSON.stringify(gameState.unitPositions)},"${gameState.activeTraits.join(';')}","${gameState.unitsInShop.join(';')}"`;
        });
        return header + rows.join('\n');
    }
}

export default DataRecorder;