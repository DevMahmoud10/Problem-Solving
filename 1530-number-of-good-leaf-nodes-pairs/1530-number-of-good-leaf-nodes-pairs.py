# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def build_graph(node):
            if not node: return
            if node not in g:
                g[node]=[]
            if node.left:
                if node.left not in g:
                    g[node.left]=[]
                g[node].append(node.left)
                g[node.left].append(node)
            if node.right:
                if node.right not in g:
                    g[node.right]=[]
                g[node].append(node.right)
                g[node.right].append(node)
            if not node.left and not node.right:
                leafs.add(node)
            build_graph(node.left)
            build_graph(node.right)
        
        def bfs(leaf_node):
            visited=set([leaf_node])
            q=[(leaf_node,0)]
            while q:
                node,dist=q.pop(0)
                if leaf_node!=node and node in leafs and dist<=distance:
                    nonlocal res
                    res+=1
                for nei in g[node]:
                    if nei not in visited and dist<distance:
                        visited.add(nei)
                        q.append((nei,dist+1))
                        
        
        g={}
        leafs=set()
        build_graph(root)
        res=0
        for leaf_node in leafs:
            bfs(leaf_node)
        return res//2
        