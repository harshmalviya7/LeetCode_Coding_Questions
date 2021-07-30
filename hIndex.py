# 274. H-Index
# https://leetcode.com/problems/h-index/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        n = len(citations)
        citations.sort(reverse=True)
        for i in range(n):
            if citations[i] <= i:
                return i
        return len(citations)
