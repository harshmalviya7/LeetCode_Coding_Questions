# 1935. Maximum Number of Words You Can Type
# https://leetcode.com/problems/maximum-number-of-words-you-can-type/
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        a = 0
        q = 0
        for i in text:
            print(i)
            for j in brokenLetters:
                if j in i:
                    q = 1
                    break
            if q:
                q = 0
                continue
            a += 1

            print(a)
        return a