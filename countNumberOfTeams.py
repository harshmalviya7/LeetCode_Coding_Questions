# 1395. Count Number of Teams
# https://leetcode.com/problems/count-number-of-teams/
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0

        for i in range(1, len(rating) - 1):
            inc1 = inc2 = dec1 = dec2 = 0
            for j in range(0, len(rating)):

                if i > j:
                    if rating[j] < rating[i]:
                        inc1 += 1
                    else:
                        dec1 += 1
                if j > i:
                    if rating[j] > rating[i]:
                        inc2 += 1
                    else:
                        dec2 += 1

            res += inc1 * inc2 + dec1 * dec2

        print(res)
        return res

