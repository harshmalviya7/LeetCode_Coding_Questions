# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        res = 1
        for i in range(1, len(nums)):
            res *= nums[i - 1]
            left.append(res)

        right = [1] * len(nums)
        res = 1
        for i in range(len(nums) - 2, -1, -1):
            res *= nums[i + 1]
            right[i] = res

        return [i * j for i, j in zip(left, right)]