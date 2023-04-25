

class Solution:
    def __init__(self):
        self.ans = inf
        
    def bfs(self, src: int, adj: List[List[int]], n: int) -> None:
        distance = [inf] * n
        parent = [-1] * n
        
        q = deque()
        distance[src] = 0
        q.append(src)
        
        while  q:
            node = q.popleft()
            for neigh in adj[node]:
                if distance[neigh] == inf:
                    distance[neigh] = 1 + distance[node]
                    parent[neigh] = node
                    q.append(neigh)
                elif parent[node] != neigh and parent[neigh] != node:
                    self.ans = min(self.ans, distance[neigh] + distance[node] + 1)
                
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        for i in range(n):
            self.bfs(i, adj, n)
            
        if self.ans == inf:
            return -1
        
        return self.ans
