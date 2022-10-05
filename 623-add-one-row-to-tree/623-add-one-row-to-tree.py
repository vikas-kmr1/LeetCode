# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], v: int, d: int,left:bool = True) -> Optional[TreeNode]:
        if d == 1:
            return TreeNode(v, root if left else None, root if not left else None)
        elif root:
            root.left = self.addOneRow(root.left, v, d - 1, True)
            root.right = self.addOneRow(root.right, v, d - 1, False)
        return root
        