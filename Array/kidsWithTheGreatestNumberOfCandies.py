# 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        l=[False]*len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=m:
                l[i]=True
        return l