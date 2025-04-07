# Overwolf League of Legends Team Fight Tactics Tracker

This project is an Overwolf app designed to track and log player information in League of Legends Team Fight Tactics (TFT). The app provides a user-friendly interface to select a file path for saving game data and transitions to an in-game log window that displays real-time information about the player's units, items, positions, and more.

## Features

- Welcome window with a file path selection button.
- Real-time tracking of player units, items, and positions during gameplay.
- Logging of game data to a CSV file at the user-defined path.
- User-friendly interface for both the welcome and in-game windows.

## Project Structure

```
overwolf-app
├── src
│   ├── main.ts                # Entry point of the application
│   ├── welcome
│   │   ├── WelcomeWindow.ts   # Manages the welcome interface
│   │   └── WelcomeWindow.html  # HTML structure for the welcome window
│   ├── ingame
│   │   ├── IngameWindow.ts     # Manages the in-game log interface
│   │   └── IngameWindow.html    # HTML structure for the in-game log window
│   ├── utils
│   │   └── FileHandler.ts      # Utility for saving game data to CSV
│   └── types
│       └── index.ts           # Defines data structures used in the app
├── package.json                # npm configuration file
├── tsconfig.json               # TypeScript configuration file
├── overwolf-manifest.json      # Manifest for the Overwolf app
└── README.md                   # Project documentation
```

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the necessary dependencies using npm:
   ```
   npm install
   ```
4. Build the project using TypeScript:
   ```
   npm run build
   ```
5. Load the app in Overwolf by following the Overwolf app development guidelines.

## Usage

- Launch the app to open the welcome window.
- Click the "Select File Path" button to choose where to save the game data.
- Start a game of League of Legends Team Fight Tactics.
- The app will automatically switch to the in-game log window and begin tracking player information.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.