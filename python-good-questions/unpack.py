"""
The problem is to convert a multidimensional list/array to single dimension.
Example:
Input: [1,[2,[3]], [4,5], [[[6]]]]
Output: [1,2,3,4,5,6]
"""
arr = [1,[2,[3]], [4,5], [[[6]]]]

def unpack_arr(nums):
	res = []

	def unpack(nums):
		for i in nums:
			if isinstance(i, list):
				unpack(i)
			else:
				res.append(i)
	unpack(nums)
	return res

if __name__ == '__main__':
	print unpack_arr(arr)