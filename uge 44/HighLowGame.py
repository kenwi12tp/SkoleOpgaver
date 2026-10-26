import random as rnd



def retry_function():
    while True:
        retry = input("\nwould you like to play again? yes or no\n").strip().lower()
        if retry in ("no", "n"):
            print("\nThank you for playing")
            return retry
        elif retry in ("yes", "y"):
            return retry
        else:
            print("you didnt write yes or no")

def numberGuessing(goal, count):
    while True:
        guess = input("Enter your guess: ")
        if guess.isdigit():
            guess = int(guess)
            if guess == goal:
                print("You guessed the right number congrats!!!")
                count += 1
                print(f"you used {count} guesses")
                break
            elif guess > goal:
                print("your guess was too high of a number")
                count += 1
            elif guess < goal:
                print("your guess was too low of a number")
                count += 1
        else:
            print("you didnt write a number")

print("this is a game about guessing what number the pc is thinking about")
def game():
    while True:
        count = 0
        goal = rnd.randint(1,100)
        numberGuessing(goal, count)
        retry = retry_function()
        if retry in ("no", "n"):
            break



game()