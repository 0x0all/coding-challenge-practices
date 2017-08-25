# http://blog.gainlo.co/index.php/2017/01/12/rotated-array-binary-search/
# The problem is to search for an element in a sorted and rotated list and return the index of the element, else return -1. It is very apparent we need to use binary search and recursion to solve this problem. And I believe I have encountered the same problem twice in different interviews.

def search(target, nums):
	left, right = 0, len(nums) -1
	while left <= right:
		mid = (left+right)//2
		if nums[mid] ==  target: return mid
		
		if nums[left] <= nums[mid]:
			if nums[left] <= target <= nums[mid]:
				right = mid - 1
			else:
				left = mid + 1
		
		else:
			if nums[mid] <= target <= nums[right]:
				left = mid + 1
			else:
				right = mid - 1

	return -1


	
	
if __name__ == '__main__':
	print search(3, [5, 6, 7, 8, 9, 10, 1, 2, 3])