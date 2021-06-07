# 27. Remove Element
# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:


        inde x =0 a=len(nums )
        for i in range(a):
            if nums[i]!=val:
                nums[index]=nums[i]
                index+=1
        return index


