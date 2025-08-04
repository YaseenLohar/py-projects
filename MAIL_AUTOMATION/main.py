#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#OPEN THE NAMES FILE AS A LIST
with open("Input/Names/invited_names.txt") as nam:
    n=nam.readlines()

# OPEN THE LETTER FILE AS A LIST OF LINES
with open("Input/Letters/starting_letter.txt") as file:
    l = file.readlines()
word = "[name]"

# REMOVE NEXT LINE ESCAPE SEQUENCE \n FROM EACH LINE
for y in range(len(n)-1):
    n[y]=n[y].strip()

# REPLACE EACH NAME WITH THE NEXT AND CREATE NEW INVITE TEXT FILES IN THE DESTINATION FOLDER
for x in n:
    l[0] = l[0].replace(word,x)
    word=x
    with open(f"../Mail Merge Project Start/Output/ReadyToSend/inv_{x}.txt","w") as out:
        out.writelines(l)




