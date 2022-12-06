# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        level = 0
        while queue:
            level += 1
            b = len(queue)
            for i in range(b):
                rt = queue.popleft()
                if rt.left:
                    queue.append(rt.left)
                if rt.right:
                    queue.append(rt.right)
                if not rt.left and not rt.right:
                    return level
        return -1
        