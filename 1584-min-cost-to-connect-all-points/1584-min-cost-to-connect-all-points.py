from  heapq import heappop, heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adjList = defaultdict(list)
        for i in range(len(points)):
            x1 , y1 = points[i]
            for j in range(i+1, len(points)):
                
                x2 , y2 = points[j]
                
                dis = abs(x2 - x1) + abs(y2 -y1)
                adjList[i].append((dis,j))
                adjList[j].append((dis,i))
        

        
        visited = set()
        minHeap = [ (0, 0 )]
        res = 0
        while minHeap:
            dis, src = heappop(minHeap)
            
            if src in visited:
                continue
                
            visited.add(src )
        
            res += dis
            
            for d,tar in adjList[src]:
                if tar not in visited:
                    heappush(minHeap, (d , tar )) 
                    
        return res
            
        