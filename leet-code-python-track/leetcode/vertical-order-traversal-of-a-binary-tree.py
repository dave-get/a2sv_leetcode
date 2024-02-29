# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        dict_ = defaultdict(list)
        
        def traverse(node, row, col):
            if not node:
                return
            dict_[col].append((row, node.val))  

            traverse(node.left, row + 1, col - 1)
            traverse(node.right, row + 1, col + 1)
        
        traverse(root, 0, 0)
        sorted_nodes = sorted((col, sorted(vals)) for col, vals in dict_.items())
        
        ans = [[val for i, val in vals] for i,vals in sorted_nodes]
        
        return ans