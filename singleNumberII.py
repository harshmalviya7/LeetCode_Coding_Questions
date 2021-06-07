# 137. Single Number II
# https://leetcode.com/problems/single-number-ii/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        #         count=collections.Counter(nums)
        #         for i,j in count.items():
        #             if j!=3:
        #                 return i

        return ( 3 *sum(set(nums) ) -sum(nums) )/ /2
