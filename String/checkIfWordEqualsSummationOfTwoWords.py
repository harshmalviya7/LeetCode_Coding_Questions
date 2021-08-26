# 1880. Check if Word Equals Summation of Two Words
# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a=b=""
        for i in firstWord:
            a+=str(ord(i)-ord("a"))
        for j in secondWord:
            b+=str(ord(j)-ord("a"))
        a=int(a)+int(b)
        b=""
        for j in targetWord:
            b+=str(ord(j)-ord("a"))
        print(a,b)
        if a==int(b):
            return True
        return False