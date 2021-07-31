
# 1748. Sum of Unique Elements
# https://leetcode.com/problems/sum-of-unique-elements/
from collections import Counter


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        # d=Counter(nums)
        s = 0
        for i, j in d.items():
            if j == 1:
                s += i
        return s