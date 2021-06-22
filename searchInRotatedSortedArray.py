# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        def minIndex(nums, l, r):
            while (l <= r):
                mid = l + (r - l) // 2
                if nums[mid] >= nums[0]:

                    l = mid + 1
                else:
                    r = mid - 1
            return l

        def binarysearch(arr, target):
            l = 0
            r = len(arr) - 1
            while (l <= r):
                mid = l + (r - l) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        minno = minIndex(nums, 0, len(nums) - 1)
        x = binarysearch(nums[minno:], target)
        if x != -1:
            return minno + x
        y = binarysearch(nums[:minno], target)
        if y != -1:
            return y
        return -1
