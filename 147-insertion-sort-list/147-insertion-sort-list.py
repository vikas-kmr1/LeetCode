# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
         # keep the start of the list -> sentinel node
        # this really helps us to keep the code concise
        sentinel = ListNode(val=-50001, next=head)
        
        # we need to iterate through the list and check whether we are smaller then
        # the previous node
        # once this happens we need to do the following steps:
        # 1) cut out the node (set previous node.next to current.next)
        # 2) find the position to put the node
        #   2a) We need to start from the beginning and as soon we are smaller or equal
        #       to the next node
        #   2b) we insert by setting current.next to us and us.next to current.next
        # 3) We need to got back to the node we were and continue
        previous = sentinel
        current = head
        while current:
            
            # check whether we are smaller than previous node
            if current.val < previous.val:
                
                # delete the current node from the list (1)
                previous.next = current.next
                
                # go through the list until we encounter a node (2a)
                # that is bigger than us
                start = sentinel
                while start.next.val < current.val:
                    start = start.next
                    
                # insert our node in the list again (2b)
                current.next = start.next
                start.next = current
                
                # return to the previous node (3)
                current = previous
                
            # everything is fine and we can go on
            previous = current
            current = current.next
        
        return sentinel.next
                
            
            
            
        
    
    
        