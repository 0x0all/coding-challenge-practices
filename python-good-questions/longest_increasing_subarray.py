# http://blog.gainlo.co/index.php/2017/02/02/uber-interview-questions-longest-increasing-subarray/

def longest_increasing_subarray(nums):
	length = 0
	current_length = 0
	prev = 0

	for i in range(len(nums)):
		if nums[i] < prev:
			prev = nums[i]
			length = current_length
			current_length = 1

		else:
			current_length += 1
			prev = nums[i]

	return max(current_length, length)

if __name__ == '__main__':
	print longest_increasing_subarray([1, 3, 2, 3, 4, 8, 7, 9])