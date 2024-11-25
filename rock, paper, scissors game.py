import random
# Function to get player's choice and the computer's choice
name= input ("Enter your name ")
print(f"Hello {name} lets play Game ")
def get_game():
    player_choice = input("Enter your choice to play the game (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices  # Fixed typo here, 'retrun' -> 'return'
# Function to check the winner
def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock" and computer == "scissors":
        return "You win!"
    elif player == "paper" and computer == "rock":
        return "You win!"
    elif player == "scissors" and computer == "paper":
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
def play_game():
    while True:
        choices = get_game()  # Get choices from both player and computer
        result = check_win(choices["player"], choices["computer"])  # Check the winner
        print(result)
        
        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print(f"Thanks for playing! Goodbye! {name}")
            break  # Exit the loop if the player doesn't want to play again

# Run the game
play_game()
