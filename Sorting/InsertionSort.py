
def InsertionSort(n):
    print(n)
    for i in range(1,len(n)):
        a=n[i]
        j=i-1
        while j>=0 and n[j]>a:
            n[j+1]=n[j]
            j-=1
        n[j+1]=a
        print(n)
InsertionSort([12, 11, 13, 5, 6])
# [12, 11, 13, 5, 6]
# [11, 12, 13, 5, 6]
# [11, 12, 13, 5, 6]
# [5, 11, 12, 13, 6]
# [5, 6, 11, 12, 13]
InsertionSort([4, 1, 3, 9, 7])
# [4, 1, 3, 9, 7]
# [1, 4, 3, 9, 7]
# [1, 3, 4, 9, 7]
# [1, 3, 4, 9, 7]
# [1, 3, 4, 7, 9]
# #

