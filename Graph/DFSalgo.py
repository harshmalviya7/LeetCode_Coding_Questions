class Solution:

    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited = [False] * V

        def solve(src, visited, adj):
            visited[src] = True
            l.append(src)
            for i in adj[src]:
                if not visited[i]:
                    solve(i, visited, adj)

        l = []
        solve(0, visited, adj)
        return l
ob=Solution()
V=5
adj={0:[1,2,3],1:[0],2:[4,0],3:[0],4:[2]}

print(ob.dfsOfGraph(V,adj)) # [0, 1, 2, 4, 3]