
def first_duplicate(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i])-1] < 0:
            return abs(arr[i])
        else :
            arr[abs(arr[i])-1]=-arr[abs(arr[i])-1]
    return -1

print(first_duplicate([1,2,3,2,3,2]))



