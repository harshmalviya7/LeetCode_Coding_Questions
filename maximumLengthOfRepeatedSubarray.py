
# 718. Maximum Length of Repeated Subarray
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        m = [[0 for i in range(len(nums2) + 1)] for j in range(len(nums1) + 1)]
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):

                if nums1[i] == nums2[j]:
                    m[i][j] = 1 + m[i + 1][j + 1]

        return max(max(row) for row in m)
