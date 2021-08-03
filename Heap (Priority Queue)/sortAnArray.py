# 912. Sort an Array
# https://leetcode.com/problems/sort-an-array/
import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        l = []
        while (nums):
            l.append(heapq.heappop(nums))
        return l

        # return sorted(nums)