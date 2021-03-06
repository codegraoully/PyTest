import math
import os
import random
import re
import csv

def clear():
    os.system("clear")

# Lecture du dictionnaire utilisateur
wordList = []
numberOfWord = 0
with open('/home/michel/Documents/Projects/Python/src/dictionnaire.txt', newline='') as csvFile:
    line = csv.reader(csvFile, delimiter='|')
    for row in line:
        wordList.append(row)
        numberOfWord =+ 1

vowel = ["a", "e", "i", "o", "u", "y"]

consonant = ["b", "c", "d", "f", "g", "h",
             "j", "k", "l", "m", "n", "p",
             "q", "r", "s", "t", "v", "w", "x", "z"]

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
attempt = 0
win = False
clear()
while not win:
    print("---------------------------------------")
    print('help: ', wordToFindHelper)
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
    for letter in wordToFind:
        if userLetter == letter:
            print('Good job.')
            pos = wordToFind.index(letter)
            userWord[pos] = letter
            break

    attempt += 1
    print("Attempt: ", attempt)

    if "".join(userWord) == wordToFind:
        win = True

print("Congratulation ! With ", attempt, "try on ", len(wordToFind), " letters.")
