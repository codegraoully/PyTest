import os

charToReplace = {'[', ']', '\'', '(', ')'}
charReplacing = '_'

for filename in os.listdir('.'):

    if filename == "." or ".." or os.path.isdir(filename):
        break

    newFilename = filename.lower().replace(' ', '_')

    for char in charToReplace:
        if filename.find(char) > -1:
            newFilename = newFilename.replace(char, charReplacing)

    print(filename, ' -> ', newFilename)
    # os.rename(filename, newFilename)
