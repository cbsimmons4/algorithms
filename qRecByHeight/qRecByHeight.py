# Suppose you are given a list of people in a queue
# Each person is described by a pair of integers 
# (h,k), where k is the height of the person 
# and k is the number of people in front 
# of this person who have 
# a height greater than or equal to h.
# Write an algorithm to reconstruct the
# queue

def qRecByHeight (Qin):
    kMap = {}
    for ele in Qin:
        if ele[1] in kMap.keys():
            kMap[ele[1]].append (ele[0])
        else:
            kMap[ele[1]] = [ele[0]]

    Qout = []
    for k in sorted(kMap.keys()):
        for h in sorted(kMap[k], reverse = True):
            quota = k
            i = 0
            while (quota > 0):
                if (h <= Qout[i][0]):
                    quota -= 1
                i += 1
            Qout.insert(i, [h,k])
    return Qout
            
print (qRecByHeight([[7, 0], [4, 5], [8, 0], [5, 0], [6, 1], [5, 2]]))
# [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]