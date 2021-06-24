# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        an s =[]

        def backtrack(s ,l ,r):
            if len(s )= = 2 *n:
                ans.append("".join(s))

            if l> 0:
                s.append("(")
                backtrack(s, l - 1, r)
                s.pop()
            if r > l:
                s.append(")")
                backtrack(s, l, r - 1)
                s.pop()

        backtrack([], n, n)
        return ans