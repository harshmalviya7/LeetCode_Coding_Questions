# 1464. Maximum Product of Two Elements in an Array
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/


import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = []
        for i in nums:
            heapq.heappush(l, -i)

        return (-heapq.heappop(l) - 1) * (-heapq.heappop(l) - 1)