# https://leetcode.com/problems/sorting-the-sentence/
# 1859. Sorting the Sentence

class Solution:
    def sortSentence(self, s: str) -> str:
        l=s.split()
        res=[0]*len(l)
        for i in l:
            print(i[-1])
            res[int(i[-1])-1]=i[:-1]
        print(res)
        return " ".join(res)