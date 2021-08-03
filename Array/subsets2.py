# 90. Subsets II
# https://leetcode.com/problems/subsets-ii/
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            return res
        nums.sort()

        def helper(i, curr, nums):
            res.append(curr.copy())
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                curr.append(nums[j])
                helper(j + 1, curr, nums)
                curr.pop()

        helper(0, [], nums)
        return res

