## Table of Contents

1. [Portal Gaming Hub - Console Version](#portal-gaming-hub---console-version)
2. [Tutorial](#tutorial)
3. [How does it work](#how-does-it-work)
4. [For the program to work correctly](#for-the-program-to-work-correctly)
5. [Requirements](#requirements)
6. [Configuration](#configuration)
7. [Contributors](#contributors-)
8. [Usage](#usage)
9. [Support](#support)
10. [License](#license)


# Portal Gaming Hub - Console Version

This code implements a number guessing mini-game, which can be run from the command line. The user navigates through menus to select a platform and then a game, after which they must guess a number within a randomly generated interval while receiving clues about the current interval. The game stores information such as the last time it was played and the current interval limits. 

Additionally, the "main_menu" function displays a series of options and has a different color scheme based on ANSI escape characters if it is run on a Windows operating system with color support.

# Tutorial

[![Portal Gaming Hub in Console](https://img.youtube.com/vi/F-H_VAORFRk/0.jpg)](https://www.youtube.com/watch?v=F-H_VAORFRk)

# How does it work:

- The code imports several libraries: json, time, random, datetime, os, and platform.
- It then checks the type of platform and enables color support on the command prompt if the platform is Windows.
- The main_menu function clears the console and prints out some options.
- The platforms_menu function clears the console and prints out a list of available platforms. It then prompts the user to select a platform and returns the available games for that platform.
- The games_menu function clears the console and prints out a list of available games. It then prompts the user to select a game and starts a mini-game where the user has to guess a randomly generated number within a certain range.
- The generate_number function generates a new random number each time it is called, within a certain range determined by the time since the last time the game was played.
- The countdownMiniGame function is called to give a short countdown before displaying the next message.

# For the program to work correctly:
- Ensure that you have all the requirements.txt installed. ( pip install -r requirements.txt )
- Make sure that you have selected the correct path in game_location, in platforms.json

# Requirements

Python 3.6 or later
Required packages listed in requirements.txt
To install the required packages, run the following command in your terminal:

```sh
pip install -r requirements.txt
```

# Configuration

The script requires path in order to execute .exe files that will be mention in platforms.json, field "game_location".

Example of platforms.json

For example game League of Legends

```json
{
    "Riot Games": {
        "platform_name_suggestion": "Try playing a game outside instead of playing Steam games.",
        "available_games": {
            "League of Legends": {
                "suggestion": "Why not go for a walk in the park instead of playing League of Legends?",
                "game_location": "C:\\Riot Games\\League of Legends\\LeagueClient.exe",
                "last_played": 1676827442.9226286
            }
        }
    }
}
```

# Contributors ✨

Thanks go to these wonderful people:

<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://axbecher.com"><img src="https://avatars.githubusercontent.com/u/72851811?v=4" width="100px;" alt="Alexandru Becher"/><br /><sub><b>Alexandru Becher</b></sub></a><br />
      </td>
    </tr>
  </tbody>
</table>

# Usage
1. To run the script, use the following command in your terminal:
```sh
python main.py
```
2. Double click on main.py and console will pop up.

# Support
For any questions or support, please contact me via https://axbecher.com/contact/

# License
This project is licensed under the MIT License.
