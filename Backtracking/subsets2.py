# https://leetcode.com/problems/subsets-ii/
# 90. Subsets II
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def helper(i, curr):
            a.append(list(curr))
            for j in range(i, len(nums)):
                if j != i and nums[j] == nums[j - 1]:
                    continue
                curr.append(nums[j])
                helper(j + 1, curr)
                curr.pop()

        nums.sort()
        a = []
        helper(0, [])
        return a

#         res=[]
#         if len(nums)==0:
#             return res
#         nums.sort()
#         def helper(i,curr,nums):
#             res.append(curr.copy())
#             for j in range(i,len(nums)):
#                 if j>i and nums[j]==nums[j-1]:
#                     continue
#                 curr.append(nums[j])
#                 helper(j+1,curr,nums)
#                 curr.pop()
#         helper(0,[],nums)
#         return res

