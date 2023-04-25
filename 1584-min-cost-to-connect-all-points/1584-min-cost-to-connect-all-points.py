# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        
#         n, c = len(points), collections.defaultdict(list)
#         for i in range(n):
#             for j in range(i+1, n):
#                 d = manhattan(points[i], points[j])
#                 c[i].append((d, j))
#                 c[j].append((d, i))
        
#         cnt, ans, visited, heap = 1, 0, [0] * n, c[0]
#         visited[0] = 1
#         heapq.heapify(heap)
#         while heap:
#             d, j = heapq.heappop(heap)
#             if not visited[j]:
#                 visited[j], cnt, ans = 1, cnt+1, ans+d
#                 for record in c[j]: heapq.heappush(heap, record)
#             if cnt >= n: break        
#         return ans



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
        minHeap = [ ( 0, 0 )]
        res = 0
        while minHeap:
            dis, src = heappop(minHeap)
            
            if src not in visited:
                visited.add(src )
                res += dis
                for d,tar in adjList[src]:
                    if tar not in visited:
                        heappush(minHeap, (d , tar )) 
                        
            if len(visited) >= len(points):
                return res
                    
  