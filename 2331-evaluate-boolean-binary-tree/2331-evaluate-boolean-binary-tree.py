# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: return
            if not node.left and not node.right:
                return node.val
            if node.left and node.right:
                l,r = dfs(node.left),dfs(node.right)
                return l and r if node.val==3 else l or r
        return dfs(root)
            
                
                
            