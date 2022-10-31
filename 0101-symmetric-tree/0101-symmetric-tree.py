# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def checkSymmetric(left,right)->bool:
            if (not left) or (not right):
                return left == right
            
            if left.val != right.val:
                return False
            
            return checkSymmetric(left.left,right.right) and checkSymmetric(left.right,right.left)
       
        return not root or checkSymmetric(root.left,root.right) 
        