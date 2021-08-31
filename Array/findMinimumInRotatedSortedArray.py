# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""
Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        if nums[i] <= nums[j]:
            return nums[0]
        while (i <= j):
            mid = i + (j - i) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                i = mid + 1
            else:
                j = mid - 1
        # while(i<=j):
        #     mid=i+(j-i)//2
        #     nextt=(mid+1)%n
        #     prev=(mid+n-1)%n
        #     if nums[prev]<=nums[mid] and nums[mid]>=nums[nextt]:
        #         return nums[mid+1]
        #     elif nums[i]<=nums[mid]:
        #         i=mid+1
        #     else:
        #         j=mid-1
