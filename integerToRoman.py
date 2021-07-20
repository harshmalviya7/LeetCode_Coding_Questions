# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D",
             900: "CM", 1000: "M"}
        l = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        s = ""
        for i in range(len(l) - 1, -1, -1):
            while (num >= l[i]):
                num -= l[i]
                s += d[l[i]]
        return (s)
