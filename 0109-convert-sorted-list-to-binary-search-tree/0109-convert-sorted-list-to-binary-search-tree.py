# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None
        
        def toBst(head ,tail = None):
            slow = fast = head
            if head == tail:return None
            
            while (fast is not tail) and (fast.next is not tail):
                slow = slow.next
                fast = fast.next.next
                
            
            node = TreeNode(slow.val)
            node.left = toBst(head, slow)
            node.right =toBst(slow.next, tail)
            return node
        
        return toBst(head)
        
        
                
            
        