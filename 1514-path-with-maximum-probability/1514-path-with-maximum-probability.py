class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adjList  = defaultdict(list)
        

        minHeap = [ (-1, start )]
        visited = set() 
        
        for edge,p in zip(edges,succProb):
            adjList[edge[0]].append( (edge[1],p))
            adjList[edge[1]].append((edge[0],p))
            
            
        while minHeap:
            ps , s  = heapq.heappop(minHeap) 
            
            visited.add(s)
            if s == end:
                return abs(ps)
                    
            for t,pt in adjList[s]:
                if t not in visited:
                    heapq.heappush(minHeap, ( pt*ps , t ) )
                    
        return 0
        
        
        