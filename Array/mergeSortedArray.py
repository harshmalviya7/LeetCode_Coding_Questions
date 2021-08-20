# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
import heapq
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l = []
        for i in range(m):
            heapq.heappush(l, nums1[i])
        for i in nums2:
            heapq.heappush(l, i)

        for i in range(len(nums1)):
            nums1[i] = heapq.heappop(l)

