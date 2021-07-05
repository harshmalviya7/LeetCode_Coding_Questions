# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a, b = len(p), len(s)
        if a > b:
            return []
        res1, res2 = [0 for _ in range(26)], [0 for _ in range(26)]
        r = 0
        while (r < a):
            res1[ord(p[r]) - ord("a")] += 1
            res2[ord(s[r]) - ord("a")] += 1
            r += 1

        r -= 1
        l = 0
        i=[]
        while (r < b):
            if res1 == res2:
                i.append(l)
            r += 1
            if r != b:
                res2[ord(s[r]) - ord("a")] += 1
            res2[ord(s[l]) - ord("a")] -= 1
            l += 1

        return i
ob=Solution()
ob.findAnagrams("abab", "ab")