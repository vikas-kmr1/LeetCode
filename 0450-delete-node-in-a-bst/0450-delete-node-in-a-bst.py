# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lastRight(self,root):
        while root.right:
            root = root.right
        return root

    def deleteNode(self, root, key):
        if not root: return None
        
        if root.val == key:
            if not root.right: return root.left
            
            if not root.left: return root.right
            
            
            rightChild = root.right
            lastRight = self.lastRight(root.left)
            
            lastRight.right = rightChild
            
            return root.left
            
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root

    
# change the val of the node to the key 
# class Solution:
#     def findRightMost(self ,root):
#         if root.left is None:
#             return root
#         return self.findRightMost(root.left)


#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
#         if root is None:
#             return root
#         if root.val == key :
#             if root.right is None:
#                 return root.left
#             if root.left is None:
#                 return root.right
#             root.val = self.findRightMost(root.right).val 
#             root.right = self.deleteNode(root.right,root.val)
            
#         elif root.val < key:
#             root.right = self.deleteNode(root.right,key)
#         else:
#             root.left = self.deleteNode(root.left,key)
#         return root