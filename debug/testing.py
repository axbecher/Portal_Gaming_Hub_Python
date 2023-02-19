import json
import time
import random
import datetime
import os
import platform

if platform.system() == 'Windows':
    os.system('color') # enable color support on Windows command prompt

def main_menu():
    os.system('cls') # clear console
    print("\033[1;32m Select an option: \033[0m") 
    print("\033[2;37m     exit - Exit the program \033[0m") 
    print("\033[1;34m     platforms \033[0m\033[1;32m-\033[0m\033[1;34m Check available platforms\033[0m")
    print("\n")

def platforms_menu(platforms):
    os.system('cls') # clear console
    print("\033[1;32m Select a platform:\033[0m") # print in green
    print("\033[2;37m     back to menu - return to main menu\033[0m") # print in red
    for platform in platforms:
        print("\033[1;34m     " + platform + "\033[0m") # print in blue
    platform_choice = input("\n \033[7;32m Platform choice: \033[0m ")
    if platform_choice == "back to menu":
        return
    if platform_choice in platforms:
        games_menu(platforms[platform_choice]["available_games"])
    else:
        print("Invalid choice")

def games_menu(games):
    os.system('cls') # clear console
    print("\033[1;32m Select a game:\033[0m") # print in green
    print("\033[2;37m     back to menu - return to main menu\033[0m") # print in red
    for game_name, game_data in games.items():
        if "last_played" in game_data:
            last_played = game_data["last_played"]
            global last_played_old
            last_played_old = game_data["last_played"]
            last_played_formatted = time.strftime("%H:%M:%S - %d/%m/%Y", time.localtime(last_played))
            time_difference = datetime.timedelta(seconds=int(time.time() - last_played))
            time_difference_formatted = ""
            if time_difference.days > 0:
                time_difference_formatted += f"\033[1;36m{time_difference.days}\033[0m \033[3;36mdays, "
            if time_difference.seconds >= 3600:
                hours = time_difference.seconds // 3600
                time_difference_formatted += f"\033[1;36m{hours}\033[0m \033[3;36mhours, "
            if time_difference.seconds >= 60:
                minutes = (time_difference.seconds % 3600) // 60
                time_difference_formatted += f"\033[1;36m{minutes}\033[0m \033[3;36mminutes, "
            seconds = time_difference.seconds % 60
            time_difference_formatted += f"\033[1;36m{seconds}\033[0m \033[3;36mseconds ago"
        print("\033[1;34m     " + game_name + "\033[0m \033[1;32m-\033[0m " + f"{time_difference_formatted}" + "\033[0m") # print in blue
    game_choice = input("\n \033[7;32m Game choice: \033[0m ")
    if game_choice == "back to menu":
        return
    if game_choice in games:
        game = games[game_choice]
        print(f"Time current: ",int(time.time()))
        print(f"Last played: ",int(last_played_old))
        print(f"Diference: ",int(time.time() - last_played_old))
        global random_number

        def generate_number():
            diff = int(time.time() - last_played_old)
            global minLimit
            global maxLimit
            minLimit = random.randint(10000 + diff, 100000 + diff)
            maxLimit = random.randint(100000 + diff, 1000000 + diff)
            random_number = random.randint(minLimit, maxLimit)
            return random_number
        random_number = int(generate_number())
        while True:
            # os.system('cls') # clear console
            print("\033[1;32m Guess the number between \033[1;34m{0}\033[0m \033[1;32mand \033[1;34m{1}\033[0m\033[1;32m: \033[0m".format(minLimit,maxLimit))
            guess = input("\n\033[7;32m Choice: \033[0m ")
            if guess.upper() == "QUIT":
                break
            elif int(guess) < minLimit:
                print("\033[7;31mInvalid input;\033[0m \033[1;32mPlease enter a number \033[1;34mgreater\033[0m\033[1;32m than \033[1;34m{0}\033[0m\033[1;32m;\033[0m".format(minLimit))
                countdownMiniGame(2)
            elif int(guess) > maxLimit:
                print("\033[7;31mInvalid input;\033[0m \033[1;32mPlease enter a number \033[1;34mless\033[0m\033[1;32m than \033[1;34m{0}\033[0m\033[1;32m;\033[0m".format(maxLimit))
                countdownMiniGame(2)
            elif not guess.isdigit():
                print("\033[7;31mInvalid input;\033[0m \033[1;32mPlease enter a number.\033[0m")
                countdownMiniGame(2)
            elif int(guess) > random_number:
                print("\033[1;32mYou're number is \033[0m\033[1;34mhigher\033[0m\033[1;32m.")
                countdownMiniGame(2)
            elif int(guess) < random_number:
                print("\033[1;32mYou're number is \033[0m\033[1;34mlower\033[0m\033[1;32m.")
                countdownMiniGame(2)
            else:
                print("\033[7;32mCongratulations!\033[0m\033[1;34m You guessed the number!\033[0m")
                print("\n\033[1;32mLaunching \033[0m\033[1;34m"+game_choice+"\033[0m\033[1;32m in\033[1;32m")
                countdown(10)
                game["last_played"] = time.time()
                with open("platforms.json", "w") as f:
                    json.dump(platforms, f, indent=4)
                os.startfile(game["game_location"])
                break

    else:
        print("Invalid choice")

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)
    print("\033[1;32mStarting game...\033[1;32m")
    time.sleep(2)

def countdownMiniGame(seconds):
    print("\nYou can try again in ")
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)
    print("Restarting...")
    time.sleep(1)
    os.system('cls')

with open("platforms.json") as f:
    platforms = json.load(f)

while True:
    main_menu()
    choice = input("\033[7;32m Choice: \033[0m ")
    os.system('cls' if os.name=='nt' else 'clear')  # Clear console after each choice
    if choice == "exit":
        break
    elif choice == "platforms":
        platforms_menu(platforms)
    else:
        print("Invalid choice")