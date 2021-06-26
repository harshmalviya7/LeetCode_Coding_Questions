# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: p=""
        for i in zip(*strs):
            if len(set(i))==1:
                p+=i[0]
            else:
                return p
        return p