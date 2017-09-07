# Similar to https://www.hackerrank.com/contests/projecteuler/challenges/euler014

def collatzSum(maxNumber, minLength):
    dict = {} # key, value pair of number and length
    
    def collatz_seq(num):
        count = 1
        temp = num

        while temp != 1:
            if temp in dict:
                dict[num] = dict[temp] + count - 1
                return
            elif temp%2 == 0:
                temp /= 2
            else:
                temp = temp*3 + 1
            count += 1
            
        dict[num] = count
        
    
    for i in range(1, maxNumber+1):
        collatz_seq(i)
    
    return sum(k for k, v in dict.items() if v > minLength)