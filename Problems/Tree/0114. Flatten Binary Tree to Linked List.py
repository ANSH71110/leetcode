# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    r=TreeNode(None)
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans=self.r
        self.dfs(root)
    def dfs(self,node1):
        if not node1:
            return
        self.r.left=None    
        self.r.right=node1
        self.r=self.r.right
        a,b=node1.left,node1.right
        self.dfs(a)
        self.dfs(b)
