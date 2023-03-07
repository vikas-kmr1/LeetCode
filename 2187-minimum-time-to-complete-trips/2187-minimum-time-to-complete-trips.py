class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        left,right = 1 , min(time) * totalTrips
        minTime = right
    
        while left <= right:
            t = (left + right)//2
            completedTrips = 0
            for n in time:
                completedTrips += ( t // n )
         
            if completedTrips >= totalTrips:
                right = t - 1
                minTime = min(t,minTime)
            else:
                left = t + 1
                
        return minTime
                
            
        
        