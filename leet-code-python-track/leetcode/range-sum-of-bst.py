# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum_ = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return
        if root.val <= high and root.val >= low:
            self.sum_ +=root.val
        self.rangeSumBST(root.right,low,high)
        self.rangeSumBST(root.left,low,high)
        return self.sum_
        