"""
The Problem:
Write a function to reverse the vowels in a given string
Example:
input -> output
"hello elephant" -> "halle elophent"
"abcde" -> "ebcda"
"abc" -> "abc"
"""

def reverse_vowels(s):

    vowels =  'aeiou'
    
    res = list(s)
    
    pos = [index for index, char in enumerate(s) if char in vowels]
    
    reversed_pos = pos[::-1]
    
    for index in range(len(pos)):
    	res[pos[index]] = list(s)[reversed_pos[index]]
    
    return ''.join(res)


if __name__ == '__main__':
    print reverse_vowels("hello elephant")