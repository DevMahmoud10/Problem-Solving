# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children=set()
        g={}
        for p,c,d in descriptions:
            if p not in g:
                g[p]=TreeNode(val=p)
            if c not in g:
                g[c]=TreeNode(val=c)
            children.add(c)
        
        for p,c,d in descriptions:
            if d:
                g[p].left=g[c]
            else:
                g[p].right=g[c]
                
        root=list(set(g)-children)[0]
        return g[root]
        
                