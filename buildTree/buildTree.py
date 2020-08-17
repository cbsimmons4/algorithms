# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        if len(postorder) <= 0: return None
        self.root = TreeNode(postorder[-1],None,None)
        curRoot = self.root
        leftSet = set()
        leftInorder = []
        rightInorder = []
        pastRoot = False
        for num in inorder:
            if num == self.root.val:
                pastRoot = True
            elif pastRoot:
                rightInorder.append(num)
            else:
                leftInorder.append(num)
                leftSet.add(num)
        leftPostorder = []
        rightPostorder = []
        for num in postorder:
            if num == self.root.val:
                continue
            elif num in leftSet:
                leftPostorder.append(num)
            else:
                rightPostorder.append(num)
        self.buildTreeHelper(leftInorder,leftPostorder,curRoot,True)
        self.buildTreeHelper(rightInorder,rightPostorder,curRoot,False)
        return self.root
    
    def buildTreeHelper(self, inorder,postorder,curRoot,isLeft):
        if len(inorder) <= 0:
            return
        subRoot = TreeNode(postorder[-1],None,None)
        if isLeft:
            curRoot.left = subRoot
        else:
            curRoot.right = subRoot
        leftSet = set()
        leftInorder = []
        rightInorder = []
        pastRoot = False
        for num in inorder:
            if num == subRoot.val:
                pastRoot = True
            elif pastRoot:
                rightInorder.append(num)
            else:
                leftInorder.append(num)
                leftSet.add(num)
        leftPostorder = []
        rightPostorder = []
        for num in postorder:
            if num == subRoot.val:
                continue
            elif num in leftSet:
                leftPostorder.append(num)
            else:
                rightPostorder.append(num)
        self.buildTreeHelper(leftInorder,leftPostorder,subRoot,True)
        self.buildTreeHelper(rightInorder,rightPostorder,subRoot,False)
        
def printTree(root):
    if root == None:
        return
    print(root.val)
    printTree(root.left)
    printTree(root.right)

mySolution = Solution()
root = mySolution.buildTree([9,3,15,20,7], [9,15,7,20,3])
printTree(root)

