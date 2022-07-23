# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], l: int, h: int) -> int:
        def dfs(n1,s):
            if not n1:
                return
            if n1.val<=h and n1.val>=l:
                self.s+=n1.val

            dfs(n1.left,s)
            dfs(n1.right,s)
        
        self.s=0   
        dfs(root,0)
             
        return self.s
