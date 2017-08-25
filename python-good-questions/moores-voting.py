"""
Design an algorithm to find all elements that appear more than n/2 times in the list. Then do it for elements that appear more than n/4 times.
I/P : 3 3 4 2 4 4 2 4 4
O/P : 4

This could also be done in a much simpler way using hash maps, in Python there's collections.Counter which takes care of this problem automatically.
"""


def mooresVoting(nums):
	"""
	:type nums: list of Int
	:rtype: list of Int
	"""
	candidate = nums[0]
	maxi = len(nums)//2
	res = []
	count = 1

	for i in range(1, len(nums)):
		if candidate == nums[i]:
			count += 1
		else:
			count -= 1

		if count == 0:
			candidate = nums[i]
			count = 1
	
	count = 0
	for item in nums:
		if item == candidate:
			count += 1	

	return candidate if count > maxi else -1


def main():
	nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]

	print mooresVoting(nums)

if __name__ == '__main__':
	main()