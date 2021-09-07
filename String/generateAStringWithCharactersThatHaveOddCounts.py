# 1374. Generate a String With Characters That Have Odd Counts
# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
class Solution:
    def generateTheString(self, n: int) -> str:
        a = "a"
        b = "b"
        if n % 2 == 0:
            return a + b * (n - 1)
        return a * (n)