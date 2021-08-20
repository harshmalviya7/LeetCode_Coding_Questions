# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        d = defaultdict(int)
        for i in nums1:
            d[i] += 1
        for j in nums2:
            if d[j] > 0:
                res.append(j)
                d[j] -= 1
        return res

        # res=[]
        # i=0
        # j=0
        # nums1.sort()
        # nums2.sort()
        # while(i<len(nums1) and j<len(nums2)):
        #     if nums1[i]==nums2[j]:
        #         res.append(nums1[i])
        #         i+=1
        #         j+=1
        #     elif nums1[i]>nums2[j]:
        #         j+=1
        #     else:
        #         i+=1
        # return res


