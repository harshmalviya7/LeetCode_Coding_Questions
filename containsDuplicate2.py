# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool: d={}

        for i in range(len(nums)):
            if nums[i] in d:



                if abs(i- d[nums[i]])<=k:
                    return True
            d[nums[i]]=i
