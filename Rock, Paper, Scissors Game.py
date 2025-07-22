# Rock, Paper, Scissor Game
import random
import time

class RockPaperScissorsGame:
    def __init__(self):
        self.options = ["rock", "paper", "scissors"]

    def get_user_move(self):
        """Prompts user for input and validates it."""
        while True:
            move = input("Choose a move (rock, paper, scissors): ").lower()
            if move in self.options:
                return move
            else:
                print("Invalid input. Please choose either 'rock', 'paper', or 'scissors'.")

    def get_cpu_move(self):
        """Returns a random move for the computer."""
        return random.choice(self.options)

    def determine_winner(self, player, cpu):
        """Determines and prints the winner based on moves."""
        print("Loading... Please wait...")
        time.sleep(2)
        print(f"\nYou chose '{player}' & Computer chose '{cpu}'.\n")

        if player == cpu:
            print("It's a tie!")
            return "tie"
        elif (
            (player == "rock" and cpu == "scissors") or
            (player == "scissors" and cpu == "paper") or
            (player == "paper" and cpu == "rock")
        ):
            print("You win!\n")
            return "win"
        else:
            print("You lose!\n")
            return "lose"

    def play_round(self):
        """Plays one round of the game."""
        player = self.get_user_move()
        cpu = self.get_cpu_move()
        result = self.determine_winner(player, cpu)
        return result

    def start_game(self):
        """Starts the game and handles replay logic."""
        print("*************************")
        print("Rock, Paper, Scissors Game")
        print("*************************\n")

        while True:
            result = self.play_round()
            if result == "lose":
                break

        print("Game Over!")

def main():
    while True:
        game = RockPaperScissorsGame()
        game.start_game()

        replay = input("Do you want to play again? (yes / no): ").lower()
        if replay != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == '__main__':
    main()
