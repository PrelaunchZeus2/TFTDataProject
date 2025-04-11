class WelcomeWindow {
    private filePath: string;

    constructor() {
        this.filePath = '';
        this.initialize();
    }

    private initialize(): void {
        this.displayWelcomeMessage();
        this.setupFilePathButton();
    }

    private displayWelcomeMessage(): void {
        const welcomeMessage = document.createElement('h1');
        welcomeMessage.innerText = 'Welcome to the Overwolf App!';
        document.body.appendChild(welcomeMessage);
    }

    private setupFilePathButton(): void {
        const selectButton = document.createElement('button');
        selectButton.innerText = 'Select File Path';
        selectButton.onclick = () => this.selectFilePath();
        document.body.appendChild(selectButton);
    }

    private selectFilePath(): void {
        overwolf.io.getFilePath((result) => {
            if (result.status === 'success') {
                this.filePath = result.path;
                this.startGameDetection();
            } else {
                console.error('Failed to get file path:', result);
            }
        });
    }

    private startGameDetection(): void {
        overwolf.games.onGameInfoUpdated.addListener((info) => {
            if (info && info.gameInfo && info.gameInfo.isRunning) {
                this.transitionToIngameWindow();
            }
        });
    }

    private transitionToIngameWindow(): void {
        overwolf.windows.obtainDeclaredWindow('IngameWindow', (result) => {
            if (result.status === 'success') {
                overwolf.windows.restore(result.window.id);
            } else {
                console.error('Failed to open IngameWindow:', result);
            }
        });
    }
}

export default WelcomeWindow;