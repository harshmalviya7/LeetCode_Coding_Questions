# 1985. Find the Kth Largest Integer in the Array
# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        l = []
        for i in nums:
            heapq.heappush(l, int(i))
            if len(l) > k:
                heapq.heappop(l)

        return str(heapq.heappop(l))
