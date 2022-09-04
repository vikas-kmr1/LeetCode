# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ans = ListNode(-101,head)
        current = head
        while current:
             
            if current.next and current.next.val == current.val:
                while current.next and current.next.val == current.val:
                    current = current.next
            
                dummy.next = current.next
                
            else:
                dummy = dummy.next
                
            current  = current.next
            
        return ans.next
                
            