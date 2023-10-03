from collections import deque

class Solution:
    def isBipartite(self, V,graph):
            
        n, colored = len(graph), {}
        for i in range(n):
            if i not in colored :
                colored[i] = 1
                q = deque([i])
                while q:
                    cur = q.popleft()
                    for nb in graph[cur]:
                        if nb not in colored:
                            colored[nb] = -colored[cur]
                            q.append(nb)
                        elif colored[nb] == colored[cur]:
                            return False
        return True
        # color = {}
        # def dfs(pos):
        #     for i in graph[pos]:
        #         if i in color:
        #             if color[i] == color[pos]:
        #                 return False
        #         else:
        #             color[i] = 1 - color[pos]
        #             if not dfs(i):
        #                 return False
        #     return True
        # for i in range(len(graph)):
        #     if i not in color:
        #         color[i] = 0
        #         if not dfs(i):
        #             return False
        # return True
        #code here





#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends