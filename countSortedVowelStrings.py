# 1641. Count Sorted Vowel Strings
# https://leetcode.com/problems/count-sorted-vowel-strings/
class Solution:
    def countVowelStrings(self, n: int) -> int:
        s = [1] * 5
        for i in range(2, n + 1):
            for i in range(3, -1, -1):
                s[i] += s[i + 1]

        return sum(s)

