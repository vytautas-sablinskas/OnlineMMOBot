# SimpleMMO Bot

The SimpleMMO Bot is a tool that automates various actions in the game [SimpleMMO](https://web.simple-mmo.com), making it easier to progress through the game. The bot has both a frontend and a backend component, allowing for easy customization and control.

## Features

### Frontend

The frontend component of the bot includes:

- A user-friendly interface for setting up the bot's Chrome options and entering your SimpleMMO account/Discord credentials.
- A progress tracker to see the bot's current session progress.

### Backend

The backend component of the bot includes:

- Ability to attack mobs in the game.
- Ability to gather resources (mining, chopping wood, catching fish, salvaging and grabbing materials).
- Automatic dependency checking and installation on launch.

### Discord Integration

The bot includes Discord integration, allowing for seamless communication with a Discord server:

- Sends a message to the configured Discord server whenever an AFK check is detected in the game.
- Allows users to continue the bot's actions after responding to an AFK check by simply writing "!continue" in the Discord server.

## Getting Started

To get started with the SimpleMMO Bot, you'll need:

- Python 3.x
- Google Chrome

To install and use the bot:

1. Clone this repository to your local machine.
2. Launch Launcher.py file which will install needed dependencies.
3. Open a terminal and navigate to the Frontend directory.
4. Run `python Launcher.py`.
5. Wait until the GUI is opened.
6. Enter your SimpleMMO account/Discord credentials in the frontend interface.
7. Configure the Chrome options to your preference.
8. Click "Start Bot" to begin automating actions in the game.
