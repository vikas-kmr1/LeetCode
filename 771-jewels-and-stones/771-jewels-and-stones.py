class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = {}
        for x in jewels:
            dict[x] = 0
            
        count = 0
        for x in stones:
            if x in dict:
                count += 1
        return count