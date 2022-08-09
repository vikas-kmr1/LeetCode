class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        store =  dict()
        
        for stone in stones:
            if stone in store:
                store[stone] += 1
            else:
                store[stone] = 1
        
       
        
        count_stone = 0
        
        for tStone in jewels:
            if tStone in store:
                count_stone += store[tStone]
                
        return count_stone
            
                
        