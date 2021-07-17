# 18. 4Sum
# https://leetcode.com/problems/4sum/
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        res = []
        n = len(nums)
        nums.sort()
        for i in range(0, n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                a = target - (nums[i] + nums[j])
                l = j + 1
                h = n - 1
                while (l < h):

                    if nums[l] + nums[h] == a:
                        print(res)
                        res.append([nums[i], nums[j], nums[l], nums[h]])

                        while (l < h and nums[l] == nums[l + 1]):
                            l += 1
                        while (l < h and nums[h] == nums[h - 1]):
                            h -= 1
                        l += 1
                        h -= 1
                    elif nums[l] + nums[h] > a:
                        h -= 1
                    else:
                        l += 1

        return res
