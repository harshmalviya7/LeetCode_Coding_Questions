# 658. Find K Closest Elements
# https://leetcode.com/problems/find-k-closest-elements/
import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l = []
        for i in arr:
            heapq.heappush(l, (abs(i - x), i))
        nums = []
        while (k):
            nums.append(heapq.heappop(l)[1])
            k -= 1
        print(nums)
        return sorted(nums)
        # l=0
        # r=len(arr)-k
        # while(l<r):
        #     mid=l+(r-l)//2
        #     if x-arr[mid]>arr[mid+k]-x:
        #         l=mid+1
        #     else:
        #         r=mid
        # return arr[l:l+k]
