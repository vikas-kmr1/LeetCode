


    

class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        
        max_pro =  0
        mini = 1000001
        
        for i in range(len(prices)):
            if(prices[i] < mini):
                mini = prices[i]
            else:
                max_pro = max(max_pro,prices[i] - mini )
        
        return max_pro
             
        
        
        
        
            
            
        
           
                
                