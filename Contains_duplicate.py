# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # a = set()
        # for i in nums:
        #     if i in a:
        #         return True
        #     else:
        #         a.add(i)
        # return False

        d={}
        for i in nums:
            if i in d: return True
            else:d[i]=1
        return False
ob=Solution()
print(ob.containsDuplicate([1,2,3,4]))