class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

#class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
#         if len(intervals) <= 1:
#             return intervals
        
    
#         result  = []
        
#         intervals.sort()
        
#         minX =intervals[0][0]
#         maxY =intervals[0][1]
        
#         for i in  range(1,len(intervals) ):
#             a,b = intervals[i][0],intervals[i][1]
        
#             if a <= maxY:
#                 maxY = max([maxY,a,b])
            
#             else:
#                 result.append([minX,maxY])
#                 minX = a
#                 maxY = b
        
#         result.append([minX,maxY])
#         return result
            
            
                
          