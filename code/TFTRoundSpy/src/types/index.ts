export interface PlayerUnit {
    id: string;
    name: string;
    position: { x: number; y: number };
    items: Item[];
}

export interface Item {
    id: string;
    name: string;
}

export interface GameState {
    playerUnits: PlayerUnit[];
    benchUnits: PlayerUnit[];
    availableUnits: PlayerUnit[];
    currentRound: number;
    playerGold: number;
}