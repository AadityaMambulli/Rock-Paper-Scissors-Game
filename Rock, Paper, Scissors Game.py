# Rock, Paper, Scissor Game
import random
import time

def play_game():
    options = ["rock", "paper", "scissors"]

    print("*************************")
    print("Rock, Paper, Scissors Game")
    print("*************************")

    while True:
        player = input("Choose a move (rock, paper, scissors): ").lower()
        if player not in options:
            print("Invalid input. Please choose either 'rock', 'paper', or 'scissors'.")
            continue

        cpu = random.choice(options)
        print("Loading... Please wait...")
        time.sleep(2)
        print(f"You chose '{player}' & Computer chose '{cpu}'.")

        if player == cpu:
            print("It's a tie!")
        elif (
            (player == "rock" and cpu == "scissors") or
            (player == "scissors" and cpu == "paper") or
            (player == "paper" and cpu == "rock")
        ):
            print("You win!")
        else:
            print("You lose!")
            break

if __name__ == '__main__':
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes / no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break
