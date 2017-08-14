# Problem Name is &&& Pangram
"""
 Pangram Detector

 The sentence "The quick brown fox jumps over the lazy dog" contains
 every single letter in the alphabet. Such sentences are called pangrams.

 Write a function findMissingLetters, which takes a string `sentence`,
 and returns all the letters it is missing (which prevent it from
 being a pangram). You should ignore the case of the letters in sentence,
 and your return should be all lower case letters, in alphabetical order.
 You should also ignore all non US-ASCII characters.
"""
import string
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def FindMissingLetters(sentence):
    s = list(sentence.strip(string.punctuation).lower())
    s = [ x for x in s if x != ' ' ]  # remove white spaces
    # res = []
    # for char in ALPHABET:
    #     if char not in s:
    #         res.append(char)
    # return ''.join(res)
    return ''.join(sorted(list(set(ALPHABET) - set(s))))

# Test Cases
def runTests():
    success = (
        '' == FindMissingLetters("The quick brown fox jumps over the lazy dog") and
        'bfgjkvz' == FindMissingLetters("The slow purple oryx meanders past the quiescent canine") and
        'cdfjklmopqruvxyz' == FindMissingLetters("We hates Bagginses!") and
        'abcdefghijklmnopqrstuvwxyz' == FindMissingLetters("")
    )

    return success

if __name__ == "__main__":
    if runTests():
        print("All tests passed")
    else:
        print("At least one test failed.")
    # print FindMissingLetters("The slow purple oryx meanders past the quiescent canine")