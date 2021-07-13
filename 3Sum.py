# 15. 3Sum
# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        li = []
        if not nums:
            return None
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while (l < r):
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    a = [nums[i], nums[l], nums[r]]
                    if a not in li:
                        li.append(a)
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                if s < 0:
                    l += 1
                else:
                    r -= 1
        return (li)