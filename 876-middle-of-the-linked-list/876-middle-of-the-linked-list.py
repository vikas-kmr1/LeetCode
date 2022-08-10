# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        
        current = head
        
        while current:
            lst.append(current)
            current = current.next
        return lst[len(lst)//2] 
            
        
        
            
        
        