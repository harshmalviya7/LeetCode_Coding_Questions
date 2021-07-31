# 941. Valid Mountain Array
# https://leetcode.com/problems/valid-mountain-array/
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 1
        lengthArr = len(arr)

        while i < lengthArr and arr[i] > arr[i - 1]:
            i += 1

        if i == 1 or i == lengthArr:
            return False

        while i < lengthArr and arr[i] < arr[i - 1]:
            i += 1

        return i == lengthArr

#         if len(arr)<3:
#             return False
#         c=arr[0]
#         a=0
#         for i in range(1,len(arr)):
#             if a==0 and c<arr[i]:
#                 c=arr[i]
#             elif a==1 and c>arr[i]:
#                 c=arr[i]
#             elif c>arr[i] and i!=1:
#                 c=arr[i]
#                 a=1
#             else:
#                 return False
#         if a:
#             return True
#         else:
#             return False


