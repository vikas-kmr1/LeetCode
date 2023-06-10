
class Node:
    def __init__(self,val=0,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next

        while curr and index  :
            curr = curr.next
            index -= 1

        if curr and index == 0 and curr != self.tail:
            return curr.val
        return -1 

        
    def addAtHead(self, val: int) -> None:
        next,prev = self.head.next, self.head
        node = Node(val,next, prev )
        next.prev = node
        prev.next = node 

    def addAtTail(self, val: int) -> None:
        next, prev = self.tail, self.tail.prev
        node = Node(val, next, prev)
        prev.next = node
        next.prev = node
        
    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        
        while curr and index:
            index -= 1
            curr = curr.next

        if curr and index == 0 :
            next, prev = curr , curr.prev
            node = Node(val, next, prev)
            next.prev = node
            prev.next = node
            
        
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        
        while index and curr:
            index -= 1
            curr = curr.next

        if curr and index == 0 and curr != self.tail:
    
            curr.prev.next, curr.next.prev = curr.next, curr.prev
            

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)