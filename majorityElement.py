# 169. Majority Element
# https://leetcode.com/problems/majority-element/

import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #         d=collections.defaultdict(int)
        # 1
        #         for i in nums:
        #             d[i]+=1
        #             if d[i]>(len(nums)//2):
        #                 return i

        # 2
        # return sorted(nums)[len(nums)//2]

        # 3
        count = collections.Counter(nums)
        return max(count.keys(), key=count.get)