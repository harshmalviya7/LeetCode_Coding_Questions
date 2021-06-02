# 231. Power of Two
# https://leetcode.com/problems/power-of-two/


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 1
        while (i < n):
            i *= 2
        return i == n

ob=Solution()
num=3
print(ob.isPowerOfTwo(num))
