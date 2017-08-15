from math import log

def pow_of_four(n):
	if n==0:
		return 0

	while n!=0:
		if n%4 != 0:
			return 0
		n /= 4

	return 1


def pow_of_four_2(n):
	"""
	https://discuss.leetcode.com/topic/43151/share-my-c-solution-with-explanation-easy-to-understand
	num must be positive
	num must be power of 2
	num mod 3 must be 1
	"""
	if n <= 0:
		return False
	if n&n-1:
		return False
	return n%3 == 1

     
def pow_of_four_3(n):
	res = log(n, 4)
	return (res).is_integer()


def main():
	print pow_of_four_3(8)


if __name__ == '__main__':
	main()