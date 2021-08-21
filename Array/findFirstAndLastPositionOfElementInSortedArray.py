# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        ans = -1

        # left bound
        while (l <= r):
            mid = l + (r - l) // 2
            if nums[mid] == target:
                ans = mid
                r = mid - 1
            elif nums[mid] > target:

                r = mid - 1
            else:

                l = mid + 1
        if ans == -1:
            return [-1, -1]
        res = [ans]

        # right bound
        l = 0
        r = len(nums) - 1
        while (l <= r):
            mid = l + (r - l) // 2
            if nums[mid] == target:
                ans = mid
                l = mid + 1
            elif nums[mid] > target:

                r = mid - 1
            else:

                l = mid + 1
        res.append(ans)
        return res


