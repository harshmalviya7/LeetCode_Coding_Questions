# 136. Single Number leetcode
# https://leetcode.com/problems/single-number/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #         d={}
        #         for i in nums:
        #             if i in d:
        #                 d[i]=d[i]+1
        #             else:
        #                 d[i]=1

        #         for i in d:
        #             if d[i]==1:
        #                 return i

        # run time 144ms

        a = set()
        for i in nums:
            if i in a:
                a.remove(i)
            else:
                a.add(i)
        for i in a:
            return i

        # run time 124ms

ob=Solution()
nums=[4,1,2,1,2]
print(ob.singleNumber(nums))