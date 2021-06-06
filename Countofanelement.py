#Geeks for geeks
# https://practice.geeksforgeeks.org/problems/number-of-occurrence2259/1
# https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1

class Solution:
    def binarySearch_left(self,arr,l,r,x):
        res=-1
        while l<=r:
            mid=(l+(r-l)//2)
            if arr[mid]==x:
                res=mid
                r=mid-1
            elif arr[mid]>x:
                r=mid-1
            else:
                l=mid+1
        return res
    def binarySearch_right(self,arr,l,r,x):
         res=-1
         while(l<=r):
             mid=l+(r-l)//2
             if arr[mid] == x:
                 res = mid
                 l = mid+1
             elif arr[mid] > x:
                 r = mid - 1
             else:
                 l = mid + 1
         return res


ob=Solution()
l=[1, 1,1 ,1,1,2,2,2,2, 3,3]   #2 count

print(ob.binarySearch_right(l,0,len(l)-1,2)-ob.binarySearch_left(l,0,len(l)-1,2)+1)   #4