# 896. Monotonic Array
# https://leetcode.com/problems/monotonic-array/
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        in c =True
        de c =True

        for i in range(len(nums ) -1):
            if nums[i ] >nums[ i +1]:
                in c =False
            if nums[i ] <nums[ i +1]:
                de c =False

        return inc or dec

