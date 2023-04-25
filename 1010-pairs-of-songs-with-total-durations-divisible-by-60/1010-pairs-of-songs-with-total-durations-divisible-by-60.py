class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = 0
        lookup =  defaultdict(int) 

        for t in time:
            n = 60 - (t%60) 
            if n == 60:
                n = 0
            if n in lookup:
                cnt += lookup[n]
            
            lookup[t % 60] += 1
        
        return cnt
        