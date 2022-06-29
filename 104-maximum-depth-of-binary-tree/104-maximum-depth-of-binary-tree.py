# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def height(node):
            if node is None:
                    return 0
            else:
                # Compute the height of each subtree
                lheight = height(node.left)
                rheight = height(node.right)
                     # Use the larger one
                if lheight > rheight:
                    return lheight+1
                else:
                    return rheight+1
                
        return height(root)