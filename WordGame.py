import random
def get_random_word():
    words = ["pizza","cheese","apples"]
    word = words[random.randint(0,len(words)-1)] 
    return word

def show_word(word):      #in (word) its (_____) ie.5 "_"
    for character in word:   # for each character which is "_" in this used for loo[ to print
        print(character, " ",end = "")
    print("")

def get_guess():
    print("Enter a Letter: ")
    return input()

def process_letter(letter, secret_word, blanked_word ):
    result = False

    for i in range (0, len(secret_word)):
        if secret_word[i] == letter:
            result = True
            blanked_word[i] = letter
    
    return result

def print_strikes(number_of_strikes):
    for i in range(0, number_of_strikes):
        print("X"," ",end = "")
    print("")
    
    
def playWordGame():
    strikes = 0
    max_strikes = 3
    playing = True
    word = get_random_word()
    blanked_word = list("_" * len(word))  

    while playing:
        show_word(blanked_word)  ##show_word(_____) ie.5 "_"
        letter = get_guess()
        found = process_letter(letter, word, blanked_word)

        if not found:
            strikes += 1
            print_strikes(strikes)
            
        if strikes >= max_strikes:
            playing = False

        if not "_" in blanked_word:
            playing = False

    if strikes >= max_strikes:
        print("Looser")
    else:
        print("Winner!")

    
        
    

print("Game started")
playWordGame()
print("Game Over")
 
