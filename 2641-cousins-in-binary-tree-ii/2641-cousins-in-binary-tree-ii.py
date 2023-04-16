# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def replaceValueInTree(self,root):
        q = deque()
        q.append(root)
        root.val = 0
        
        while q:
            n ,childrenSum = len(q) , 0
            parents = []
            for _ in range(n):
                node = q.popleft()
                parents.append(node)
                if node.left:
                    childrenSum += node.left.val
                    q.append(node.left)
                if node.right:
                    childrenSum += node.right.val
                    q.append(node.right)
                    
            for parent in parents:
                s = childrenSum
                if parent.left:
                    s -= parent.left.val
                if parent.right:
                    s -= parent.right.val
                if parent.left:
                    parent.left.val = s
                if parent.right:
                    parent.right.val = s
        return root
                    
