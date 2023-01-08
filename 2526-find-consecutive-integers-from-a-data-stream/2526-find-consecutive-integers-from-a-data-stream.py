class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.val = value
        self.ind = 0
        
    def consec(self, num: int) -> bool:
        if self.val == num:
            self.ind += 1
        else:
            self.ind = 0
   
        return self.ind >= self.k 
            
        
            
            


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)