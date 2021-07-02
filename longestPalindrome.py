from collections import defaultdict

# 409. Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/
class Solution:
    def longestPalindrome(self, s: str) -> int:

        d = defaultdict(int)
        for i in s:
            d[i] += 1
        s = 0
        l = 0
        for i, j in d.items():
            l += j // 2
            if j % 2 != 0:
                s = 1

        return l * 2 + s
