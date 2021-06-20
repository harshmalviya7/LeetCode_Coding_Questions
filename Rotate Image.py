def rotate_image(arr):
    for i in range(len(arr)):
        print(arr[i])
    print("Transpose----")
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]

    for i in range(len(arr)):
        print(arr[i])
    print("90 degree rotation---")

    for i in range(len(arr)):
        for j in range(0,len(arr)//2):
            arr[i][j], arr[i][len(arr)-1-j] = arr[i][len(arr)-1-j], arr[i][j]

    for i in range(len(arr)):
        print(arr[i])


rotate_image([[1,2,3],[4,5,6],[7,8,9]])
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# Transpose----
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]
# 90 degree rotation---
# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]