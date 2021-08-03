# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        count = Counter(nums)
        l = []
        for i in count:

            heapq.heappush(l, (count[i], i))
            if len(l) > k:
                heapq.heappop(l)
        n = []
        while (l):
            n.append(heapq.heappop(l)[1])
        return n

#         count=Counter(nums)
#         return heapq.nlargest(k,count.keys(),key=count.get)

