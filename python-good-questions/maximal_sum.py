"""
https://stackoverflow.com/questions/29236837/find-max-sum-of-elements-in-an-array-with-twist
Given a array with +ve and -ve integer , find the maximum sum such that you are not allowed to skip 2 contiguous elements ( i.e you have to select at least one of them to move forward).
eg :-
10 , 20 , 30, -10 , -50 , 40 , -50, -1, -3
Output : 10+20+30-10+40-1 = 89

This is very similar to an interview question I've had, and it actually got me thinking whether I should continue a career in software engineering. At the time of the interview, I had zero idea of dynamic programming or anything similar to that and in fact, this problem got me upset for days, and searching online for a similar problem so I can understand it better and find a solution. Even to this day I still think I need to practice dynamic programming problems a lot more. The idea of the solution is to use Dynamic Programming, and iterate the array arr backwards, each time storing the answer maximal[i]. Since we cannot skip 2 contiguous elements, either element i+1 or element i+2 has to be included in maximal[i].
"""
def maximal(arr):
	maximal = [0]*len(arr)

	for i in range(0, len(arr)):
		maximal[i] = arr[i] + max(maximal[i-1], maximal[i-2])

	return max(maximal[-1], maximal[-2])



def main():
	arr = [10 , 20 , 30, -10 , -50 , 40 , -50, -1, -3]
	# arr = [-1, -2, -3, -4, -5]
	print maximal(arr)

if __name__ == '__main__':
	main()