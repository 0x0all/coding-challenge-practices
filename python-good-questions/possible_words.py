# Print all possible words from phone digits
# Very similar to http://www.geeksforgeeks.org/find-possible-words-phone-digits/
# 2, 2, 3 => ace, abe, bad


dict = {2: 'abc', 3: 'def', 4: 'ghi', 5:'jkl', 6:'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
   
def possible_english_words(nums):
    if not nums:
        return []
        
    elif len(nums) <= 1:
        return [x for x in list(dict[nums[0]])]
    else: 
        temp = possible_english_words(nums[:-1])
        temp2 = dict[nums[-1]]
        return [x + y for x in temp for y in temp2]


if __name__ == '__main__':
    print possible_english_words([2])
    print possible_english_words([2,2,3])
