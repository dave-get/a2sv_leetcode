# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res_node = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       
        def find(node,p,q):
            if not node:
                return False
            if node.val == p.val or node.val == q.val:
                if not self.res_node:
                    self.res_node = node
                return True
            left = find(node.left,p,q)
            right = find(node.right,p,q)
            if right and left:
                self.res_node = node

            return left or right
        find(root,p,q)
        # print(self.res_node.val)
        return self.res_node
             
            