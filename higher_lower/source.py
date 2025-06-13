# import data and ASCII art

import random
from art import logo,vs              
from game_data import instagram_celebrities

# define the game as a callable function

def Higher_Lower():
   score = 0
   var1= random.choice(instagram_celebrities)
   instagram_celebrities.pop(instagram_celebrities.index(var1))
   var2 = random.choice(instagram_celebrities)
   instagram_celebrities.pop(instagram_celebrities.index(var2))
    
# use while loop to keep it running
   
   while True:
        
        print(logo,"\n")
        print(f" A is {var1['name']}, is from {var1['country']} and is a {var1['occupation']}\n.")
        print(vs,"\n")
        print(f" B is {var2['name']}, is from {var2['country']} and is a {var2['occupation']}\n.")
        guess = input(" Does B have Higher followers or Lower followers than A?:  ").lower()

# use higher and lower inputs to check, if true for higher, switch vars and compare again

        if guess == 'higher':
            if var1['follower_count'] < var2['follower_count']:
                print(" That is correct!")
                score+=1
                var1 = var2
                var2 = random.choice(instagram_celebrities)
                instagram_celebrities.pop(instagram_celebrities.index(var2))

            else:
                print("wrong answer you lose!")
                print(f"Your score is {score}")
                break

# if lower is true for B, random assign B and compare again

        elif guess == 'lower':
            if var1['follower_count'] > var2['follower_count']:
                print("That is correct!")
                score+=1
                var2=random.choice(instagram_celebrities)
                instagram_celebrities.pop(instagram_celebrities.index(var2))
            else:
                print("wrong answer you lose!")
                print(f"Your score is {score}")
                break
        if len(instagram_celebrities) == 0:
            print(" You're something else...")
            break



Higher_Lower()
       

        








    