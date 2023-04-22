# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []

        def helper(root,ind):
            if  len(res) < ind+1 :
                res.append([root.val])
            elif len(res) >= ind+1:
                res[ind].append(root.val)
            
            if root.left: helper(root.left,ind+1)
            if root.right: helper(root.right,ind+1)
        res = []
        helper(root,0)
        return res

# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
#         # if root not exist return 
#         if not root:
#             return []
        
        
#         #using BFS
        
#         ans = [] #(list of lists storing ) level order lists 
#         queue  = collections.deque()
#         queue.append(root) # pushing root or source node in the queue
    
    
#         # run untill queue is not empty
#         while queue:        
#             queue_size = len(queue)
            
#             lst = []
#             # run for each node in the queue
            
#             for _ in range(queue_size):
#                 node = queue.popleft()
                
#                 lst.append(node.val)
                
#                 if node.left:
#                     queue.append(node.left)
                
#                 if node.right:
#                     queue.append(node.right)

#             #adding the level ordered list
#             if lst:
#                 ans.append(lst)
#         return ans
            
        
                
            
            
                
        