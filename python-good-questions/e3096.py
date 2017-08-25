# Why Bloomberg:
# http://thegatewayonline.com/technology/internships/bloomberg-technology-at-bloomberg-internship-opportunities
# https://www.techatbloomberg.com/post-topic/open-source/
# https://github.com/bloomberg
# https://www.techatbloomberg.com/blog/bloomberg-ctos-vision-ideal-engineer-engineering-students-study-not-math-also-literature/
# https://www.techatbloomberg.com/blog/bringing-interactivity-data-bqplot/
# https://gaishishukatsu.com/archives/98777

# Algorithm Reads
# https://www.quora.com/How-should-I-prepare-for-a-software-developer-internship-interview-at-Bloomberg
# https://en.wikipedia.org/wiki/Big_O_notation

# Data Structure Reads
# Priority Queue: https://en.wikipedia.org/wiki/Priority_queue
# Heap: https://en.wikipedia.org/wiki/Heap_(data_structure)


# https://www.glassdoor.co.uk/Interview/Bloomberg-L-P-Interview-Questions-E3096.htm

# - Reverse an integer:
# eg: 3421 --> 1243
def reverseInt(num):
	isNegative = False

	if (num < 0):
		isNegative = True

	numStr = str(abs(num))

	numStr = list(numStr)

	reversedNum = ''.join(numStr[::-1])

	if isNegative:
		print - int(reversedNum)
	else:
		print int(reversedNum)

def reverseInt2(x):
	isNegative = False

	if (x < 0): isNegative = True

	x = str(abs(x))[::-1]

	if (abs(int(x)) > 0x7FFFFFFF): return 0
	elif isNegative: return -int(x)
	else: return int(x)

# reverseInt(12340)
# reverseInt(-123456789)


# - Given a set of arbitrary float numbers in an SQL table and select only the ones that are exactly 4 decimal places
# SELECT * FROM `test` WHERE LENGTH(SUBSTR(`salary`,INSTR(`salary`,"."))) = 5

# - Remove arbitrary spaces from a sentence:
# eg: "The sky is blue " --> "The sky is blue"
def removeSpace(line):
	arr = line.split()
	endWithPeriod = False

	if (arr[len(arr)-1] == '.'):
		arr.pop()
		endWithPeriod = True

	if endWithPeriod:
		temp = ' '.join(arr)
		temp += '.'
		print temp
	else:
		print ' '.join(arr)

# removeSpace('The sky  is blue. ')
# removeSpace('Here is  some   text   I      wrote   .')


# https://www.glassdoor.co.uk/Interview/1-return-the-maximum-product-of-3-numbers-in-an-array-2-print-out-the-pairs-of-a-number-and-the-nearest-greater-number-t-QTN_2027094.htm

# - Return the maximum product of 3 numbers in an array
def maxProduct(arr):
	arr.sort()

	# if (arr[0] < 0) and (arr[1] < 0):
	arr = arr[::-1]

	print arr[0]*arr[1]*arr[2]

# maxProduct([5,3,4,-17,0,8,1])


# - Print out the pairs of a number and the nearest greater number to its right in an array. Example: given [1,2,5,2,6], print out (1,2), (2,5), (5,6), (2,6)
def nearestGreater(arr):
	for p in range(0, len(arr), 1):
		if (p+1 < len(arr)):
			for q in range(p+1, len(arr), 1):
				if (arr[q] > arr[p]):
					break
			print '(' + str(arr[p]) + ', ' + str(arr[q])  + ')'

# nearestGreater([1,2,5,2,6,7,90,1,8,0,3,99])


# https://www.glassdoor.com/Interview/Given-a-string-AABCCC-make-a-new-string-2A1B3C-QTN_1997939.htm
# - Given a string "AABCCC" make a new string "2A1B3C"
def countChar(line):
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
	print new_arr

# countChar('AABCCCA')


# - You are given a vector of integers. You have to delete the odd numbers from it. Expected complexity is O(N) Time and O(1) space
def deleteOdd(arr):

	new_arr = []

	for item in arr:
		if (item%2 == 0):
			new_arr.append(item)

	print new_arr

# deleteOdd([1,2,5,2,6,7,-90,1,8,0,3,99])

# O(1) space means that the memory required by the algorithm is constant, i.e. does not depend on the size of the input.

# O(n) space means that the memory required by the algorithm has (in the worst case) the same order of magnitude as the size of the input.

# Edit: Adding two examples:

#     Bubblesort requires O(1) space.
#     Mergesort requires O(n) space.
# https://stackoverflow.com/questions/2219109/what-does-this-mean-on-steps-and-o1-space



# - Write a piece of code to find the square root of a number.
# https://en.wikipedia.org/wiki/Newton%27s_method#Square_root_of_a_number
def findSqrt(num):
	precision = 0.005

	if ((num == 0) or (num == 1)):
		print num
	elif (num < 0):
		print 'Invalid'

	guess = num
	while guess*guess > num:
		guess = (guess + num/guess) / 2.0

	print guess

findSqrt(2)



# - Given an array of integers sorted in ascending order, find the starting and ending position of a given target value. Complexity O(log n). If the target is not found in the array, return [-1, -1].
# i.e. Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].
# https://leetcode.com/problems/search-for-a-range/#/description
def searchRange(arr, val):
	# if ((arr[0] > val) or (arr[-1] < val)):
	# 	return [-1, -1]

	lo = binarySearch(arr, val) # Find Lowest Boundary

	if val in arr[lo:lo+1]:
		hi = binarySearch(arr, val+1) 
	else:
		return [-1, -1]

	return [lo, hi-1]


def binarySearch(arr, val):
	first, last = 0, len(arr)

	while (first < last):
		mid = (first + last)/2
		if (arr[mid] >= val):
			last = mid
		else:
			first = mid + 1
	# print first
	return first

# print searchRange([2, 5, 7, 7, 8, 8, 8, 10], 8)
# print searchRange([4, 5, 8, 8, 8, 8, 9, 9, 10], 8)
# print searchRange([5, 7, 7, 8, 8, 10], 15)


# - Find the pairs from a given array, whose sum is equal to the target sum.
def findPair(arr, num):
	for item in arr:
		potential = num - item
		if (potential > 0) and (potential in arr):
			print (item, potential)

# findPair([1,2,3,4,5,6,7,8,10,9], 7)


# - Decide whether there are duplicates in an array.
# Covert to a set and check length, compare to original

# - Deal with a stream of pairs and whether one can get to certain point

# - Check if a tree is a BST
# Inorder Traversal
# def inorder(tree):
#   if tree != None:
#       inorder(tree.getLeftChild())
#       print(tree.getRootVal())
#       inorder(tree.getRightChild())
# Use list as a stack, use append() to add and pop() to retrieve. Check every item to see if it is getting smaller.

# - Given an input string and a number n, return all the characters that are repeated at least n times in the input string
import sys

def repeatedChars(line, n):
	# print sys.argv
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
			print k, v

# repeatedChars('Time is money', 2)


# https://www.glassdoor.com/Interview/Bloomberg-L-P-Interview-RVW14143101.htm
# - Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/#/description
def isValid(s):
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
	
	# return False
	# print stack
	return isValid

# print isValid('{{[()]}}()[]')
# print isValid('()[]{})')
# print isValid('([)]')
# print isValid('{{)}')

# https://www.glassdoor.com/Interview/Bloomberg-L-P-Interview-RVW14322068.htm
# - 1 Given two integer arrays A and B, where A is larger in size than B, find the intersection of the two arrays, i.e. the elements that are present in both A and B.
def findIntersect(a, b):
	a = set(a)
	b = set(b)
	print list(a&b)

# findIntersect([1, 1, 7, 7, 8, 9], [1, 2])

# - 2 Given an unordered list of tasks, where a task is a class that has an id and a parent id, implement a function called killBranch. killBranch would be passed the task id that is to be killed and the unordered list. The function should kill all the children tasks of the parent task needed to be killed and return the updated list. (No brute force solution, or topological sort)

# - 3 Given a set, return the power set.
# Power set of a set A is the set of all of the subsets of A.


# https://www.glassdoor.com/Interview/Bloomberg-L-P-Interview-RVW13471308.htm
# a Find longest substring with unique characters in O(n) time.
# b Find all nodes matching a given value in a Tree.

# https://www.glassdoor.com/Interview/Bloomberg-L-P-Interview-RVW14491043.htm
# Tech question1 : Linkedlist cycle. Find if there is a cycle in one linkedlist.
# Tech question2 : Find the intersection of two integer arrays.

# Coding question: given a array and a number k, find a contiguous longest subarray having sum <=k.
# def findSubArray(arr, k):

# Given 11000111, output how far each 0 is from the current index. So output should be 21000123
def distanceToZero(s):
	arr = list(s)

	# print arr

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

	print ''.join(arr)
	print arr

# distanceToZero('11000111')

def removeDuplicates(nums):
	nums = list(set(nums))

	print nums

	return len(nums)

# removeDuplicates([1,1,2])

INT_MAX = 4294967296
INT_MIN = -4294967296

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTUtil(root, INT_MIN, INT_MAX)
        
    def isValidBSTUtil(self, root, min, max):
        if not root: return True
        if root.val <= min or root.val >= max: return False
        return self.isValidBSTUtil(root.left, min, root.val) and self.isValidBSTUtil(root.right, root.val, max)


def height(root):
    if not root: return -1
    
    return 1 + max(height(root.left), height(root.right))

def inOrder(root):
    #Write your code here
    if root.left: inOrder(root.left)
    print root.data,
    if root.right: inOrder(root.right)

arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)




























