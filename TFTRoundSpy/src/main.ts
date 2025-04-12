import { WelcomeWindow } from './welcome/WelcomeWindow';
import { IngameWindow } from './ingame/IngameWindow';

const initApp = async () => {
    const welcomeWindow = new WelcomeWindow();
    await welcomeWindow.show();

    const filePath = await welcomeWindow.getSelectedFilePath();
    if (filePath) {
        const ingameWindow = new IngameWindow(filePath);
        await ingameWindow.waitForGameStart();
        await ingameWindow.show();
    }
};

initApp().catch(err => {
    console.error('Error initializing the app:', err);
});