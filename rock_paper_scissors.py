import random

MOVES = ["rock", "paper", "scissors", "spock", "lizard"]
VALID_CHOICES = ["rock", "r","paper", "p", "scissors", "sc",
                 "spock", "sp", "lizard", "l"]

def prompt(message):
    """Prints message with the given format"""
    print(f"==> {message}")

def display_winner(player, computer):
    """Announces winner of rock paper scissors"""

    prompt(f"You chose {player}, computer chose {computer}")

    if player == computer:
        prompt("It's a tie!")
    elif player_wins(player, computer):
        prompt("You win!")
    else:
        prompt("Computer wins!")

def player_wins(player_choice, computer_choice):
    """Determines if player won"""

    if ((player_choice == "rock" and\
         (computer_choice == "scissors" or computer_choice == "lizard")) or

        (player_choice == "scissors" and\
         (computer_choice == "paper" or computer_choice == "lizard")) or

        (player_choice == "paper" and\
         (computer_choice == "rock" or computer_choice == "spock")) or

        (player_choice == "spock" and\
         (computer_choice == "scissors" or computer_choice == "rock")) or

        (player_choice == "lizard" and\
         (computer_choice == "paper" or computer_choice == "spock"))):
        return True
    else:
        return False
    
def convert():
    global choice
    global computer_choice

    if choice == "r":
        choice = "rock"
    elif choice == "sc":
        choice = "scissors"
    elif choice == "p":
        choice = "paper"
    elif choice == "sp":
        choice = "spock"
    elif choice == "l":
        choice = "lizard"

    if computer_choice == "r":
        computer_choice = "rock"
    elif computer_choice == "sc":
        computer_choice = "scissors"
    elif computer_choice == "p":
        computer_choice = "paper"
    elif computer_choice == "sp":
        computer_choice = "spock"
    elif computer_choice == "l":
        computer_choice = "lizard"
    
while True:
    prompt('Choose one: rock (r), paper (p),' + 
            'scissors (sc), spock (sp), spock (sp)')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    convert()

    display_winner(choice, computer_choice)

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()

    while answer not in ("y", "n"):
        prompt('Please enter "y" or "n".')
        answer = input().lower()
        
    if answer[0] != "y":
        break
