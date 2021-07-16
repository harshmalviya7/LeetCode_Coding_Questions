# 611. Valid Triangle Number
# https://leetcode.com/problems/valid-triangle-number/
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        a=0
        for i in range(len(nums)-1,1,-1):
            l=0
            h=i-1
            while(l<h):
                if nums[l]+nums[h]>nums[i]:
                    a=a+h-l
                    h-=1
                else:
                    l+=1
        return a