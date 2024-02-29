# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        lis = []
        def mode(node):
            if not node:
                return 
            lis.append(node.val)
            mode(node.left)
            mode(node.right)
        mode(root)
        c = Counter(lis)
        m = max(c.values())
        ans = []
        for k,v in c.items():
            if v == m:
                ans.append(k)

        return ans

