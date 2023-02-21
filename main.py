import json
import time
import random
import datetime
import os
import platform
import debug

debugEnv = debug.debugEnvironment
debugJSONLocation = debug.testingPlatforms
if(debugJSONLocation):
    platformsJsonLocation = "debugPlatforms.json"
else:
    platformsJsonLocation = "platforms.json"

if platform.system() == 'Windows':
    os.system('color')

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
            time_difference = datetime.timedelta(seconds=float(time.time() - last_played))
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
        print("\033[1;34m     " + game_name + "\033[0m \033[1;32m-\033[0m " + f"{time_difference_formatted}" + "\033[0m")
    game_choice = input("\n \033[7;32m Game choice: \033[0m ")
    if game_choice == "back to menu":
        return
    if game_choice in games:
        game = games[game_choice]
        global random_number

        def extract_time(diff):
            days, seconds = divmod(diff, 86400)
            hours, seconds = divmod(seconds, 3600)
            minutes, seconds = divmod(seconds, 60)
            hours += days * 24
            return days, hours, minutes, seconds

        def generate_number():
            
            diff = int(time.time() - last_played_old)
            days, hours, minutes, seconds = extract_time(diff)
            if(debugEnv):
                messageDebug = f"(debug): {hours} hours have passed"
                print(messageDebug)
            global minLimit
            global maxLimit
            if(hours > 72):
                minToAdd = 1
                maxToAdd = 5
            elif(hours > 56):
                minToAdd = 1
                maxToAdd = 10
            elif(hours > 48):
                minToAdd = 10
                maxToAdd = 100
            elif(hours > 36):
                minToAdd = 100
                maxToAdd = 1000
            elif(hours > 24):
                minToAdd = 1000
                maxToAdd = 10000
            elif(hours > 18):
                minToAdd = 10000
                maxToAdd = 90000
            elif(hours > 12):
                minToAdd = 600000
                maxToAdd = 900000
            elif(hours > 8):
                minToAdd = 500000
                maxToAdd = 900000
            elif(hours > 6):
                minToAdd = 100000
                maxToAdd = 350000
            elif(hours >= 3):
                minToAdd = 1000000
                maxToAdd = 35000000
            elif(hours >= 1):
                minToAdd = 5000000
                maxToAdd = 10000000
            else:
                minToAdd = 5000000
                maxToAdd = 50000000
            minLimit = random.randint(minToAdd, maxToAdd)
            maxLimit = random.randint(minToAdd + hours, maxToAdd + hours)
            if(minLimit > maxLimit):
                minLimit, maxLimit = maxLimit, minLimit
                if(debugEnv):
                    print(f"(debug): Swapping between minLimit({minLimit}) and maxLimit({maxLimit}) was necessary")

            elif(minLimit == maxLimit):
                minLimit -= 3
                if(debugEnv):
                    print(f"(debug): The value of minLimit({minLimit}) was decreased by 3, maxLimit({maxLimit})")
            if(debugEnv):
                print(f"(debug): minToAdd = {minToAdd}")
                print(f"(debug): maxToAdd = {maxToAdd}")
                print(f"(debug): minLimit = {minLimit}")
                print(f"(debug): maxLimit = {maxLimit}")
            random_number = random.randint(minLimit, maxLimit)
            if(debugEnv):
                print(f"(debug): random_number = {random_number}")
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
                with open(platformsJsonLocation, "w") as f:
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

with open(platformsJsonLocation) as f:
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