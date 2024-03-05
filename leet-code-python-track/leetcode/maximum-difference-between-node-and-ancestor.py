# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        diff = 0
        def search(node,max_,min_):
            nonlocal diff
            if not node:
                return 
            if node.val > max_:
                max_ = node.val
            if min_ > node.val:
                min_ = node.val
            if abs(max_ - min_) > diff:
                diff = abs(max_ - min_)
            search(node.left,max_,min_)
            search(node.right,max_,min_)
        search(root,-1,float("inf"))
        return diff