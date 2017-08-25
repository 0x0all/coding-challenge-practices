def friendCircles(friends):
    matrix = [] 
    temp = []
    # Get number of people
    n = len(friends)

    for line in friends:
        matrix.append(list(line))
        
    for p in range(n):
        for q in range(p+1, n):
            if matrix[p][q] == 'Y':
                # Get a unique list of friend pairs as tuples
                temp.append((p,q))
    
    def make_set(x):
        return frozenset([x])
    
    circles = set([make_set(x) for x in range(n)])
    
    #print circles
    def find(x):
        for subset in circles:
            if x in subset:
                return subset
     
    def union(p,q):
        circles.add(frozenset.union(p,q))
        circles.remove(p)
        circles.remove(q)
    #print temp
    
    for (p,q) in temp:
        set_p = find(p)
        set_q = find(q)
        
        if set_p != set_q:
            union(set_p, set_q)
            
    return len(circles)
        