# 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        #         s=set(nums1)
        #         t=set(nums2)

        #         return s.intersection(t)
        set1 = set(nums1)
        set2 = set(nums2)
        inter = []
        for num in set1:
            if num in set2:
                inter.append(num)
        return inter