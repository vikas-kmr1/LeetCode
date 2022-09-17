class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0 
        def fun(arr):
            nonlocal ans 
            if len(arr)<=1:
                return arr
            left = fun(arr[:len(arr)//2])
            right = fun(arr[len(arr)//2:])
            j = 0 
            for i in range(len(left)):
                while j<len(right):
                    if 2*right[j]<left[i]:
                        j+=1
                    else:
                        break
                ans += j 
            return list(sorted(left + right))
        
        fun(nums)
        return ans