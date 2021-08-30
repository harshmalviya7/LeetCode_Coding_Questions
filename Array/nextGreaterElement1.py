# 496. Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m={}
        for i in range(len(nums2)):
            m[nums2[i]]=i
        l=[]
        for i in nums1:
            a=m[i]
            b=i
            for j in range(a,len(nums2)):
                if nums2[j]>i:
                    b=nums2[j]
                    break
            if b==i:
                l.append(-1)
            else:
                l.append(b)
        return l