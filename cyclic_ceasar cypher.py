def ceasar_cypher():
    """This function inputs a word, a shift value from the user and encodes it using the shift on an alphabet key."""


    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print("WELCOME TO CEASAR CYPHER ENCRYPTION!!")
    direction= input("Enter ENCODE to encode, or DECODE to decode: ").lower()
    shift=int(input("\nshift amount: "))
    text = input("\nEnter the word: ").lower()

    if shift > len(alphabet):
        shift = shift % len(alphabet)

    ###################################################################################################################

    def right_shift(k,n):         # does'nt return anything
            if n == len (k):          # same list
                print(k)
            elif n < len(k):          # shifting by 1, n times.
                for t in range(1,n+1):
                    global new
                    new=[]
                    for x in k:
                        if k.index(x) < (len(k)-1):
                            x=k[k.index(x) + 1]
                            new.append(x)
                        elif k.index(x) == (len(k)-1):
                            x = k[0]
                            new.append(x)                
                    right_shift(new,n-1)                  # calling function within fumction (recursion)

    right_shift(alphabet,shift)
    #print(new)

    ################################################################################################################

    def encode(word):                 # function to encode
        
        indices=[]                     # extract indices of letters in input wrt to list alphabet
        word_list= list(word)

        for x in word_list:
            if x in alphabet:
                indices.append(alphabet.index(x))
    
        encoded= []
                                      
        for x in indices:
            encoded.append(new[x])            # extract letters in those indices from list new       
    
        encoded_word= encoded[0]             
        for x in encoded[1::]:
            encoded_word += x                 # convert to string

        k=list(encoded_word)                   # this part is to keep the spaces and symblos as they are and at the same positions
        sym_ind=[]
        sym=[]
        for x in word_list:
            if x not in alphabet:
                sym_ind.append(word_list.index(x))
                sym.append(x)
        
        for x in range(0,len(sym)):
            k.insert(sym_ind[x],sym[x])
        
        new_encoded_word= k[0]               # convert to string 
        for x in k[1::]:
            new_encoded_word += x


        print(f"The encoded word is {new_encoded_word}." )

    ##########################################################################################################################


    def decode(word):                           #function to decode
        ind=[]
        word_list=list(word)
        for x in word_list:
            if x in alphabet:
                ind.append(new.index(x))            # extrace indices of given test wrt to shifted key sequence.
    

        decoded=[]
        for x in ind:
            decoded.append(alphabet[x])          # source letters at same index as (new) in orignal key sequence.
    
        decoded_word=decoded[0]

        for x in decoded[1::]:                   #convert to string
            decoded_word += x
        
        k=list(decoded_word)                   # this part is to keep the spaces and symbols as they are and at the same positions
        sym_ind=[]
        sym=[]
        for x in word_list:
            if x not in alphabet:
                sym_ind.append(word_list.index(x))
                sym.append(x)
        
        for x in range(0,len(sym)):
            k.insert(sym_ind[x],sym[x])
        
        new_encoded_word= k[0]               # convert to string 
        for x in k[1::]:
            new_encoded_word += x

        print(f"decoded word is {decoded_word}.")


    ###########################################################################################################################


    if direction == "encode":
        encode(text)
    elif direction == "decode":
        decode(text)
    elif direction != "encode" and direction != "decode":
        print("Enter only ENCODE or DECODE!")

ceasar_cypher()

while True:
    cont=input("Do you want to continue?: Y or N").lower()
    if cont=='y':
        ceasar_cypher()
    else:
        break





    



