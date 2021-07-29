from collections import deque


class Solution:

    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):

        visited = [False] * V
        q = deque()
        q.append(0)
        visited[0] = True
        arr = []
        while q:
            temp = q.popleft()

            arr.append(temp)

            for i in adj[temp]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
        return arr

ob=Solution()
V=5
adj={0:[1,2,3],1:[0],2:[4,0],3:[0],4:[2]}
print(ob.bfsOfGraph(V,adj)) #[0, 1, 2, 3, 4]
    #
    #     0
    # /    |   \
    # 1    2    3
    #      |
    #      4
