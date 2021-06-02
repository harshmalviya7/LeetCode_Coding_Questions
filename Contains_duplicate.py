# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = set()
        for i in nums:
            if i in a:
                return "true"
            else:
                a.add(i)
        return "false"

ob=Solution()
print(ob.containsDuplicate([1,2,3,4]))