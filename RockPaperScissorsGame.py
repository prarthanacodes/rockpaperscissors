# This is a Rock, Paper, Scissors game. This is completly fair. Best of three games.
# The computer's choices are pre-determined.
# I wrote r, p, and s to make typing faster, but r means Rock, p means Paper and s means scissors.
# Additionally, when I wrote 1's and 0's for the win_or_lose function, 1 is win and 0 is lose. Draw is neither.
import random
# The variable below is used to check if a round needs to be re-done.
draw = False
# The variable 'score' is to keep track of who won. Initializing it to 0
score = 0
# List
computer_choice_list = ["r", "p", "s"]


def invalid_user_input(user_choice):
    while user_choice != "r" and user_choice != "p" and user_choice != "s":
        print("Invalid response.")
        user_choice = input("Rock, Paper, or Scissors? (r/p/s) ")
        # This one works as expected


def draws(draw):
    if draw == True:
        print("It was a draw!\nGo again!")
        draw_computer_choice = computer_choice_list[random.randint(0, 2)]
        user_draw_input = input("Rock, paper, or scissors? (r/p/s) ")
        invalid_user_input(user_draw_input)
        determining_round_wins(user_draw_input, draw_computer_choice)


def determining_round_wins(user_choice, computer_choice):
    if user_choice == "r" and computer_choice == "r":
        draw = True
        draws(draw)
    elif user_choice == "r" and computer_choice == "p":
        draw = False
        draws(draw)
        print("The computer chose paper.\nThe computer wins this round!")
        return 0
    elif user_choice == "r" and computer_choice == "s":
        draw = False
        draws(draw)
        print("The computer chose scissors\nYou win this round!")
        return 1
    elif user_choice == "p" and computer_choice == "p":
        draw = True
        draws(draw)
    elif user_choice == "p" and computer_choice == "s":
        draw = False
        draws(draw)
        print("The computer chose scissors.\nThe computer wins this round!")
        return 0
    elif user_choice == "p" and computer_choice == "r":
        draw = False
        draws(draw)
        print("The computer picked rock.\nYou win this round!")
        return 1
    elif user_choice == "s" and computer_choice == "s":
        draw = True
        draws(draw)
    elif user_choice == "s" and computer_choice == "r":
        draw = False
        draws(draw)
        print("The computer picked rock.\nThe computer wins this round!")
        return 0
    elif user_choice == "s" and computer_choice == "p":
        draw = False
        draws(draw)
        print("Computer picked paper.\nYou win this round!")
        return 1
    else:
        print("Something is fishy")


computer_choice_1 = computer_choice_list[random.randint(0, 2)]
computer_choice_2 = computer_choice_list[random.randint(0, 2)]
computer_choice_3 = computer_choice_list[random.randint(0, 2)]

# Round 1
user_choice_1 = input("Rock, Paper or Scissors? (r/p/s) ").lower()
invalid_user_input(user_choice_1)
win_or_lose = determining_round_wins(user_choice_1, computer_choice_1)
if win_or_lose == 1:
    score += 1
print(f"Your current score is: {score}")


# Round 2
user_choice_2 = input("Rock, Paper or Scissors? (r/p/s) ").lower()
invalid_user_input(user_choice_2)
win_or_lose = determining_round_wins(user_choice_2, computer_choice_2)
if win_or_lose == 1:
    score += 1
print(f"Your current score is: {score}")


# Round 3
user_choice_3 = input("Rock, Paper or Scissors? (r/p/s) ").lower()
invalid_user_input(user_choice_3)
win_or_lose = determining_round_wins(user_choice_3, computer_choice_3)
if win_or_lose == 1:
    score += 1
print(f"Your current score is: {score}")

# FINAL SCORE!!
if score >= 2:
    print("CONGRATS! YOU WON THIS GAME OF ROCK, PAPER AND SCISSORS!")
else:
    print("Sorry, the computer won. Better luck next time.")
