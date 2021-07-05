
# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set()
        l = []
        for i in nums:
            if i in s:
                l.append(i)
            else:
                s.add(i)
        return l
