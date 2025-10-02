import random

user_win = 0
computer_win = 0
draw = 0

choose_array = ["rock", "paper", "scissor"]

while True:
    user_choose = input("Please enter your choice (rock, paper, scissor) or q to quit: ").lower()

    if user_choose in ["q", "quit"]:
        break

    if user_choose not in choose_array:
        print("Invalid choice, try again!")
        continue

    computer_choose = random.choice(choose_array)
    print("Computer chose:", computer_choose)

    if user_choose == computer_choose:
        print("Draw")
        draw += 1
    elif (user_choose == "rock" and computer_choose == "scissor") or \
         (user_choose == "scissor" and computer_choose == "paper") or \
         (user_choose == "paper" and computer_choose == "rock"):
        print("You won!")
        user_win += 1
    else:
        print("You lost!")
        computer_win += 1

print("\nThanks for playing!")
print("User wins:", user_win)
print("Computer wins:", computer_win)
print("Draws:", draw)
