# 506. Relative Ranks
# https://leetcode.com/problems/relative-ranks/
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        import heapq
        h = []
        for i in score:
            heapq.heappush(h, -i)
        l = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        d = {}

        for i in range(len(score)):
            if i < 3:
                d[-heapq.heappop(h)] = l[i]
            else:
                d[-heapq.heappop(h)] = str(i + 1)

        print(d)
        return [d[i] for i in score]


