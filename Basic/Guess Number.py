import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    attempts = 0

    while guess != random_number:
        try:
            guess = int(input(f"Guess a number between 1 and {x}: "))
            attempts += 1
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"Yay Congrats, {random_number} was correct! You guessed it in {attempts} attempts.\n")

def main():
    print(" Welcome to the Number Guessing Game!")
    
    while True:
        try:
            upper_limit = int(input("Enter the maximum number for the range (e.g., 10, 50, 100): "))
            guess(upper_limit)
        except ValueError:
            print("Please enter a valid number.")
            continue

        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
