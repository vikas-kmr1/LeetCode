# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = []
        q = collections.deque([root])

        while q:
            leftSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
        
                leftSide = node
                if node.right:    
                    q.append(node.right)
                if node.left:
                    q.append(node.left)        
            res.append(leftSide.val) 
        return res[-1]
        
        
        
#         res = [] 
        
#         def dfs(root,level):
#             if not root:
#                 return 
#             if level == len(res):
#                 res.append(root.val)
            
#             dfs(root.left , level + 1)
#             dfs(root.right, level + 1)
            
        dfs(root,0)
        return res[-1]