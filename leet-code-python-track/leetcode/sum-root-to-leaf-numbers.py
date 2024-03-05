# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sm = 0
        num = 0
        def sum_(node):
            nonlocal sm,num
            if not node:
                return
            if not node.left and not node.right:
                num = num * 10 + node.val
                sm +=num
                num =(num - node.val)//10
                return sm
            num = num * 10 + node.val
            sum_(node.left)
            sum_(node.right)
            num =(num - node.val)//10
            return sm
        return sum_(root)