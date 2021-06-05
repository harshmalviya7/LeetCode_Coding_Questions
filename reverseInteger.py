# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:

        def no(x): a=0
            while(x>0):
                a=a*10+x%10

                x=x//10

            return 0 if a> 0x7fffffff else a

        if x<0:
            return -1*no(abs(x))
        else:
            return no(x)
