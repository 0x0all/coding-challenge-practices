# Random Weight
# Write a custom data structure and implement two functions put(String, Int) and get(): String
# Very similar to http://blog.gainlo.co/index.php/2016/11/11/uber-interview-question-weighted-random-numbers/
# Example:
# Put:
# "a": 1
# "b": 2
# "c": 3
# "a": -10
# Get:
# "b" -> "2 / 5"
# "c" -> 3 / 5

import random
from collections import defaultdict


class RandomWeight(object):

    def __init__(self):
        self.weight = 0
        self.l = []
        self.dict = defaultdict(set)

    
    def put(self, s, num):
        # if num < 0 and s in self.dict:
        #     if num >= len(self.dict[s]):
        #         temp = self.dict[s]
        #         del self.dict[s]
        #     else:
        self.weight += num
        
        self.vals.append(val)
        self.idxs[val].add(len(self.vals) - 1)
        return len(self.l[val]) == 1
                
        for x in range(self.weight, self.weight + num):
            self.dict[s].append(x)
        

        # return self.dict

    
    def get(self):
        num = random.randint(0, self.weight)
        for k in self.dict:
            if num in self.dict[k]:
                return k      
        
        
if __name__ == '__main__':
    test = RandomWeight()
    test.put('a',5)
    test.put('b',1)
    test.put('a',1)
    print test.get()
        
        
        
        
        
        