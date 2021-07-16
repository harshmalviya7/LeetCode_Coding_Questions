# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

