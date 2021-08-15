# https://leetcode.com/problems/relative-sort-array/
# 1122. Relative Sort Array

from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        d1 = Counter(arr1)

        l = []
        for i in (arr2):
            l += [i] * d1[i]
            del d1[i]

        for i in sorted(d1):
            l += [i] * d1[i]

        return l