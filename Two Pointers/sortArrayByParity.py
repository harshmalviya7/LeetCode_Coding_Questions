# 905. Sort Array By Parity
# https://leetcode.com/problems/sort-array-by-parity/


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while (i < j):

            while (i < j and nums[i] % 2 == 0):
                i += 1

            while (i < j and nums[j] % 2 != 0):
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        return nums