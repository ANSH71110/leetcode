# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    def getTargetCopy(self, org: TreeNode, cl: TreeNode, t: TreeNode) -> TreeNode:
        def dfs(n1,n2):
            if not n1 or self.stop:
                return
            
            if n1 is t:
                self.stop=True
                self.clt=n2
                return
            
            dfs(n1.left,n2.left)
            dfs(n1.right,n2.right)
            
        self.stop=False
        dfs(org,cl)
        return self.clt
