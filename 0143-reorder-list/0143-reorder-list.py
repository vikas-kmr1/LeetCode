# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid 
        
        fast , slow =  head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        # reverse second half
        curr = slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp
            
        curr = head 
        while prev:
            cNext , pNext = curr.next , prev.next
            
            curr.next = prev
            prev.next = cNext
            
            curr = cNext
            prev = pNext
            
            
            
            
            
            
            
            
        
        
        