# 268. Missing Number
# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        sm_expecte d =len(nums ) *(len(nums ) +1 )/ /2
        actua l =sum(nums)




        return sm_expecte d -actual

