from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res = 1
        q = deque()
        q.append((root, 0))
        
        while q:
            cnt = len(q)
            start = q[0][1]
            end = q[-1][1]
            
            res = max(res, end - start + 1)
            
            for i in range(cnt):
                node, idx = q.popleft()
                
                if node.left:
                    q.append((node.left, 2 * idx + 1))
                
                if node.right:
                    q.append((node.right, 2 * idx + 2))
        
        return res
