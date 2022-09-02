# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        ans = []
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            
            lst = []
            
            for i in range(len(queue)):
                node =  queue.popleft()
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
                lst.append(node.val)
                
            ans.append(sum(lst) / len(lst) )
            
        return ans
            
            
        
        
        
        
        