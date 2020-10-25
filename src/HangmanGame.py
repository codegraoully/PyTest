import math
import os
import random
import re


def clear():
    os.system("clear")


wordList = {1: "renégat",
            2: "duel",
            3: "fantastique",
            4: "truc"}

helpWordList = {1: "traître",
                2: "combat",
                3: "science fiction",
                4: "machin"}

vowel = ["a", "e", "i", "o", "u", "y"]

consonant = ["b", "c", "d", "f", "g", "h",
             "j", "k", "l", "m", "n", "p",
             "q", "r", "s", "t", "v", "w", "x", "z"]

score = 0
attempt = 0

print("--- Hangman Game ---")

# Find a random word in the collection
randomNumber = math.trunc(random.random() * 10)

while randomNumber > 4 or randomNumber < 1:
    randomNumber = math.trunc(random.random() * 10)

wordToFind = wordList.get(randomNumber)

# Init user word
userWord = []
i = 0
while i < len(wordToFind):
    userWord.append("-")
    i += 1

# Main game
win = False
while not win:
    clear()
    clear()
    print("---------------------------------------")
    print(userWord)
    print("---------------------------------------")
    print(vowel)
    print(consonant)
    print("---------------------------------------")
    userLetter = input("Choose an available letter: ")

    # Remove the letter in the possibilities
    try:
        posVowel = vowel.index(userLetter)
        vowel.pop(posVowel)
    except ValueError:
        Exception
    try:
        posConsonant = consonant.index(userLetter)
        consonant.pop(posConsonant)
    except ValueError:
        Exception

    # Find the letter in the word
    pattern = re.compile(userLetter)
    matchs = re.finditer(pattern, wordToFind)
    if matchs:
        for match in matchs:
            print("pos:", match.start())
            userWord[match.start()] = userLetter

        print("Good, continue.")
        score += 1
    else:
        print("ok")
        print("Not in this word ! Try again.")

    attempt += 1
    print("Your score: ", score, "/", attempt)

    if "".join(userWord) == wordToFind:
        win = True

if win:
    print("Congratulation ! With ", score, "/", attempt)
