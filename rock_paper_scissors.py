"""Import random module"""
import random

def prompt(message):
    """Prints message with the given format"""
    print(f"==> {message}")

def display_winner(player_move, computer_move):
    """Announces winner of rock paper scissors"""

    prompt(f"You chose {player_move}, computer chose {computer_move}")

    if player_move == computer_move:
        prompt("It's a tie!")
    elif player_wins(player_move, computer_move):
        prompt("You win!")
    else:
        prompt("Computer wins!")

def player_wins(player_move, computer_move):
    """Determines if player won"""

    return bool((player_move == "rock" and\
         (computer_move in ("scissors", "lizard"))) or

        (player_move == "scissors" and\
         (computer_move in ("paper", "lizard"))) or

        (player_move == "paper" and\
         (computer_move in ("rock", "spock"))) or

        (player_move == "spock" and\
         (computer_move in ("scissors", "rock"))) or

        (player_move == "lizard" and\
         (computer_move in ("paper", "spock"))))

def convert(short_choice):
    """Converts short answers to complete ones"""
    if short_choice == "r":
        short_choice = "rock"
    elif short_choice == "sc":
        short_choice = "scissors"
    elif short_choice == "p":
        short_choice = "paper"
    elif short_choice == "sp":
        short_choice = "spock"
    elif short_choice == "l":
        short_choice = "lizard"

    return short_choice

def score_board(p_score, c_score):
    """Draws scoreboard"""
    print(' ' + '_' * 19)
    print('| Player | Computer |')
    print(f'|   {p_score}    |    {c_score}     |')
    print(' ' + '￣' * 10)

# Constants
MOVES = ["rock", "paper", "scissors", "spock", "lizard"]
VALID_CHOICES = ["rock", "r","paper", "p", "scissors", "sc",
                 "spock", "sp", "lizard", "l"]
WELCOME = "Welcome to Rock Paper Scissors Spock Lizard!"

# pylint: disable=C0103 (Variables not constants)
player_score = 0
computer_score = 0

# Rock Paper Scissors Spock Lizard
print("+" * len(WELCOME))
print(WELCOME)
print("+" * len(WELCOME))

while player_score < 3 and computer_score < 3:
    # Play round
    prompt('Choose one: rock (r), paper (p),' +
            'scissors (sc), spock (sp), spock (sp)')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    print("++++++++++++++++++++++++++++++++++++++++++++")

    computer_choice = random.choice(VALID_CHOICES)

    choice = convert(choice)
    computer_choice = convert(computer_choice)

    # Results
    display_winner(choice, computer_choice)

    if choice == computer_choice:
        pass
    elif player_wins(choice, computer_choice):
        player_score += 1
    else:
        computer_score += 1

    score_board(player_score, computer_score)
    print("++++++++++++++++++++++++++++++++++++++++++++")
