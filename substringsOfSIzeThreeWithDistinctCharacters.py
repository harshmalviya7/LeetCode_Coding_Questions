# 1876. Substrings of Size Three with Distinct Characters
# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c = 0
        for i in range(len(s) - 2):
            if len(set(s[i:i + 3])) == 3:
                c += 1
        return c
        # a=0
        # for i in range(len(s)-2):
        #     print(i)
        #     if s[i]==s[i+1] or s[i+1]==s[i+2] or s[i]==s[i+2]:
        #         continue
        #     a+=1
        # return a


