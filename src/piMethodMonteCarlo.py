from random import *

# Number of hit in a quarter circle

numberOfTry = 1_000_000_000
isInCircle = 0

for i in range(0, numberOfTry):

    x = random()
    y = random()

    if x * x + y * y < 1:
        isInCircle += 1

pi = isInCircle / numberOfTry * 4

print(pi)
