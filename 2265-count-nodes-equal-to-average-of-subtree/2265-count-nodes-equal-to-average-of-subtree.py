# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def get_avg(node):
            nonlocal res
            if not node:
                return 0,0
            
            if not node.left and not node.right:
                res+=1
                return node.val,1
            
            left_sum,left_count = get_avg(node.left)
            right_sum,right_count = get_avg(node.right)
            
            cur_sum = left_sum+right_sum+node.val
            cur_count = left_count+right_count+1
            
            cur_avg=cur_sum//cur_count
            if cur_avg==node.val:
                res+=1
            return cur_sum,cur_count
        
        res=0
        get_avg(root)
        return res