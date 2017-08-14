# Power of 10

def power_of_10(n):
	while n > 1:
		if n%10 != 0:
			return False
		n /= 10

	return True

if __name__ == '__main__':
	print power_of_10(70)
	print power_of_10(10000)
	print power_of_10(10001)
	print power_of_10(1)
	print power_of_10(90)