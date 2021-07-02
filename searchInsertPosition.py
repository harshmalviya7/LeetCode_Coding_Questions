# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while (l <= r):
            mid = l + (r - l) // 2
            if nums[mid] >= target and nums[mid - 1] < target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
                print(l)
            else:
                r = mid - 1

        if l == len(nums):
            return len(nums)
        else:
            return 0

