# 38. Count and Say
# https://leetcode.com/problems/count-and-say/
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = "11"
        if n == 2:
            return s

        for i in range(3, n + 1):
            s += "@"
            c = 1
            a = ""
            for j in range(1, len(s)):
                if s[j] == s[j - 1]:
                    c += 1
                else:
                    a += str(c)
                    a += s[j - 1]
                    c = 1

            s = a

        return (s)

