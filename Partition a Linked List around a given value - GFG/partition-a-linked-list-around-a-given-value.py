#User function Template for python3

"""

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""
class Solution:
    def partition(self, head, x):
        #code here
        left = dummy  = Node(0)
        equal = dummy3 = Node(0)
        right = dummy2 = Node(0)
        
        curr = head
        while curr:
            if curr.data < x:
                left.next = curr
                left = curr
            elif curr.data == x:
                equal.next = curr
                equal = curr
            else:
                right.next = curr
                right = curr
            curr = curr.next
            
        right.next = None
        equal.next = dummy2.next
        left.next = dummy3.next
        return dummy.next
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.partition(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1




# } Driver Code Ends