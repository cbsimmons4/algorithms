# Given an arbitrary ransom note string and another string
# containing letters from all the magazines, write a
# function that will return if the ransom note can be constructed 
# from the magazines; otherwise, it will return False

# Each letter in the magazine can be used in your ransom note 

def canConstruct (note, magCollection):
    availableLetters = {}
    for letter in magCollection:
        if letter in availableLetters.keys(): 
            availableLetters[letter] += 1
        else:  availableLetters[letter] = 1 
    for letter in note:
        if (letter in availableLetters.keys()) and (availableLetters[letter] > 0):
            availableLetters[letter] -= 1
        else: return False
    return True 


print(canConstruct('ccadac', 'acabccdcc'))
