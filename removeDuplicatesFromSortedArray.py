# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution(object):
    def removeDuplicates(self, nums):

        if len(nums )= =0:
            return 0 j=1
        for i in range(len(nums)-1):

            if nums[i]!=nums[i +1 ]:

                nums[j]=
                nums[i+1]
                j+=1
        return j

