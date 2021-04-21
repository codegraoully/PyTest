import math
import os
import random
import re
import csv


def clear():
    os.system("clear")

wordList = []
numberOfWord = 0
with open('/home/michel/Documents/Projects/Python/src/dictionnaire.txt', newline='') as csvFile:
    line = csv.reader(csvFile, delimiter='|')
    for row in line:
        wordList.append(row)
        numberOfWord =+ 1

print(wordList)
# quit()

# wordList = {1: "renégat",
#             2: "duel",
#             3: "fantastique",
#             4: "truc"}

# helpWordList = {1: "traître",
#                 2: "combat",
#                 3: "science fiction",
#                 4: "machin"}

vowel = ["a", "e", "i", "o", "u", "y"]

consonant = ["b", "c", "d", "f", "g", "h",
             "j", "k", "l", "m", "n", "p",
             "q", "r", "s", "t", "v", "w", "x", "z"]

<<<<<<< HEAD
score = 0
attempt = 0

print("--- Hangman Game ---")

=======
>>>>>>> 9b41bb2 (Utilisation d'un dictionnaire)
# Find a random word in the collection
randomNumber = math.trunc(random.random() * 10)

while randomNumber > numberOfWord or randomNumber < 1:
    randomNumber = math.trunc(random.random() * 10)

wordToFind = wordList[randomNumber][0]
wordToFindHelper = wordList[randomNumber][1]

# Init user word
userWord = []
i = 0
while i < len(wordToFind):
    userWord.append("-")
    i += 1

# Main game
print("--- Hangman Game ---")
score = 0
attempt = 0
win = False
clear()
while not win:
<<<<<<< HEAD
    clear()
    clear()
=======
    print("---------------------------------------")
    print('help: ', wordToFindHelper)
>>>>>>> 9b41bb2 (Utilisation d'un dictionnaire)
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
    print("Your score: ", attempt)

    if "".join(userWord) == wordToFind:
        win = True

if win:
    print("Congratulation ! With ", attempt, "try.")
