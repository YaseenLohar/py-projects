from art import logo
print(logo)
from random import randint

def guess_the_number():
    guesses = 0
    diff= input("Enter the difficulty, 'easy' or 'hard': ").lower()              #inputs

    if diff == "easy":
        guesses = 10
    elif diff == 'hard':                        # game difficulty
        guesses = 5

    num = randint(1,100)                       
    flag=True
    while flag:

        if guesses==0:
            play = input("Do you want to try again? Y or N: ").lower()
            if play == 'y':
                guess_the_number()                                      # restart game if guesses are over
            else:
                break

        gues= int(input(" Make a guess:"))

        if gues > num:
            print("too high")
            guesses-=1
            print(f"You have {guesses} guesses left")
        elif gues < num:
            print("too low")
            guesses-=1                                                     # decrement number of guesses left
            print(f"you have {guesses} guesses left")
        elif gues == num:
            print(f"the number is {num}.\n you win!!!")
            play1 = input("Do you want to try again? Y or N: ").lower()
            if play1 == 'y':
                guess_the_number()                                      # ask to replay game if achieved a win
            elif play1 == 'n':
                flag=False


guess_the_number()

