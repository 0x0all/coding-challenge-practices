# Given N integers, count the number of pairs of integers whose difference is K.
# Input Format: The first line contains N and K. All the N numbers are unique.
# Output Format: An integer that tells the number of pairs of integers whose difference is K.

def couting_pairs(nums, k):
	sorted(nums)

	count, start_pos, curr_pos = 0, 0, 0

	while curr_pos < len(nums):
		curr_pos = start_pos + 1
		while curr_pos < len(nums):
			diff = abs(nums[curr_pos] - nums[start_pos])
			if diff == k:
				count += 1
			elif diff > k:
				break
			curr_pos += 1
		start_pos += 1
	
	return count

if __name__ == '__main__':
	print couting_pairs([2,3,5,7,8], 1)