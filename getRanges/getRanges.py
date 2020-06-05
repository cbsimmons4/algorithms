# Given a sorted list of values and a target,
# return the first index and the last index of the target

def getRangesHelper(array,index,target,lbIn,ubIn):
    first = index
    last = index

    lb = lbIn
    ub = index
    while ((lb <= ub) and (first > 0) and (array[first-1] == target)):
        cur = int((lb + ub)/2)
        if (array[cur] == target):
            first = cur
        if (target <= array[cur]):
            ub = cur 
        else: lb = cur 

    lb = index
    ub = ubIn
    while ((lb <= ub) and (last < len(array) - 1) and (array[last+1] == target)):
        cur = int((lb + ub)/2)
        if (array[cur] == target):
            last = cur
        if (target < array[cur]):
            ub = cur 
        else: lb = cur 

    return [first,last]
    
def getRanges (array, target):
    lb = 0
    ub = len(array)
    while (lb + 1 < ub or array[lb] == target):
        cur = int((lb + ub)/2)
        if (array[cur] == target): return getRangesHelper(array,cur,target,lb,ub)
        if (target <= array[cur]):
            ub = cur
        else: lb = cur
    return False
        
print(getRanges([1,1,1,2], 1))


# O(logN)
