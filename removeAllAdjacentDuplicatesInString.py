# 1047. Remove All Adjacent Duplicates In String
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
class Solution:
    def removeDuplicates(self, s: str) -> str: l=[s[0]]
        for i in range(1,len(s)):
            if len(l) and s[i]==l[-1] :

                l.pop(-1)
            else:
                l.append(s[i])
        return "".join(l)




