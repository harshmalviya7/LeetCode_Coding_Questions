# 645. Set Mismatch
# https://leetcode.com/problems/set-mismatch/
from collections import defaultdict
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
            if d[i]==2:
                c=i
        for i in range(1,len(nums)+1):
            if i not in d:
                return [c,i]
