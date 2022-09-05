"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []
        
        queue = collections.deque()
        queue.append(root)
        
        ans  = []
        
        while queue:
            lst = []
            for _ in range(len(queue)):
                
                node = queue.popleft()
                lst.append(node.val)
                
                for child in  node.children:
                    queue.append(child)
            
            if lst:
                ans.append(lst)
                    
                    
        return ans        
                
                
        
        