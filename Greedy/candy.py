# 135. Candy
# https://leetcode.com/problems/candy/
"""Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions."""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        #         n=len(ratings)
        #         l=[1]*n

        #         for i in range(1,n):
        #             if ratings[i]>ratings[i-1]:
        #                 l[i]=l[i-1]+1
        #         c=0
        #         for i in range(n-2,-1,-1):
        #             if ratings[i]>ratings[i+1]:
        #                 l[i]=max(l[i],l[i+1]+1)
        #             c+=l[i]
        #         c+=l[n-1]
        #         return c
        n = len(ratings)
        l = [1] * n
        r = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                l[i] = l[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                r[i] = r[i + 1] + 1
        c = 0
        for i in range(n):
            c += max(r[i], l[i])
        return c


