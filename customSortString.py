# 791. Custom Sort String
# https://leetcode.com/problems/custom-sort-string/

class Solution:
    def customSortString(self, order: str, str: str) -> str:

        l = [0] * 26
        for i in range(len(order)):
            l[ord(order[i]) - ord("a")] = 1
        s1 = ""
        for i in str:
            if l[ord(i) - ord("a")] != 0:
                l[ord(i) - ord("a")] += 1
            else:
                s1 += i
        s2 = ""
        for i in order:
            s2 += i * (l[ord(i) - ord("a")] - 1)

        print(s2)
        return s2 + s1
