# 565. Array Nesting
# https://leetcode.com/problems/array-nesting/
'''
Example 1:

Input: nums = [5,4,0,3,1,6,2]
Output: 4
Explanation:
nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
One of the longest sets s[k]:
s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}
'''
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] != float("inf"):
                start = nums[i]
                c = 0
                while (nums[start] != float("inf")):
                    temp = start
                    start = nums[start]
                    c += 1
                    nums[temp] = float('inf')

                res = max(res, c)
        return res
