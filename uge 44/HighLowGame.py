import random as rnd


###this function lets the user chose if they want to play the game again or not
def retry_function():
    while True:

        #here the user will chose if they want to retry or not by typing yes or no
        retry = input("\nwould you like to play again? yes or no\n").strip().lower()

        #the if statements here dictates what happens when the user either writes yes or no
        if retry in ("no", "n"):
            print("\nThank you for playing")
            return retry
        elif retry in ("yes", "y"):
            return retry

        #just input valdiation so they cant write anything wrong
        else:
            print("you didnt write yes or no")

### this function lets the user guess what number the pc is thinking of,
### the number the pc is thinking of is goal
def numberGuessing(goal):
    count = 0
    while True:
        guess = input("Enter your guess: ")

        #checking to make sure the user wrote a number
        if guess.isdigit():

            #turning it into an int so i can compare the goal and the guess
            guess = int(guess)

            #the diffrent if statements dictates what happens when the user guesses too low or too high
            #or the exact number the pc is thinking of
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
            elif count == 10:
                print(f"you have used all your guesses and have lost the game the number was {goal}")

        #this is what happens when the user doesnt write a number
        else:
            print("you didnt write a number")

#this is the main function that will play the game
def game():
    while True:

        #the pc's number
        goal = rnd.randint(1,100)

        #the player guessing
        numberGuessing(goal)

        #if the player want to retry
        retry = retry_function()
        if retry in ("no", "n"):
            break

#this is just a little intro
print("this is a game about guessing what number the pc is thinking about\n"
      "you need to guess the number with a max amount of 10 guesses")

#calling the main function that is called game
game()