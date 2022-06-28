# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            dup_val = head.val
            current = head
        
            while current.next:
                if current.next.val == dup_val:
                    current.next = current.next.next
                    continue
        
                if current.next.val > dup_val:
                    dup_val = current.next.val
                    current = current.next
            
        return head
                
            
    