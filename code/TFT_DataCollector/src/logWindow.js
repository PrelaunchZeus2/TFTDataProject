const statusElement = document.getElementById('status');
const logElement = document.getElementById('log');

function updateStatus(status) {
    statusElement.textContent = status;
}

function appendLog(message) {
    logElement.textContent += message + '\n';
    logElement.scrollTop = logElement.scrollHeight;
}

overwolf.windows.getCurrentWindow(result => {
    const windowId = result.window.id;

    overwolf.windows.onStateChanged.addListener((state) => {
        if (state.window_id === windowId && state.window_state === 'normal') {
            updateStatus('Logging started');
        }
    });
});

window.updateStatus = updateStatus;
window.appendLog = appendLog;