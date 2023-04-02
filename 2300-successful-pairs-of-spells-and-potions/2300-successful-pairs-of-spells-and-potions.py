class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        #T.C = O(mlogm + nlogm ) ,where n = len(spells) and m = len(potions)
        #S.C = O(n)
        
        pairs = [] 
        lookUp = {}
        potions.sort()
        for n in spells:
            cnt = 0 
            if n in lookUp :
                cnt = lookUp[n]
            else:
                cnt = self.binarySearch(potions,n,success) 
                lookUp[n] = cnt 
            pairs.append(cnt)
        return pairs
        
    def binarySearch(self,potions,n,success):
            left = 0
            right = len(potions) - 1

            while left <= right:
                mid = left + (right - left)//2 
                need = n * potions[mid]
        
                if need  >= success:
                    right = mid - 1
                else:
                    left  = mid + 1
                    
            return len(potions) - left
                
                