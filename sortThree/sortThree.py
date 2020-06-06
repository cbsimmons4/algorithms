# Given an unsorted array with atmost three distict values,
# return a sorted array 

def sortThree (array):
    map = {}
    for ele in array:
        if ele in map.keys():
            map[ele] += 1
        else: map[ele] = 1
    i = 0 
    for key in sorted((map.keys())):
        while ( map[key] > 0):
            array[i] = key
            map[key] -= 1
            i += 1 
    return array
    
print (sortThree([3,2,3,3,2,2,2,2,1,1,1,1]))