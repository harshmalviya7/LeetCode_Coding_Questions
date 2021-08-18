# 561. Array Partition I
# https://leetcode.com/problems/array-partition-i/
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        for i in range(0, len(nums), 2):
            s += nums[i]
        return s