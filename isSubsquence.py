# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_l = len(s)
        t_l = len(t)
        if s_l > t_l:
            return False
        if s_l == t_l:
            return s == t
        i, j = 0, 0

        while (i < s_l and j < t_l):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == s_l

#         def make(s,t,i,j):
#             if i==0:
#                 return True
#             if j==0:
#                 return False
#             if s[i-1]==t[j-1]:
#                 return make(s,t,i-1,j-1)
#             else:
#                 return make(s,t,i,j-1)


#         return make(s,t,len(s),len(t))





