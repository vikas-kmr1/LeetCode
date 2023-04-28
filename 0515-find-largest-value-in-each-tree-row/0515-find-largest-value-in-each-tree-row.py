# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        q = deque([root])
        res = []

        while q:
            n = len(q)
            maxNode = q[0].val
            for i in range(n):
                node = q.popleft()
                
                maxNode = max(maxNode,node.val) 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(maxNode)
        return res
                
        
        