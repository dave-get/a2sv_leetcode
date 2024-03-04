# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)//2
        if n < 0 or n > len(nums)-1:
            return None
        node = TreeNode(nums[n])
        left = self.sortedArrayToBST(nums[:n])
        right = self.sortedArrayToBST(nums[n+1:])
        node.left = left
        node.right = right
        return node