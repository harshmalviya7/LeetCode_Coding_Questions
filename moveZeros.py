# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        a = 0
        for i in range(len(nums)):

            if nums[i] != 0:
                # nums[a]=nums[i]
                # a+=1
                nums[i], nums[a] = nums[a], nums[i]
                a += 1
        # for i in range(a,len(nums)):
        #     nums[i]=0

    # uncomment for 2 method
