from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        #create a adjacency list
        edges = defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w)) 
        
        minHeap = [ (0,k) ] 
        time = 0
        visited = set()
        
        while minHeap:
            weight_S, source = heapq.heappop(minHeap)
            if source in visited:
                continue
            
            visited.add(source)
            time = max(time,weight_S)

            for target, weight_T  in edges[source]:
                if target not in visited:
                    heapq.heappush(minHeap, (weight_S + weight_T , target))
                    
        return time  if len(visited) == n else -1

            
            
            
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        