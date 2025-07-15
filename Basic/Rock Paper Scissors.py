import random

def play():
    user = input("What's your choice (rock, paper, scissors): ").lower()


    if user not in ['rock', 'paper', 'scissors']:
        return "Invalid choice. Please choose 'rock', 'paper', or 'scissors'."
    
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)

    print(f"Computer chose {computer}.")
    
    if user == computer:
        return f"Both chose {user}. It's a tie!"
    
    return winner(user, computer)

def winner(user, computer):
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'paper' and computer == 'rock') or \
       (user == 'scissors' and computer == 'paper'):
        return f"You win! {user} beats {computer}."
    else:
        return f"You lose! {computer} beats {user}."


print(play())
