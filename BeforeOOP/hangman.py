#Hangman in Python

import random
#dictionary of key:()
hangman_art = {0: ("   ",
                   "    "
                   "    "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}
words = ("apple", "orange", "banana", "coconut", "pineapple")

def displayWords(showIndices, word):
    wordLength = len(word)
    for i in range(wordLength):
        if i in showIndices:
            print(word[i], end=" ")
        else:
            print("_", end=" ")
    print("\n")

def initializeGame(wordsIndex):
    # 1. Display the guess word i.e. randomly choose few letters from the words and display as an initial question to user.
    word = words[wordsIndex]
    wordLength = len(word)
    wordsLeftToGuess = set()
    print(word, wordLength)
    print("Guess the word \n")
    guessCount = 0
    hint = 0
    if wordLength <= 6:
        hint = 2
    elif wordLength >= 6 or wordLength >= 8:
        hint = 3
    elif wordLength >= 10:
        hint = 4
    showIndices = set(random.sample(range(wordLength), hint))
    wordsLeftToGuess = {word[i] for i in range(wordLength) if i not in showIndices}
    displayWords(showIndices, word)
    return showIndices, wordsLeftToGuess, guessCount, wordsLeftToGuess, word, wordLength


def main():
    wordsIndex = 0
    guessComplete = False
    playGame = True
    showIndices, wordsLeftToGuess, guessCount, wordsLeftToGuess, word, wordLength = initializeGame(wordsIndex)
    while playGame:
        # 2. If any letters are correct then show the actual place of a letter in the word
        letter = input("Enter your guess letter: ")
        if letter in wordsLeftToGuess:
            wordsLeftToGuess.remove(letter)
            indices = [i for i, char in enumerate(word) if char == letter]
            showIndices.update(indices)
            displayWords(showIndices, word)
            if len(showIndices) == wordLength:
                displayWords(showIndices, word)
                print(f"Congratulations.")
                choice = input("Do you want to play again y/n: ").upper()
                if choice == "Y":
                    wordsIndex += 1
                    showIndices, wordsLeftToGuess, guessCount, wordsLeftToGuess, word, wordLength = initializeGame(wordsIndex)
                    continue
                else:
                    playGame = False
                    break

        # 3 If the letter doesn't appear in the word decrement the chances and show appropriate hangman image
        else:
            print("OPPS WRONG GUESS!!!")
            displayWords(showIndices, word)
            guessCount += 1
            print(f"Total guess left: {6 - guessCount}")
            for i in range(3):
                print(hangman_art[guessCount][i])
            if guessCount == 6:
                print("Game Over....")
                choice = input("Do you want to play again y/n: ").upper()
                if choice == "Y":
                    wordsIndex += 1
                    showIndices, wordsLeftToGuess, guessCount, wordsLeftToGuess, word, wordLength = initializeGame(wordsIndex)
                    continue
                else:
                    playGame = False
                    break


if __name__ == '__main__':
    main()




