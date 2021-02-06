import random
import os
from words import wordList

#function to pick random word
def getWord():
    word = random.choice(wordList)
    return word.upper()

#the game rules
def play(word):
    wordCompleted = "-" * len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 6

    print("Hangman mini-game by @miljkovicjovan")    
    print(display(tries))
    print(wordCompleted)
    print('\n')

    while not guessed and tries > 0:
        guess = input("Guess a letter from the secret word: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                os.system('cls')
                print("You have already tried that!")
            elif guess not in word:
                os.system('cls')
                print(guess, "is not in the secret word!")
                tries -= 1
                guessedLetters.append(guess)
            else:
                os.system('cls')
                print("Good job,", guess, "is in the secret word!")
                guessedLetters.append(guess)
                wordAsList = list(wordCompleted)
                indices =[i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    wordAsList[index] = guess
                wordCompleted = "".join(wordAsList)
                if "-" not in wordCompleted:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedWords:
                os.system('cls')
                print("You have already tried that!")
            elif guess != word:
                os.system('cls')
                print(guess, "is not the secret word!")
                tries -= 1
                guessedWords.append(guess)
            else:
                guessed = True
                wordCompleted = word
        else:
            os.system('cls')
            print("Not valid input, Try again!")
        
        print(display(tries))
        print(wordCompleted)
        print('\n')

    if guessed:
        os.system('cls')
        print("Congrats you have won!")
    else:
        os.system('cls')
        print("You ran out of tries the word was, ", word)

def display(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

os.system('cls')
word = getWord()
play(word)
while input("Play again? (Y/N) ").upper() == "Y":
    os.system('cls')
    word = getWord()
    play(word)