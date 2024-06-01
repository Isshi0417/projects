import random

VALID_CHOICES = ["rock", "paper", "scissors", "spock", "lizard"]

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

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()

    while answer not in ("y", "n"):
        prompt('Please enter "y" or "n".')
        answer = input().lower()
        
    if answer[0] != "y":
        break
