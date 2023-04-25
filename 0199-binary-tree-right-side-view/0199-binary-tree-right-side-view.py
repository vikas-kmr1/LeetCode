# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                rightSide = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(rightSide.val)
        return res

#         ans = []

#         def rightView(node, level):
#             if not node:
#                 return
#             if level == len(ans):
                
#                 ans.append(node.val)
#             rightView(node.right,level+1)
#             rightView(node.left,level+1)
             
#         rightView(root,0)

#         return ans
