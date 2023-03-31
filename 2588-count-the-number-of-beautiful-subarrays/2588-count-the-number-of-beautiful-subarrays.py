class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        lookUp = {0:1}
        cnt = 0
        xor = 0
        for n in nums:
            xor = xor^n
            cnt += lookUp.get(xor,0)
            lookUp[xor] = lookUp.get(xor,0)  +1 
        
        return cnt
            
        