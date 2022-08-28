# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # if root not exist return 
        if not root:
            return []
        
        
        #using BFS
        
        ans = [] #(list of lists storing ) level order lists 
        queue  = collections.deque()
        queue.append(root) # pushing root or source node in the queue
    
    
        # run untill queue is not empty
        while queue:
            
            lst = []
            
            queue_size = len(queue)
            
            lst = []
            # run for each node in the queue
            
            for _ in range(queue_size):
                node = queue.popleft()
                
                lst.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            #adding the level ordered list
            ans.append(lst)
            
            #reinitialize an empty list
            lst = []
                    
        return ans
            
                
            
            
                
        