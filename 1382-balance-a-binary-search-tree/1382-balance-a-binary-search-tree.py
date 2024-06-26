# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder_traversal(node):
            if not node: return
            inorder_traversal(node.left)
            inorder_nodes.append(node.val)
            inorder_traversal(node.right)
        
        def build_bst(l,r):
            if l>r: return
            mid=l+(r-l)//2
            left=build_bst(l,mid-1)
            right=build_bst(mid+1,r)
            return TreeNode(inorder_nodes[mid],left,right)
        
        
        inorder_nodes=[]
        inorder_traversal(root)
        return build_bst(0,len(inorder_nodes)-1)