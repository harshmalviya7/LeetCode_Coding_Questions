# 1371. Find the Longest Substring Containing Vowels in Even Counts
# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        m = 0
        ans = 0
        # d={'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        d = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        seen = {0: -1}
        for i in range(len(s)):
            if s[i] in d:
                m ^= d[s[i]]
            if m not in seen:
                seen[m] = i
            ans = max(ans, i - seen[m])
        return ans
