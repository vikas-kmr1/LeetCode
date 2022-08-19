class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = {x : 0 for x in jewels}
        count = 0
        for x in stones:
            if x in dict:
                count += 1
        return count