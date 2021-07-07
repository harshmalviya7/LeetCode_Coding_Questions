# 459. Repeated Substring Pattern
# https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:


        res = ""
        n = len(s)
        for i in range(n // 2):
            res += s[i]
            if n % len(res) == 0:
                if res * (n // len(res)) == s:
                    return True
        return False

