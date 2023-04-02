class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        v = {chars[i]:vals[i] for i in range(len(chars))}
        arr = [ v.get(c, ord(c) - 96 ) for c in s ]
        
        curSum = 0
        mSum = 0
        
        for n in arr:
            curSum = max(n, curSum+n)
            mSum = max(mSum, curSum)
        return mSum if mSum > 0 else 0
            
    
        
        
        