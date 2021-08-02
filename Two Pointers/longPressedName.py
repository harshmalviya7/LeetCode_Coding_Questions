# 925. Long Pressed Name
# https://leetcode.com/problems/long-pressed-name/
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(name)
        m = len(typed)

        if m < n:
            return False
        i = j = 0
        while (True):
            print(i, j)
            if i == n and j == m:
                return True

            if i < n and j < m and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and j < m and typed[j - 1] == typed[j]:

                j += 1
            else:
                return False
