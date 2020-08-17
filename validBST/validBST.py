# Problem:
# Given an array representation of a tree, is it a BST?

# A BST is defined as follows:
# - The left subtree of a node contains only nodes with keys less than the nodes key.
# - The right subtree of a node contains only nodes with keys greater than the nodes key.
# - Both the left and right subtree must also be binary search trees.

def isBST (tree):
    return isBSTHelper(tree, 0, float('-inf'), float('inf'))

def isBSTHelper (tree,index,lb,ub):
    leftChildIndex = (2 * index + 1)
    rightChildIndex = (2 * index + 2)

    hasLeft = True if (len(tree) > leftChildIndex
    and tree[leftChildIndex] != None) else False

    hasRight = True if (len(tree) > rightChildIndex
    and tree[rightChildIndex] != None) else False

    if ( not hasLeft and not hasRight ): return True

    leftIsBST = None
    if (hasLeft):
        if (tree[leftChildIndex] <= tree[index]
        and tree[leftChildIndex] > lb
        and  tree[leftChildIndex] <= ub):
            leftIsBST = isBSTHelper(tree, leftChildIndex , lb , tree[index])
        else:
            return False 
    
    rightIsBST = None
    if (hasRight):
        if (tree[rightChildIndex] > tree[index]
        and tree[rightChildIndex] > lb
        and tree[rightChildIndex] <= ub):
            rightIsBST = isBSTHelper(tree, rightChildIndex, tree[index], ub)
        else:

            return False

    if (hasLeft and hasRight ): return leftIsBST and rightIsBST
    elif (hasLeft): return leftIsBST
    else: return rightIsBST

# False: 4 < 5 but 4 is on 5's right
treeOne = [5,1,4,None,None,3,6]
print ('treeOne: ', isBST(treeOne))

# False: 4 < 5 but 4 is on 5's right.  
treeTwo = [5,1,6, None, None,4,7]
print ('treeTwo: ', isBST(treeTwo))

# False: 7 > 6 but 7 is on 6's left.  
treeThree = [5,1,6, None, None,7,8]
print ('treeThree: ', isBST(treeThree))

#True: All good!
treeFour = [5,1,7,None,None,6,8]
print ('treeFour: ', isBST(treeFour))



print(493827157>>2)
