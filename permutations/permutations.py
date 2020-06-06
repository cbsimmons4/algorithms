#Given a collection of distinct integers, return all possible purmutations 

def permutations (array):
    res = []
    def helper(start):
        if (start == len(array) - 1 ): 
            res.append(array[:])
        else: 
            for i in range(start, len(array)): 
                print(start)
                array[start], array[i] = array[i], array[start]
                helper(start + 1)
                array[start], array[i] = array[i], array[start]
    helper(0)
    return res
    
print(permutations([1,2,3]))