class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        cnt = 1
        inc = 1
        dec = 1
        
        for k in range(1,len(arr)):
            
            if arr[k] < arr[ k - 1 ]:
                dec = inc + 1
                inc = 1
            elif arr[k] > arr[k - 1]:
                inc = dec + 1
                dec = 1
            else :
                inc = 1 
                dec = 1
        
            cnt =  max(cnt,max(dec,inc))
        return cnt
            