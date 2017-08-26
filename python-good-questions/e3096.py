"""
All these is to practice questions for Bloomberg suggested on Glassdoord.com. I went on and had a final onsite interview, but did not receive an offer. Also some ideas for why Bloomberg:
http://thegatewayonline.com/technology/internships/bloomberg-technology-at-bloomberg-internship-opportunities
https://www.techatbloomberg.com/post-topic/open-source/
https://github.com/bloomberg
"""

# - Reverse an integer:
# eg: 3421 --> 1243
def reverse_int(x):
	isNegative = False

	if (x < 0): isNegative = True

	x = str(abs(x))[::-1]

	if (abs(int(x)) > 0x7FFFFFFF): return 0
	elif isNegative: return -int(x)
	else: return int(x)

#print reverse_int(12340)
#print reverse_int(-123456789)


# - Given a set of arbitrary float numbers in an SQL table and select only the ones that are exactly 4 decimal places
# SELECT * FROM `test` WHERE LENGTH(SUBSTR(`salary`,INSTR(`salary`,"."))) = 5


# - Remove arbitrary spaces from a sentence:
# eg: "The sky is blue " --> "The sky is blue"
def remove_space(line):
	arr = line.split()
	endWithPeriod = False

	if (arr[len(arr)-1] == '.'):
		arr.pop()
		endWithPeriod = True

	if endWithPeriod:
		temp = ' '.join(arr)
		temp += '.'
		return temp
	else:
		return ' '.join(arr)

#print remove_space('The sky  is blue. ')
#print remove_space('Here is  some   text   I      wrote   .')


# - Return the maximum product of 3 numbers in an array
# https://www.glassdoor.co.uk/Interview/1-return-the-maximum-product-of-3-numbers-in-an-array-2-print-out-the-pairs-of-a-number-and-the-nearest-greater-number-t-QTN_2027094.htm
def max_product(arr):
	arr.sort()
	arr = arr[::-1]

	return arr[0]*arr[1]*arr[2]

#print max_product([5,3,4,-17,0,8,1])



# - Print out the pairs of a number and the nearest greater number to its right in an array. Example: given [1,2,5,2,6], print out (1,2), (2,5), (5,6), (2,6)
def nearest_greater(arr):
    for p in range(len(arr)):
        if (p+1 < len(arr)):
            for q in range(p+1, len(arr)):
                if (arr[q] > arr[p]):
                    break
            print '(' + str(arr[p]) + ', ' + str(arr[q])  + ')'

#print nearest_greater([1,2,5,2,6,7,90,1,8,0,3,99])



# - Given a string "AABCCC" make a new string "2A1B3C"
# https://www.glassdoor.com/Interview/Given-a-string-AABCCC-make-a-new-string-2A1B3C-QTN_1997939.htm
def count_char(line):
	newline = list(line)
	unique_elem = []

	for index in newline:
		if index not in unique_elem:
			unique_elem.append(index)

	i = 0
	temp = {}

	for p in unique_elem:
		temp[p] = i
		for q in newline:
			if p == q:
				temp[p] += 1

	new_arr = ''
	for item in unique_elem:
		new_arr += str(temp[item]) + item
	return new_arr

#print count_char('AABCCCA')


# - You are given a vector of integers. You have to delete the odd numbers from it. Expected complexity is O(N) Time and O(1) space
def delete_odd(arr):
	new_arr = []

	for item in arr:
		if (item%2 == 0):
			new_arr.append(item)

	return new_arr

#print delete_odd([1,2,5,2,6,7,-90,1,8,0,3,99])



# - Time and space complexity
# https://stackoverflow.com/questions/2219109/what-does-this-mean-on-steps-and-o1-space
# O(1) space means that the memory required by the algorithm is constant, i.e. does not depend on the size of the input.
# O(n) space means that the memory required by the algorithm has (in the worst case) the same order of magnitude as the size of the input.
# Bubblesort requires O(1) space.
# Mergesort requires O(n) space.



# - Write a piece of code to find the square root of a number.
# Algorithm used: https://en.wikipedia.org/wiki/Newton%27s_method#Square_root_of_a_number
def find_sqrt(num):
	precision = 0.005

	if ((num == 0) or (num == 1)):
		return num
	elif (num < 0):
		return 'Invalid'

	guess = num
	while guess*guess > num:
		guess = (guess + num/guess) / 2.0

	return guess

#print find_sqrt(2)



# - Given an array of integers sorted in ascending order, find the starting and ending position of a given target value. Complexity O(log n). If the target is not found in the array, return [-1, -1].
# i.e. Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].
# https://leetcode.com/problems/search-for-a-range/#/description
def search_range(arr, val):
	# if ((arr[0] > val) or (arr[-1] < val)):
	# 	return [-1, -1]

	lo = binary_search(arr, val) # Find Lowest Boundary

	if val in arr[lo:lo+1]:
		hi = binary_search(arr, val+1) 
	else:
		return [-1, -1]

	return [lo, hi-1]


def binary_search(arr, val):
	first, last = 0, len(arr)

	while (first < last):
		mid = (first + last)/2
		if (arr[mid] >= val):
			last = mid
		else:
			first = mid + 1
	return first

#print search_range([2, 5, 7, 7, 8, 8, 8, 10], 8)
#print search_range([4, 5, 8, 8, 8, 8, 9, 9, 10], 8)
#print search_range([5, 7, 7, 8, 8, 10], 15)


# - Find the pairs from a given array, whose sum is equal to the target sum.
def find_pair(arr, num):
	for item in arr:
		potential = num - item
		if (potential > 0) and (potential in arr):
			return (item, potential)

#print find_pair([1,2,3,4,5,6,7,8,10,9], 7)


# - Decide whether there are duplicates in an array.
# Covert to a set and check length, compare to original



# - Given an input string and a number n, return all the characters that are repeated at least n times in the input string
def repeated_chars(line, n):
	newline = list(line)
	
	while (' ' in newline):
		newline.remove(' ')

	unique_elem = set(newline)
	chars = {}

	for p in unique_elem:
		chars[p] = 0
		for q in newline:
			if p == q:
				chars[p] += 1


	for k, v in chars.iteritems():
		if v >= n:
			yield k, v

#print [x for x in repeated_chars('Time is money', 2)]



# - Valid Parentheses
# https://www.glassdoor.com/Interview/Bloomberg-L-P-Interview-RVW14143101.htm
# https://leetcode.com/problems/valid-parentheses/#/description
def is_valid(s):
	map = {')':'(', '}':'{', ']':'['}
	stack = []
	isValid = False

	if (len(s)%2 != 0):
		return False

	for char in s:
		if char in map.values():
			stack.append(char)
		elif char in map.keys():
			if (stack == []): return False
			elif (stack[-1] == map[char]): 
				stack.pop()
				isValid = True
			else: isValid = False

	if (stack != []): return False
	return isValid

#print is_valid('{{[()]}}()[]')
#print is_valid('()[]{})')
#print is_valid('([)]')
#print is_valid('{{)}')



# - Given two integer arrays A and B, where A is larger in size than B, find the intersection of the two arrays, i.e. the elements that are present in both A and B.
# https://www.glassdoor.com/Interview/Bloomberg-L-P-Interview-RVW14322068.htm
def find_intersect(a, b):
	a = set(a)
	b = set(b)
	return list(a&b)

#print find_intersect([1, 1, 7, 7, 8, 9], [1, 2])



# - Given an unordered list of tasks, where a task is a class that has an id and a parent id, implement a function called killBranch. killBranch would be passed the task id that is to be killed and the unordered list. The function should kill all the children tasks of the parent task needed to be killed and return the updated list. (No brute force solution, or topological sort)

# - Given a set, return the power set.
# Power set of a set A is the set of all of the subsets of A.


# https://www.glassdoor.com/Interview/Bloomberg-L-P-Interview-RVW13471308.htm
# a Find longest substring with unique characters in O(n) time.
# b Find all nodes matching a given value in a Tree.

# https://www.glassdoor.com/Interview/Bloomberg-L-P-Interview-RVW14491043.htm
# Tech question1 : Linkedlist cycle. Find if there is a cycle in one linkedlist.
# Tech question2 : Find the intersection of two integer arrays.

# Coding question: given a array and a number k, find a contiguous longest subarray having sum <=k.


# Given 11000111, output how far each 0 is from the current index. So output should be 21000123
def distance_to_zero(s):
	arr = list(s)

	zero_pos = []

	for i in range(0, len(arr), 1):
		if (arr[i] == '0'):
			zero_pos.append(i)

	for i in range(0, len(arr), 1):
		if (arr[i] != '0'):
			temp = len(arr)

			for item in zero_pos:
				if (abs(i-item) < temp):
					temp = abs(i-item)
				# print i, temp, item
			arr[i] = str(temp)

	return ''.join(arr)

#print distance_to_zero('11000111')



def removeDuplicates(nums):
	nums = list(set(nums))
	return len(nums)

#print removeDuplicates([1,1,2])
