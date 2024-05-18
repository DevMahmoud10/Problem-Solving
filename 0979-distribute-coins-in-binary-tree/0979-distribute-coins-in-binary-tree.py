# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0
            left_extra,right_extra = dfs(node.left),dfs(node.right)
            extra_coins = left_extra + right_extra + node.val-1
            nonlocal res
            res+=abs(extra_coins)
            return extra_coins
            
        res=0
        dfs(root)
        return res