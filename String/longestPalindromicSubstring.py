
# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def helper(l, r, s):
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l + 1:r]

        for i in range(len(s)):
            temp = helper(i, i, s)
            if len(temp) > len(res):
                res = temp
            print("k", temp)
            temp = helper(i, i + 1, s)
            if len(temp) > len(res):

        return res


