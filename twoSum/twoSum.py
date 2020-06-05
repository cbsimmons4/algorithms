# Given an array of integers, return indices of the two numbers such
# that thay add up to a specific target

# You may assume that each input would have exacly one solution,
# and you may not use the same element

def twoSum (array, target):
    map = {}
    for i, ele in enumerate(array):
        if (ele in map.keys()) and target == ele*2:
            return [map[ele],i]
        map [ele] = i

    for ele in array:
        if ( (target - ele) in map.keys() and target != ele* 2):
            return [map[ele],map[target-ele]]

    return False

#False
print (twoSum([1,4,8,4,9],1))

#False
print (twoSum([1,4,8,4,9],100))

#[0,4]
print (twoSum([1,4,8,4,9],10))

#[3,2]
print (twoSum([1,4,8,4,9],12))

#[1,3]
print (twoSum([1,4,8,4,9],8))