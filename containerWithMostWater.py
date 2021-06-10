# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:

        a = 0
        i = 0
        j = len(height) - 1
        while (i < j):

            b = min(height[i], height[j])
            a = max(a, b * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return a
