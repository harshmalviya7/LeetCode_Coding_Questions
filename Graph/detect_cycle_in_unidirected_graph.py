# Detect cycle in an undirected graph
# https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
class Solution:

    # Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):

        visited = [False] * V

        def dfs(src, par, adj, visited):
            visited[src] = True
            for i in adj[src]:
                if not visited[i]:
                    if dfs(i, src, adj, visited):
                        return True
                elif i != par:
                    return True
            return False

        for i in range(V):
            if not visited[i]:
                if dfs(i, -1, adj, visited):
                    return True
        return False