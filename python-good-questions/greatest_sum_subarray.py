"""
The problem is to find the subarray of an array/list with the greatest sum. Almost exactly the same to this problem: https://stackoverflow.com/questions/21690771/finding-contiguous-subset-with-largest-sum. At the beginning I made the mistake of finding the greatest sum instead, but it is actually to find a subset of the list. And one thing to remember is that when the sum is negative, we should return 0.
Example:
Input: [4, -1, 5, 6, -13, 2]
Output: [4, -1, 5, 6]
Input: [-1,-2,-3,-4,-5]
Output: []
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: [4, −1, 2, 1]
I think the trick to solve this problem is to actually solve it manually first, then you'll realize you need two pointers to track start and end, then the solution becomes clearer.
"""

def greatest_subarray(nums):
	if not nums:
		return []

	curr_sum = max_sum = 0
	start, end = 0, -1
	for index in range(len(nums)):
		curr_sum += nums[index]
		if curr_sum < 0:
			start = index + 1
			curr_sum = 0
		elif curr_sum > max_sum:
			end = index
			max_sum = curr_sum

	return nums[start:end+1]

if __name__ == '__main__':
	print greatest_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
	print greatest_subarray([-1,-2,-3,-4,-5])
	print greatest_subarray([4, -1, 5, 6, -13, 2])

