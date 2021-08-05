# 674. Longest Continuous Increasing Subsequence
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # runtime beats 83.53 % of python3 submissions.
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                dp[i] = dp[i - 1] + 1
        return max(dp)

# runtime beats 98.59 % of python3 submissions
# if len(nums)==0 or len(nums)==1:
#     return len(nums)
# i=0
# c=1
# res=1
# while(i<len(nums)-1):
#     if nums[i]<nums[i+1]:
#         c+=1
#     else:
#         c=1
#     res=max(res,c)
#     i+=1
# return res