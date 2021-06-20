#sorted array given then square it
#sort the array again

def squareArray(arr):
    print(arr)
    l=0
    r=len(arr)-1
    lst=[0]*len(arr)
    for i in range(len(arr)-1,-1,-1):

        if abs(arr[l])>abs(arr[r]) :
            lst[i]=arr[l]**2
            l+=1
        else:
            lst[i]=arr[r]**2
            r-=1
    print(lst)

squareArray([-2,-1,1,2,4])

