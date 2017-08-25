def findLongest(item, words, word_dict):
    if item not in word_dict: 
        word_dict[item] = 1
    
    for i in range(len(item)):
        temp = item[:i] + item[i+1:]
        
        if temp not in words:
            continue
            
        if temp not in word_dict:
            findLongest(temp, words, word_dict)
            
        word_dict[item] = max(word_dict[temp]+1, word_dict[item])

def  longestChain(words):
    if not words: return 0
    
    word_dict = {}

    words = set(words)
    
    for item in words:
        findLongest(item, words, word_dict)
    
    return max(word_dict.values())
        
            

