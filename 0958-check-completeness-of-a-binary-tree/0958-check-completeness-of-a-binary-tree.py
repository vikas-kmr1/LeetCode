# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        
        i = 0
        while q[i]:
            q.append(q[i].left)
            q.append(q[i].right)
            i += 1
    
        return not any(q[i:])
        
        
        