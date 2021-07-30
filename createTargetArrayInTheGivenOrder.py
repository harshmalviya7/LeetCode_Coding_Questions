# 1389. Create Target Array in the Given Order
# https://leetcode.com/problems/create-target-array-in-the-given-order/
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        t = []
        for i in range(len(nums)):
            t.insert(index[i], nums[i])

        return t
