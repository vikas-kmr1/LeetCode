class Solution:
      def specialArray(self, nums: List[int]) -> int:
        l = len(nums)
        lis = [0 for i in range(l+1)]
        for i in nums:
            if i >= l:
                lis[l] +=1
            else:
                lis[i] +=1
        res = 0
        for i in range(l, 0, -1):
            res += lis[i]
            if res == i:
                return i
        return -1
            
    