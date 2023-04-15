# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def replaceValueInTree(self,root):
        q = Queue()
        q.put(root)
        root.val = 0
        while not q.empty():
            n, total = q.qsize(), 0
            buf = []
            for i in range(n):
                node = q.get()
                buf.append(node)
                if node.left:
                    q.put(node.left)
                    total += node.left.val
                if node.right:
                    q.put(node.right)
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
