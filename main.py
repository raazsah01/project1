import random

def guessing_game():
    # Step 1: Computer selects a random number
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        # Step 2: User inputs their guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Step 3: Check if the guess is correct
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# Run the game
guessing_game()

