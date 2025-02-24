# Overwolf League of Legends TFT App

This project is an Overwolf app designed to track and record data from League of Legends: Teamfight Tactics (TFT) games. The app captures various game states and user actions, allowing players to analyze their performance over time.

## Features

- Monitors TFT games and records:
  - Units played
  - Items equipped
  - Units purchased on the bench
  - Unit positions on the board
  - Active traits
  - Units available in the shop
- Exports collected data to a CSV file at a user-specified path.

## Project Structure

```
overwolf-lol-tft-app
├── src
│   ├── main.ts          # Entry point of the Overwolf app
│   ├── background.ts     # Handles background processes and game event listening
│   ├── content
│   │   ├── index.html    # Main HTML file for the user interface
│   │   ├── styles.css     # Styles for the user interface
│   │   └── app.js        # JavaScript logic for user interactions
│   └── utils
│       └── dataRecorder.ts # Functions for recording game data to CSV
├── manifest.json         # Configuration file for the Overwolf app
├── package.json          # npm configuration file
└── README.md             # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd overwolf-lol-tft-app
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Load the app in Overwolf:
   - Open the Overwolf app.
   - Navigate to the "Apps" section.
   - Click on "Load unpacked" and select the project directory.

4. Configure the app:
   - Specify the path for the CSV file in the settings.

## Usage Guidelines

- Launch the app before starting a TFT game.
- The app will automatically track and record data for each round until the game ends or the player is eliminated.
- Access the recorded data in the specified CSV file path.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.