# 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result=nums[0]+nums[1]+nums[len(nums)-1]
        nums.sort()
        for i in range(len(nums)-2):
            a=i+1
            b=len(nums)-1
            while(a<b):
                current=nums[i]+nums[a]+nums[b]
                if current >target:
                    b-=1
                else:
                    a+=1
                if abs(current-target)<abs(result-target):
                    result=current
            if result-target==0:
                break
        return result