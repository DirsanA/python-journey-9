import random

# Ask for player count
num_players = input("Please enter the number of players: ")
player_name_array = []
max_game = 2  # number of rounds each player gets

def roll():
    random_roll = random.randint(1, 6)
    print("Starting the game...")
    return random_roll

# Validate input
if num_players.isdigit():
    num_players = int(num_players)

    if num_players < 2 or num_players > 6:
        print("Please enter a valid number of players (between 2 and 6).")
    else:
        # Collect player names
        for i in range(num_players):
            name = input(f"Enter name for player {i+1}: ")
            player_name_array.append(name)

        # Each player rolls for each round
        for round_num in range(max_game):
            print(f"\n--- Round {round_num + 1} ---")
            for player in player_name_array:
                print(f"{player}'s turn:")
                rolled_num = roll()
                print("You rolled:", rolled_num)

else:
    print("Please enter a valid number.")
