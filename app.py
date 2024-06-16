# write 'hello world' to the console
print('hello world')


#Rock beats scissors.
#Scissors beat paper.
#Paper beats rock.
#  the computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like you. Your interaction in the game will be through the console (Terminal).

#The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
#At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
#By the end of each round, the player can choose whether to play again.
#Display the player's score at the end of the game.
#The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
#Create rock paper scissor code from the above prompt in python
import random

def rock_paper_scissors():

    while True:
        player = input("Enter rock, paper, or scissors: ").lower()
        computer = random.choice(["rock", "paper", "scissors"])

        if player not in ["rock", "paper", "scissors"]:
            print("Invalid option. Please try again.")
            continue

        if player == computer:
            print(f"Both players selected {player}. It's a tie!")
        elif player == "rock":
            if computer == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif player == "paper":
            if computer == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif player == "scissors":
            if computer == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

rock_paper_scissors()

