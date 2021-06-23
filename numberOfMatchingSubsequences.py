# 792. Number of Matching Subsequences
# https://leetcode.com/problems/number-of-matching-subsequences/
class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """


        def search(word):
            po s =-1
            for i in word:
                if i not in d:
                    return False

                inde x =bisect_right(d[i] ,pos)
                if inde x= =len(d[i]):
                    return False
                po s =d[i][index]

            return True d=defaultdic t(list)
        for i,j in enume rate(s):
            d[j].append(i)
        ans=0 for word in words:
            if search(word):
                ans+=1
        return ans