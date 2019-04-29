#!/usr/bin/python3.7
import os
from datetime import datetime
from random import random


def printScore():
    print("Ton score: %s sur %s" % (scoreUser, scoreTotal))


def saveResult():
    file = open("us er'.txt", "a")
    file.write("%s|%s|score:%s/%s\n" % (datetime.today().strftime("%d-%m-%Y %H:%M"), userName, scoreUser, scoreTotal))
    file.close()


def clear():
    os.system('clear')


clear()
userName = ""
userResult = 0
scoreUser = 0
scoreTotal = 0
quit = "q"

print("--------------------------------------")
userName = input("Quel est ton nom? ")

while userResult != quit:

    # because we can come here from inside the while
    if userResult == quit:
        break

    leftNum = 0
    while leftNum < 2:
        leftNum = int(random() * 10)

    rightNum = 0
    while rightNum < 2:
        rightNum = int(random() * 10)

    result = leftNum * rightNum

    retry = True
    while retry:
        try:
            userResult = input("%1s X %1s = " % (str(leftNum), str(rightNum)))

            if userResult == quit:
                break
            else:
                userResult = int(userResult)

            retry = False

            scoreTotal += 1

            if int(userResult) == result:
                scoreUser += 1
                print("Ton score: %s sur %s %25s" % (scoreUser, scoreTotal, "Bien !"))
            else:
                print("%30s" % "Ouille Aïe !")
                retry = True

        except Exception as e:
            retry = True

printScore()
saveResult()

print("--------------------------------------")
print("Bye bye !")
