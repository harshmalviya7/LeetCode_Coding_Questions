https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1#

class Solution:

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        visited = [False] * V
        order = [False] * V

        def isCyclic_util(src, visited, order, adj):

            visited[src] = True
            order[src] = True
            for k in adj[src]:
                if not visited[k]:
                    conf = isCyclic_util(k, visited, order, adj)
                    if conf:
                        return True
                elif order[k]:
                    return True
            order[src] = False
            return False

        for i in range(V):
            if not visited[i]:
                flag = isCyclic_util(i, visited, order, adj)
                if flag:
                    return True

        return False