


    

class Solution:
    # two pointer approach
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        l,r = 0,1
        while r < len(prices):
            if prices[l] < prices[r]:
                max_pro = max(prices[r] - prices[l],max_pro)
            
            else:
                l = r 
            r += 1 
        return max_pro
        
        
        
        # first approach
#         max_pro =  0
#         mini = 1000001
        
#         for i in range(len(prices)):
#             if(prices[i] < mini):
#                 mini = prices[i]
#             else:
#                 max_pro = max(max_pro,prices[i] - mini )
        
#         return max_pro
             
        
        
        
        
            
            
        
           
                
                