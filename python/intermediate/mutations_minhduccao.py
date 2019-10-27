# Assumes list only contains 2 string elements
def mutations(sList):
    mainWord = sList[0].lower()         # Set words to lowercase to ignore lettercase
    checkWord = sList[1].lower()
    mainLetters = set(mainWord)         # Used sets to separate words into letters
    checkLetters = set(checkWord)       # because repetition isn't checked

    for x in checkLetters:              # Checks through each letter to see if it's in the main word
        if x not in mainLetters:
            return False                # Returns False if letter isn't in, no need to continue for loop if not found
    return True
