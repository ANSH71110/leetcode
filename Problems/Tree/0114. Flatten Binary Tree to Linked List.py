# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root and (root.right or root.left):
            stack=[]
            def dfs(node1):
                if not node1:
                    return 
            
                stack.append(node1)
                dfs(node1.left)
                dfs(node1.right)
            dfs(root)
            r=root
            while stack:
                r.right=stack.pop(0)
                r=r.right
                r.left=None
            root=r
