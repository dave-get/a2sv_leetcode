# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lis1 = []
        self.lis2 = []
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def left(node,col):
            if not node:
                return
            left(node.left,col-1)
            self.lis1.append([abs(col),node.val])
            left(node.right,col+1)
        def right(node,col):
            if not node:
                return 
            right(node.right,col+1)
            self.lis2.append([abs(col),node.val])
            right(node.left,col-1)
        left(root,0)
        right(root,0)
        if self.lis1 != self.lis2:
            return False
        return True