# 316. Remove Duplicate Letters
# 1081. Smallest Subsequence of Distinct Characters
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        d = {}
        for i in range(len(s)):
            d[s[i]] = i
        print(d)
        l = []
        for i in range(len(s)):

            if s[i] not in l:
                while l and l[-1] > s[i] and d[l[-1]] > i:
                    l.pop()
                l.append(s[i])

        return "".join(l)