# 1209. Remove All Adjacent Duplicates in String II
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) == 0 or len(s) == 1:
            return s
        l = []

        for i in range(len(s)):
            if l and l[-1][0] == s[i]:
                l[-1][1] += 1
                if l[-1][1] == k:
                    l.pop()
            else:
                l.append([s[i], 1])

        return "".join([i * j for i, j in l])

