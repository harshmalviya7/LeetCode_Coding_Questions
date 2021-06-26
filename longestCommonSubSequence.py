# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: a=len(text1)
        b=len(text2 )
        m=[[0 ]*(b+ 1 ) fr j i n range(a+1)]

        for i in range(1,a+1):
            for j in range(1,b+1):


                if text1[i-

                1]= = text2[j-1]: m[i][j]=1+m[i-1][j-1]

                else:
                    m[i][j]=max(m[i-1][j ] ,m[i][j - 1]) return m[i][j]
