# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.n = 0 
        curr = head
        while curr:
            self.n += 1
            curr = curr.next
            
    def getRandom(self) -> int:
        n = random.randint(0,self.n - 1)
        curr = self.head
        i = 0
        while curr and i < n:
            curr = curr.next
            i += 1
        return curr.val
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()