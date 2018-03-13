#this is the popular game, Hangman
#the program will generate a random word, ask the user to guess a
#letter (or the word), and check the guess for correctness until the
#stick figure hangman shows up completely or the user guesses the word

import Hangman_board #makeshift Hangman gameboard
import random

def get_word():
    #randomly generates word from list of words
    wordlist = 'project java python program class method attribute object data science computer'.upper().split()
    return random.choice(wordlist).upper()

word = get_word()
correct = []
incorrect = []

#print('DEBUG:' + word) #this was used during design process to know which letters and
                        #words to input (and not) input; uncomment to know secret word

def game_board():
    #draws the gallows for the hangman game and displays the random word
    print(Hangman_board.Gallows[len(incorrect)])
    for i in word:
        if i in correct:
            print(i, end=' ')
        else:
            print('_', end=' ')
    print("\n\n")
    print("*** INCORRECT GUESSES ***")
    for i in incorrect:
        print(i, end=' ')
    print('\n*************************')

def user_input():
    #asks user to guess letter or word and appends that letter to correct or incorrect list
    while True:
        guess = input("Guess a letter or the word: ").upper()
            
        if len(guess) == len(word):
            if guess == word:
                correct.append(guess)
                break
            else:
                print("Sorry, that is not the correct word. Guess again.")
                break
            
        #vaildation of input                
        elif guess in correct or guess in incorrect:
            print("Invalid entry: You have already guessed that letter.")        
        elif len(guess) == 0:
            print("Invalid entry: Please enter at least one letter.")
        elif guess.isalpha() == False:
            print("Invalid entry: Please enter only letters.")
        elif len(guess) > 1 and len(guess) != len(word):
            print("Invalid entry: Please enter only one letter (or the length of the word).")
        else:
            break
    
    #appends input to correct or incorrect list
    if guess in word:
        print("Good guess! :)")
        for i in guess:
            correct.append(i)
    else:
        print("Sorry, that guess is incorrect :(")
        incorrect.append(guess)

def win_or_lose():
    #Check to see if the user has won or lost the game
    if len(incorrect) > 6:
        return 'L'
    for i in word:
        if i not in correct:
            return 'no win'
    return 'W'

while True:
    #runs the game in the global frame, displays end game results
    game_board()
    user_input()
    win_condition = win_or_lose()

    if win_condition == 'L':
        print(Hangman_board.Gallows[7])
        print("GAME OVER. THE WORD WAS: " + word)
        break
    elif win_condition == 'W':
        print(Hangman_board.Gallows[len(incorrect)])
        for i in word:
            print(i, end=' ')
        print("\n")
        print("YOU WIN!! THE WORD WAS: " + word)
        break
        
        
            
          
    
