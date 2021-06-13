def selectionSort(n):
    print(n)
    for i in range(len(n)-1):
        a=n[i]
        for j in range(i,len(n)):
            if n[i]>n[j]:
                n[i],n[j]=n[j],n[i]
        print(n)



selectionSort([4, 1, 3, 9, 7])
# [4, 1, 3, 9, 7]
# [1, 4, 3, 9, 7]
# [1, 3, 4, 9, 7]
# [1, 3, 4, 9, 7]
# [1, 3, 4, 7, 9]