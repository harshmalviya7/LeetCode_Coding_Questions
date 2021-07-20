
# 1832. Check if the Sentence Is Pangram
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence))==26
        # l=[0]*26
        # for i in sentence:
        #     l[ord(i)-ord("a")]=1
        # return True if sum(l)==26 else False