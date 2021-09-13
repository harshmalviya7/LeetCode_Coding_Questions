# 1189. Maximum Number of Balloons
# https://leetcode.com/problems/maximum-number-of-balloons/
'''
Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
'''

from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d=Counter(text)
        res=["b","a","n"]
        c=d["b"]
        for i in res:
            if i in d:
                c=min(c,d[i])
            else:
                return 0
        c=min(d["l"]//2,d["o"]//2,c)
        return c