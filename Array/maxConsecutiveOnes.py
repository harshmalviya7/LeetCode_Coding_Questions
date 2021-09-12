# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/
'''
Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = 0
        c = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c += 1

            else:

                c = 0
            a = max(a, c)
        return a
