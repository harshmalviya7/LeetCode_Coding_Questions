# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """ d={"I":1," V":5, "X ":10 ," L":5 0," C":1 00, "D": 500, "M": 1000 }
        a=d[s[0]]
        for i in range(1,len(s)):
            if d[s[i]]>d[s[i-1 ] ]:
                a=a+(d[s[ i ] ] -d[s[i-1 ] ])-d[ s [i-1 ] ]
            else:
                a+=d[s[i] ]

        return a
