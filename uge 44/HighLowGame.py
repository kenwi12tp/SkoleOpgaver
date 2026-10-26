import random as rnd

def retry_function(guessed):
    if guessed == True:
        retry = input("\nwould you like to play again? yes or no\n")
        if retry.lower() == "yes" or retry.lower() == "y":
            guessed = False
            return guessed, retry

        if retry.lower() == "no" or retry.lower() == "n":
            print("thanks for playing")
            return retry


print("this is a game about guessing what number the pc is thinking about")
def game():
    guessed = False
    while guessed == False:
        goal = rnd.randint(1,100)
        while True:
            guess = input("Enter your guess: ")
            if guess.isdigit():
                guess = int(guess)
                if guess == goal:
                    print("You guessed the right number congrats!!!")
                    guessed = True
                    break
                elif guess > goal:
                    print("your guess was too high of a number")
                elif guess < goal:
                    print("your guess was too low of a number")
            else:
                print("you didnt write a number")

        guessed, retry = retry_function(guessed)
        if retry.lower() == "yes" or retry.lower() == "y":
            continue
        if retry.lower() == "no" or retry.lower() == "n":
            break

game()