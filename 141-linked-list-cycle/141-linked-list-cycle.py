# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current =  head
        list_ = []
        
        while(current):
            if current in list_:
                return True
            list_.append(current)
            current = current.next
        