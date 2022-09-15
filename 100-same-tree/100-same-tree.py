# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
#         if not q and not p:
#             return True
        
#         if not q or not p: return False
        
#         if p.val != q.val: return False
        
#         return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
        
class Solution:

    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            (p, q) = stack.pop(0)
            if p and q and p.val == q.val:
                stack.extend([
                    (p.left,  q.left),
                    (p.right, q.right)
                ])
            elif p or q:
                return False
        return True