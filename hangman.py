# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import re

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    #compare unique letters of secret_word
    if list(set(secret_word)).sort() == letters_guessed.sort():
        return True
    else:
        return False

    
    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    '''
    if letter guessed (new) in secret word
        add it to output in the correct place
    '''
    guessed = []
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            guessed.append(secret_word[i])
        else:
            guessed.append("_ ")
    return ''.join(guessed)
            

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alpha = list(string.ascii_lowercase)  #all the letters
    for letter in letters_guessed:
        alpha.remove(letter)
	
    return ''.join(alpha)
    
 
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is ",str(len(secret_word)),  "letters long.")
    #initialising 
    guesses_left = 6
    letters_guessed = []
    warnings = 3
    
    #repeating bits
    while guesses_left>0:
        print("-------------")
        print("You have", guesses_left,  "guesses left.")
        print("Available letters: ",''.join(get_available_letters(letters_guessed)))
        letter = input("Please guess a letter:").lower()
        if letter.isalpha(): #validating input
            pass 
        else:
            if warnings>0 :
                warnings -= 1
                print("Oops! That is not a valid letter.You have ", warnings, "warnings left.")
                continue
            else:
                guesses_left -= 1
                continue
        if letter in letters_guessed: #already guessed letter is input
            if warnings>0:
                warnings -= 1
                print("Oops! You've already guessed that letter.",
                      "You now have ", warnings, "warnings")
                continue
            else:
                guesses_left -=1
                continue
        else:
            letters_guessed.append(letter) #valid new input 
            
              

            
        
        if letter in secret_word:        
            print("Good guess:",''.join(get_guessed_word(secret_word, letters_guessed)))
        else:
            print("Oops! That letter is not in my word:",''.join(get_guessed_word(secret_word, letters_guessed)))
            if letter in "aeiou":
                guesses_left -=2   #wrong vowel guessed
            else:
                guesses_left -= 1 #wrong consonant guessed
        if "_" not in get_guessed_word(secret_word, letters_guessed):  #all letters guessed
            print("Congratulations, you won!\n",
                "Your total score for this game is:",
                   guesses_left*len(set(secret_word)))
            return
    if guesses_left == 0:
        print("Sorry, you ran out of guesses. The word was ",secret_word)
            



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass
    



def show_possible_matches(my_word,letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    #filler is the regex element signifying 'not already guessed letters' or ' correct letters'
    stripped_my_word = re.sub(r'_| ','',my_word)
    
    filler = "[^"+''.join(set(stripped_my_word +''.join(letters_guessed)))+"]"

    
      
    # replace _ with [^str]  in my_word to get final regex r
    my_word_regex = my_word.replace("_ ",filler)

    r = re.compile(my_word_regex)
    
    result_list = list(filter(r.match,wordlist)) #TODO better way of stopping after 10 results
    print("Possible word matches are:\n",' '.join(result_list[:10]))
    
    



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is ",str(len(secret_word)),  "letters long.")
    #initialising 
    guesses_left = 6
    letters_guessed = []
    warnings = 3
    
    #repeating bits
    while guesses_left>0:
        print("-------------")
        print("You have", guesses_left,  "guesses left.")
        print("Available letters: ",''.join(get_available_letters(letters_guessed)))
        letter = input("Please guess a letter:").lower()
        if letter.isalpha() or letter == '*': #validating input
            pass 
        else:
            if warnings>0 :
                warnings -= 1
                print("Oops! That is not a valid letter.You have ", warnings, "warnings left.")
                continue
            else:
                guesses_left -= 1
                continue
        if letter == '*':
            my_word = get_guessed_word(secret_word, letters_guessed)
            show_possible_matches(my_word,letters_guessed)
            continue

        if letter in letters_guessed: #already guessed letter is input
            if warnings>0:
                warnings -= 1
                print("Oops! You've already guessed that letter.",
                      "You now have ", warnings, "warnings")
                continue
            else:
                guesses_left -=1
                continue
        else:
            letters_guessed.append(letter) #valid new input 
            
              

            
        
        if letter in secret_word:        
            print("Good guess:",''.join(get_guessed_word(secret_word, letters_guessed)))
        else:
            print("Oops! That letter is not in my word:",''.join(get_guessed_word(secret_word, letters_guessed)))
            if letter in "aeiou":
                guesses_left -=2   #wrong vowel guessed
            else:
                guesses_left -= 1 #wrong consonant guessed
        if "_" not in get_guessed_word(secret_word, letters_guessed):  #all letters guessed
            print("Congratulations, you won!\n",
                "Your total score for this game is:",
                   guesses_left*len(set(secret_word)))
            return
    if guesses_left <= 0:
        print("Sorry, you ran out of guesses. The word was ",secret_word)
            


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
   # secret_word = choose_word(wordlist)
#    secret_word = "app"
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
