from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        #adjacency list
        edges = defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))
        
        minHeap = [ (0,k) ]
        visited = set()
        time = 0
        
        while minHeap:
            weightS , source = heapq.heappop(minHeap)
            if source in visited:
                continue
            
            visited.add(source)
            time = max(time,weightS)
            for target, weightT in edges[ source]:
                if target not in visited:
                    heapq.heappush(minHeap , (weightT+weightS , target))
        
        return time if len(visited) == n else -1
                    
                
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        