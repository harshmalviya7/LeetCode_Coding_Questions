# 462. Minimum Moves to Equal Array Elements II
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        median = nums[n // 2]
        ans = 0
        print(median)
        for i in nums:
            ans += abs(i - median)
        return ans
#         nums.sort()

#         n=len(nums)//2

#         res=nums[n]*n-sum(nums[:n])
#         print(res)
#         res2=sum(nums[n+1:])-nums[n]*(len(nums)-n-1)
#         print((len(nums)-n))
#         print(res2)
#         return abs(res)+abs(res2)


