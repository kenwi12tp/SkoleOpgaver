import random as rnd
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

        if guessed == True:
            retry = input("\nwould you like to play again? yes or no\n")
            if retry.lower() == "yes" or retry.lower() == "y":
                guessed = False
                continue
            if retry.lower() == "no" or retry.lower() == "n":
                print("thanks for playing")
                break
game()