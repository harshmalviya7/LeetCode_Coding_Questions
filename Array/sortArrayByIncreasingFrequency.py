# 1636. Sort Array by Increasing Frequency
# https://leetcode.com/problems/sort-array-by-increasing-frequency/
from collections import Counter  # , defaultdict
# import heapq
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        #         l=[]

        c = Counter(nums)
        #         print(c)
        #         for i in nums:
        #             heappush(l,(c[i],-i))
        #         res=[]
        #         while(l):
        #             res.append(-heappop(l)[1])
        #         return (res)

        return sorted(nums, key=lambda x: (c[x], -x))

