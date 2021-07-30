# 1365. How Many Numbers Are Smaller Than the Current Number
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = sorted(nums)

        d = {}
        for i in range(len(l)):
            if l[i] not in d:
                d[l[i]] = i
        a = []
        for i in nums:
            a.append(d[i])
        print(a)
        return a