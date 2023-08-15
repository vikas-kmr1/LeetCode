# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = dummy  = ListNode()
        right = dummy2 = ListNode()
        
        curr = head
        while curr:
            if curr.val < x:
                left.next = curr
                left = curr
            else:
                right.next = curr
                right = curr
            
            curr = curr.next
        right.next = None
        left.next = dummy2.next
        return dummy.next
        