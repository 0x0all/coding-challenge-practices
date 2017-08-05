"""
The Problem:
Write a function that takes a list of numbers as strings as input and outputs the biggest number formed with those strings. Example:
Input: ['32', '54', '78', '829']
Output: 829785432

During the interview I actually did the all_combination() version, but then long afterwards with the help of this post (http://blog.gainlo.co/index.php/2017/01/20/arrange-given-numbers-to-form-the-biggest-number-possible/), I realized for this problem I don't need to get all the combinations, all I need to is rearrange the numbers from largest to smallest! So I added sort_then_sum() that returns the same answer but much simpler. Sometimes the intuitive way works the best!
"""

# Solution 1
def all_combination(str):
    if len(str) <=1:
        yield str
    else:
        for temp in all_combination(str[1:]):
            for i in range(len(temp)+1):
                yield temp[:i] + str[0:1] + temp[i:]

# Solution 2
def sort_then_sum(str):
    nums = sorted(str, reverse=True)
    return ''.join(nums)
	


if __name__ == '__main__':
    res = [''.join(x) for x in all_combination(['32', '54', '78', '829'])]
    print sorted(res)[-1]

    print sort_then_sum(['32', '54', '78', '829'])