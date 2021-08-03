# 78. Subsets
# https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            return res

        def helper(i, curr, nums):
            res.append(curr.copy())
            for j in range(i, len(nums)):
                curr.append(nums[j])
                helper(j + 1, curr, nums)
                curr.pop()

        helper(0, [], nums)

        return res

        # out=[[]]
#         for i in nums:
#             out+=[lst + [i] for lst in out]
#         return (out)