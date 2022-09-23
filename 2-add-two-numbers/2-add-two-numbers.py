# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity : O(\max(m, n))O(max(m,n)). Assume that mm and nn represents the length of l1 and l2 respectively, the algorithm above iterates at most \max(m, n)max(m,n) times.

# Space complexity : O(\max(m, n))O(max(m,n)). The length of the new list is at most \max(m,n) + 1max(m,n)+1


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0) # creating new listed list that stores result
        current = head
        
        carry = 0 # To store carry of sum  
        
        while l1 or l2 or carry != 0:
            
            a = l1.val if l1 else 0  #if l1 not exist a=0
            b = l2.val if l2 else 0  #if l1 not exist b=0
        
            two_sum = (a+b+carry)
            carry = two_sum//10
            current.next  = ListNode(two_sum%10)
            
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
    
        return head.next
    
            
            
            
            
        
        
        
        