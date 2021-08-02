# 942. DI String Match
# https://leetcode.com/problems/di-string-match/
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        k = 0
        j = len(s)
        l = []
        for i in s:

            if i == "I":
                l.append(k)
                k += 1
            else:
                l.append(j)
                j -= 1

        return l + [k]


