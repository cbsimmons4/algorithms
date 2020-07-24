# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        self.traversal = []
        self.zigzagLevelOrderHelper(root, 0)
        for i in range(0,len(self.traversal)):
            if i % 2 != 0:
                self.traversal[i].reverse()
        return self.traversal
        

    def zigzagLevelOrderHelper(self, cur, depth):
        if cur == None:
            return
        if depth >= len(self.traversal):
            self.traversal.append([])
        self.traversal[depth].append(cur.val)
        self.zigzagLevelOrderHelper(cur.left, depth + 1)
        self.zigzagLevelOrderHelper(cur.right, depth + 1)




mySolution = Solution()

root = TreeNode( 3, TreeNode(9,None
,None),TreeNode(20,
TreeNode(20,None,None),TreeNode(7,None,None)))

print(mySolution.zigzagLevelOrder(root))




