# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0) # creating new listed list that stores result
        current = head
        
        carry = 0
        
        while l1 or l2 or carry != 0:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
        
            two_sum = (a+b+carry)
            carry = two_sum//10
            current.next  = ListNode(two_sum%10)
            
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
    
        
        return head.next
    
            
            
            
            
        
        
        
        