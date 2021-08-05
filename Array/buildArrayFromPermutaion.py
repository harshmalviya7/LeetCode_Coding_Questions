# 1920. Build Array from Permutation
# https://leetcode.com/problems/build-array-from-permutation/
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            l.append(nums[i])
        return l
