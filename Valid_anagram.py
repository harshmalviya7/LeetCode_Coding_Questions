# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l = [0 for i in range(26)]

        for i in range(len(s)):
            l[ord(s[i]) - ord('a')] += 1
            l[ord(t[i]) - ord('a')] -= 1

        for i in l:
            if i != 0:
                return 0

        return 1

ob=Solution()
print(ob.isAnagram("rat", "car"))