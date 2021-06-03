#geeksforgeeks
# https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1#

def rotate(arr,low,high):
    while(low<high):
        arr[low],arr[high]=arr[high],arr[low]
        low+=1
        high-=1
    return arr

if __name__=="__main__":
    a=[1,2,3,4,5,6,7,8,9]
    print(rotate(a,0,len(a)-1))