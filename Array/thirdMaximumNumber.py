# 414. Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/
class Solution:
    def thirdMax(self, arr: List[int]) -> int:
        arr = set(arr)
        arr = list(arr)
        arr.sort()
        return arr[-3] if len(arr) >= 3 else arr[-1]

