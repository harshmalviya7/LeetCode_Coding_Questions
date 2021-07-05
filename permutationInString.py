# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a, b = len(s1), len(s2)
        if a > b:
            return False
        res1, res2 = [0 for _ in range(26)], [0 for _ in range(26)]
        r = 0
        while (r < a):
            res1[ord(s1[r]) - ord("a")] += 1
            res2[ord(s2[r]) - ord("a")] += 1
            r += 1

        r -= 1
        l = 0
        while (r < b):
            if res1 == res2:
                return True
            r += 1
            if r != b:
                res2[ord(s2[r]) - ord("a")] += 1
            res2[ord(s2[l]) - ord("a")] -= 1
            l += 1

        return False

