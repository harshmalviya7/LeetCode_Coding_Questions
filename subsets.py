# 78. Subsets
# https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        for i in nums:
            out += [lst + [i] for lst in out]
        return (out)