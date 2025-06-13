# INTRODUCTION
print("Welcome to Hangman!")
print("Player one enter the word to be guessed!")
word=input("Type the word here: ").lower()

# GENERATING UNDERSCORES
lis=list(word)
lis2=[]
for x in lis:
    lis2.append("_")

em=list(enumerate(lis))



# DEFINE A FUNCTION TO CONVERT LIST TO STRING
def list_to_str(l):
    st=l[0]
    for x in range(1,len(l)):
        st= st + str(l[x])
    print(st)

counter = 0
# PLAYER2 INPUT
print("\nPlayer2 begin guessing the word!")
while lis2 != lis:
    print("guess a letter!")
    guess= input("type the letter here :\n").lower()
    if counter == 5:
        print("You lose! :(")
        break
# EXISTENCE CHECK
    if guess not in lis:
        counter += 1
        print("Wrong letter!")
        list_to_str(lis2)
        print("\n")
    elif guess in lis and guess in lis2:
        print("Invalid, character already entered!\n")
        list_to_str(lis2)
        print("\n")
    elif guess in lis and guess not in lis2:
        for k in em:
            if k[1]==guess:
                lis2[k[0]]=k[1]
        list_to_str(lis2)
    
 
    
            
if lis2 == lis:
    print("You win! :)")
    print("the word is :")
    list_to_str(lis2)

