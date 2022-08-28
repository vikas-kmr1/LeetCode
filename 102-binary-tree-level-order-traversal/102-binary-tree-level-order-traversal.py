# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        
        ans = []
        queue  = collections.deque()
        queue.append(root)
    
        while queue:
            lst = []
            
            
            
            queue_size = len(queue)
            
            lst = []
            for _ in range(queue_size):
                node = queue.popleft()
                
                lst.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            ans.append(lst)
            lst = []
                    
        return ans
            
                
            
            
                
        