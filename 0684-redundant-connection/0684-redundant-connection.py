class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range( len(edges)+1 )]
        rank = [ 1 ] * (len(edges) + 1)
        
        
        def find(n):
            p = parent[n]
            while p != parent[p]:
                p = parent[p]
            return p
        
        def union(u,v):
            u , v = find(u) , find(v)
            if u == v: return False
            
            elif rank[u] >= rank[v]:
                parent[v] = u
                rank[u] += rank[v]
            else:
                parent[u] = v
                rank[v] = rank[u]
            return True
                
        
        for u,v in edges:
            #print(f'{parent} \n{rank}')
            if not union(u,v):
                return [u,v]
        