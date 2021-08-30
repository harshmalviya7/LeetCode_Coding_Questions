# 503. Next Greater Element II
# https://leetcode.com/problems/next-greater-element-ii/
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        m = [0] * len(nums)
        stack = []
        for i in range(len(nums) * 2 - 1, -1, -1):
            while stack and nums[i % len(nums)] >= stack[-1]:
                stack.pop()

            if i < len(nums):
                m[i] = stack[-1] if stack else -1
            stack.append(nums[i % len(nums)])

        return m