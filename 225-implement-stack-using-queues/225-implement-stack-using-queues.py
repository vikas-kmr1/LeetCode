class MyStack:

    def __init__(self):
        self.arr = []
        

    def push(self, x: int) -> None:
        
        self.arr.append(x)
        

    def pop(self) -> int:
        if self.arr:
            return self.arr.pop(-1)
        return -1
    
    def top(self) -> int:
        if self.arr:
            return self.arr[-1]

    def empty(self) -> bool:
        if self.arr:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()