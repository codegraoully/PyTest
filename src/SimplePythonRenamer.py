import os

charToReplace = {'[', ']', '\'', '(', ')'}
charReplacing = '-'

for filename in os.listdir('.'):

    if filename == ".":
        break
    if filename == "..":
        break

    if os.path.isdir(filename):
        break

    newFilename = filename.lower().replace(' ', '_')

    for char in charToReplace:
        if filename.find(char) > -1:
            newFilename = newFilename.replace(char, charReplacing)

    print(filename, ' -> ', newFilename)
    # os.rename(filename, newFilename)
