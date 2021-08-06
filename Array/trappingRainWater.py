# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)

        left = []

        n = height[0]
        for i in height:
            if n < i:
                n = i
            left.append(n)

        n = height[-1]
        right = [0] * l
        maxi = -876543
        for i in range(l - 1, -1, -1):
            right[i] = max(maxi, height[i])
            maxi = right[i]

        res = 0
        for i in range(l):
            res += min(left[i], right[i]) - height[i]

        return res