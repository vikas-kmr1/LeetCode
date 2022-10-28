class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(1,len(heights)):
            k = i
            for j in range(i-1,-1,-1):
                if heights[k] > heights[j]:
                    
                    heights[k], heights[j] = heights[j], heights[k]
                    names[k],names[j] = names[j],names[k]
                    k = j
        
        
        return names
                
                    
                
                