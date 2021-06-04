# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/



class Solution:
    def firstUniqChar(self, s: str) -> int: d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=i
            else:
                d[s[i]]=-1
        for i in d:
            if d[i]!=-1:
                return d[i]
        return -1



