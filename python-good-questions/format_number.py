def formatNum(num):
	num_negative = False
	
	if (num < 0):
		num_negative = True

	str_num = str(abs(num))
	str_len = len(str_num)

	str_num = list(str_num)

	str_num = str_num[::-1]

	index = 0
	temp = []


	for index in xrange(str_len):
		temp.append(str_num[index])
		if (index%3 == 2):
			temp.append(',')

	
	if num_negative:
		temp.append('-')

	print ''.join(temp[::-1])



formatNum(1234)
formatNum(-12312315678)