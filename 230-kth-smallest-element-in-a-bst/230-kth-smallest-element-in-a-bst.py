# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        current  = root
        stack = []
        while True :
            
            while current  :
                stack.append(current)
                current = current.left
            
            
            current = stack.pop()
            k -= 1
            if not k:
                return current.val
            
            current = current.right
            
            
        
        