# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if not nums:
            return nums
        # l=[]
        # for i in nums:
        #     heappush(l,i)
        #     if len(l)>k:
        #         heappop(l)
        # return heappop(l)

        l = []
        for i in nums:
            heappush(l, -i)
        while k:
            if k == 1:
                return -heappop(l)
            heappop(l)
            k -= 1

        # return heapq.nlargest(k, nums).pop()

        # return sorted(nums)[-k]

