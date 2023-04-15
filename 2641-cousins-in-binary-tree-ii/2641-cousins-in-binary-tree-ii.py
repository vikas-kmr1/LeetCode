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
            n, total = len(q), 0
            buf = []
            for i in range(n):
                node = q.popleft()
                buf.append(node)
                if node.left:
                    q.append(node.left)
                    total += node.left.val
                if node.right:
                    q.append(node.right)
                    total += node.right.val
            for node in buf:
                t = total
                if node.left:
                    t -= node.left.val
                if node.right:
                    t -= node.right.val
                if node.left:
                    node.left.val = t
                if node.right:
                    node.right.val = t
        return root
