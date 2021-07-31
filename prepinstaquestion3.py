# https://prepinsta.com/tcs-digital/programming-questions/question-3/

# n=[[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]]
n=[[1,2,3],[4,5,6],[7,8,9]]
k=2

print(n)
for i in range(len(n)-k+1):
    for j in range(len(n)-k+1):
        a=0
        for p in range(k):
            for q in range(k):
                a+=n[p+i][q+j]
                # print(n[p+i][q+1],end=" ")

        print(a,end=" ")
    print()
