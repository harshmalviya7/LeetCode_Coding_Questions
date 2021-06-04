# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                d[s[i]] = -1
        min_no = 100000
        for i in d:
            if d[i] != -1 and d[i] < min_no:
                min_no = d[i]
        return -1 if min_no == 100000 else min_no


ob=Solution()
