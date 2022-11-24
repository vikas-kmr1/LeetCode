import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x,y in points:
            dist =  abs(x**2 - 0 ) + abs(y**2 - 0)
            pts.append([dist,x,y])
        res = []
        
        heapq.heapify(pts)
        for _ in range(k):
            dist,x,y = heapq.heappop(pts)
            res.append([x,y])
        return res