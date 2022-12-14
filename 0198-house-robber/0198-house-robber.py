class Solution:
    def rob(self, nums: List[int]) -> int:
        # base case
        if len(nums) == 1: return nums[0]
        
        # make a tabulation recipe
        table = [0 for _ in range(len(nums))]
        # seed the first 2 values
        table[0] = nums[0]
        table[1] = nums[1]
        
        # iterate through each element
        # for each element, look ahead 2 spaces ( to skip a house ), 
        # and then iterate through the rest of the elements, adding the cur
        # sum to the value stored at the table[j], but using max() to store the greatest value
        
        # at end of iteration, return the maximum amount between the last 2 indexes
		# to see if we either stopped at the last house or the second to last house to 
		# get the greatest value
        # table[-1] and table[-2]
        
        for i in range(len(nums)):
            for j in range(i+2, len(nums)):
                # add the ith index with jth index 
                # to find sum of robbing both indexes, 
                # then add if > cur elem
                table[j] = max(table[j], table[i] + nums[j])
                
        # return max of last 2 elements
        return max(table[-1], table[-2])