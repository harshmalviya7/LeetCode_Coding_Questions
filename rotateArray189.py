# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def rotate_l(nums, l, r):
            while (l < r):
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        l = len(nums)
        k %= l
        rotate_l(nums, 0, l - k - 1)
        rotate_l(nums, l - k, l - 1)
        rotate_l(nums, 0, l - 1)