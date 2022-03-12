# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        _next = None
        
        while head:
            _next = head.next
            head.next = prev
            prev = head
            head = _next
        
        return prev
        