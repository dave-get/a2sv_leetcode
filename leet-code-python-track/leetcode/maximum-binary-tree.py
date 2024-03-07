# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def create(s,e):
            if not nums[s:e]:
                return None
            indx = nums.index(max(nums[s:e]))
            tree = TreeNode(max(nums[s:e]))
            tree.left =  create(s,indx)
            tree.right = create(indx+1,e)
           
            return tree
        return create(0,len(nums))