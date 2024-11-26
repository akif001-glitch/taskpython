# Welcome message
print("Welcome to Rock, Paper, Scissors!")
print("You will play against the computer.")
print("Type 'rock', 'paper', or 'scissors' to play.")
print("Type 'quit' to exit the game at any time.")

# Main game loop
playing = True
while playing:
    # Initialize scores
    player_score = 0
    computer_score = 0
    rounds = 5  # Number of rounds to play

    # Loop for the number of rounds
    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number}/{rounds}:")
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        # Check if the user wants to quit
        if player_choice == 'quit':
            print("Thanks for playing! Goodbye!")
            playing = False
            break  # Exit the while loop

        # Validate the player's choice
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue  # Skip to the next iteration of the for loop

        # Computer's choice
        computer_choice = ['rock', 'paper', 'scissors'][round_number % 3]  # Simple way to choose for the example
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

    # Display final scores
    print("\nFinal Scores:")
    print(f"You: {player_score} | Computer: {computer_score}")

    # Determine overall winner
    if player_score > computer_score:
        print("Congratulations! You are the overall winner!")
    elif player_score < computer_score:
        print("The computer is the overall winner! Better luck next time!")
    else:
        print("It's a draw overall!")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        playing = False  # Exit the while loop