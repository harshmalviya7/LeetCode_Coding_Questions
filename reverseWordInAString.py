# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:

        l = []
        k = ""
        for i in s:
            if i == " ":
                if k:
                    l.append(k)
                k = ""
            else:
                k += i
        if k:
            l.append(k)
        return (" ".join(l[::-1]))





