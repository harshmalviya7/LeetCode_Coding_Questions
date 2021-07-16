# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        l = []
        for i in stones:
            heapq.heappush(l, -i)

        while (len(l) >= 2):
            a = heapq.heappop(l)
            b = heapq.heappop(l)
            print(a, b)

            if a != b:
                heapq.heappush(l, a - b)

        return 0 if not l else -l.pop()

