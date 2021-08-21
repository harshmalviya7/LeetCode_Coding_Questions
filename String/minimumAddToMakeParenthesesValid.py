# 921. Minimum Add to Make Parentheses Valid
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans=bal=0
        for i in s:
            bal+=1 if i=="(" else -1
            if bal==-1:
                ans+=1
                bal+=1
        return ans + bal