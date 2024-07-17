# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete=set(to_delete)
        res=[]
        q=[root]
        while q:
            node=q.pop(0)
            if node.left:
                q.append(node.left)
                if node.left.val in to_delete:
                    node.left=None
            if node.right:
                q.append(node.right)
                if node.right.val in to_delete:
                    node.right=None
            if node.val in to_delete:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
        if root.val not in to_delete:
            res.append(root)
        return res