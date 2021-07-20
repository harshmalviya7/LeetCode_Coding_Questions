
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# 1614. Maximum Nesting Depth of the Parentheses
class Solution:
    def maxDepth(self, s: str) -> int:
        a = 0
        res = 0
        for i in s:
            if i == "(":
                a += 1
            elif i == ")":
                res = max(a, res)
                a -= 1
        return res
