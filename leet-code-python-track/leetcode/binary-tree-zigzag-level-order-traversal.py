# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        dict_ = defaultdict(list)
        def search(node,row,col):
            if not node:
                return 
            dict_[row].append(node.val)
            search(node.right,row+1,col+1)
            search(node.left,row+1,col-1)
        search(root,0,0)
        ans = []
        for i in dict_.values():
            ans.append(i)
        for i in range(len(ans)):
            if i > 1 and i%2 == 0:
                ans[i] = ans[i][::-1]
        return ans 