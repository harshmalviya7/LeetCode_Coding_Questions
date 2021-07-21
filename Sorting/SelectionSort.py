n=[2,3,4,2,5,6,7]
for i in range(len(n)):
    m=i
    for j in range(i + 1,len(n)):
        if n[m]>n[j]:
            m=j
    n[i],n[m]=n[m],n[i]

