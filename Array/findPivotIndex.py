# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        p=sum(nums)
        leftsum=0
        for i in range(0,len(nums)):
            p-=nums[i]
            if p==leftsum:
                return i
            leftsum+=nums[i]
        return -1