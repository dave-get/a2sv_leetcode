# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lis = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 
        else:
            self.lis.append(root.val)
        if root.left:
            self.kthSmallest(root.left,0)
        if root.right:
            self.kthSmallest(root.right,0)
        
        return (sorted(self.lis)[k-1])